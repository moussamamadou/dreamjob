#!/usr/bin/env python3
"""Study a YouTube video: download it, grab one frame per shot, and pull the transcript.

For studying how other videos are paced and cut. Do not re-upload or recreate
the downloaded material.

Usage:
    python yt_study.py URL [--out DIR] [--scene 0.3] [--every 0] [--lang en] [--cookies-from-browser chrome]
    python yt_study.py --file video.mp4 [--subs video.en.vtt]   # skip the download

Output folder (one per video):
    video.mp4         the downloaded video (720p or lower)
    frames/           one JPG per shot change, named by timestamp (00-01-23.40.jpg)
    transcript.txt    the captions with timestamps, duplicates removed
    shots.md          shot list: time, length, frame and the words spoken during that shot
    contact_sheet.jpg every frame on one page, for a quick look at the cutting rhythm

Needs: Python 3.9+, ffmpeg and ffprobe on PATH, and `pip install yt-dlp`.
Optional: `pip install faster-whisper` to transcribe when the video has no captions.
"""
import argparse
import html
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kw)


def ts(seconds, sep=":"):
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}{sep}{int(m):02d}{sep}{s:05.2f}"


def slug(text):
    return re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")[:60] or "video"


# ---------- download ----------

def download(url, out_root, lang, browser=None):
    import yt_dlp

    base = {"quiet": True}
    if browser:
        base["cookiesfrombrowser"] = (browser,)
    with yt_dlp.YoutubeDL({**base, "skip_download": True}) as ydl:
        info = ydl.extract_info(url, download=False)
    folder = out_root / f"{slug(info.get('title', ''))}-{info['id']}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "info.json").write_text(json.dumps(
        {k: info.get(k) for k in ("id", "title", "channel", "upload_date", "duration",
                                  "view_count", "webpage_url", "description")},
        indent=2), encoding="utf-8")

    opts = {
        "outtmpl": str(folder / "video.%(ext)s"),
        "format": "bv*[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720]/b",
        "merge_output_format": "mp4",
        "writesubtitles": True,
        "writeautomaticsub": True,
        # only the original track: "en.*" would also pull dozens of auto-translations and trip a 429
        "subtitleslangs": [lang, f"{lang}-orig"],
        "subtitlesformat": "vtt",
        "noprogress": True,
        **base,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

    video = next(folder.glob("video.mp4"), None) or next(folder.glob("video.*"))
    subs = sorted(folder.glob("video*.vtt"))
    # prefer human captions over auto-generated ones (yt-dlp names both video.<lang>.vtt;
    # when both exist the manual one wins, so the first match is fine)
    return folder, video, (subs[0] if subs else None), info.get("title", "")


# ---------- transcript ----------

def parse_vtt(path):
    """Return [(start, end, text)] with YouTube's rolling-caption duplicates removed."""
    cues, start, end, lines = [], None, None, []
    stamp = re.compile(r"(\d+:)?(\d+):(\d+\.\d+)\s+-->\s+(\d+:)?(\d+):(\d+\.\d+)")

    def secs(h, m, s):
        return int((h or "0:")[:-1]) * 3600 + int(m) * 60 + float(s)

    def clean(line):
        line = re.sub(r"<[^>]+>", "", line)
        return html.unescape(re.sub(r"\s+", " ", line)).strip()

    def flush():
        if start is not None and lines:
            cues.append((start, end, [c for c in map(clean, lines) if c]))

    for raw in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        m = stamp.search(raw)
        if m:
            flush()
            start, end = secs(*m.group(1, 2, 3)), secs(*m.group(4, 5, 6))
            lines = []
        elif raw.strip() and start is not None and not raw.startswith(("NOTE", "WEBVTT", "Kind:", "Language:")):
            lines.append(raw.strip())
        elif raw.rstrip("\r") == "":  # cue separator; whitespace-only lines are caption padding
            flush()
            start, lines = None, []
    flush()

    # auto captions roll: each cue repeats the line before it, and tiny 10 ms cues repeat
    # the whole screen. Keep each line once, the first time it appears.
    out, seen = [], []
    for s, e, cue_lines in cues:
        new = [ln for ln in cue_lines if ln not in seen]
        seen = (seen + new)[-4:]
        if new:
            out.append((s, e, " ".join(new)))
    return out


def whisper_transcript(video):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None
    print("No captions found, transcribing with faster-whisper (this can take a while)...")
    model = WhisperModel("small", compute_type="int8")
    segments, _ = model.transcribe(str(video))
    return [(s.start, s.end, s.text.strip()) for s in segments]


# ---------- frames ----------

def duration_of(video):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=nw=1:nk=1", str(video)]).stdout
    return float(out.strip())


def shot_times(video, threshold, every):
    """Times (seconds) of each shot start. Scene detection, or a fixed interval if --every > 0."""
    dur = duration_of(video)
    if every > 0:
        return [round(t * every, 2) for t in range(int(dur // every) + 1)], dur
    res = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(video), "-an",
         "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"],
        text=True, capture_output=True)
    times = [float(x) for x in re.findall(r"pts_time:([\d.]+)", res.stderr)]
    times = [0.0] + [t for t in times if t > 0.3]
    # merge cuts closer than 0.4 s (flashes, transitions)
    merged = []
    for t in times:
        if not merged or t - merged[-1] >= 0.4:
            merged.append(t)
    return merged, dur


def grab_frames(video, times, frames_dir):
    frames_dir.mkdir(exist_ok=True)
    paths = []
    for t in times:
        p = frames_dir / f"{ts(t, '-')}.jpg"
        # grab slightly after the cut so the frame is not mid-transition
        run(["ffmpeg", "-hide_banner", "-y", "-ss", f"{t + 0.15:.2f}", "-i", str(video),
             "-frames:v", "1", "-q:v", "3", "-vf", "scale=640:-2", str(p)])
        paths.append(p)
    return paths


def contact_sheet(paths, times, out, cols=6):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return False
    if not paths:
        return False
    thumbs = [Image.open(p) for p in paths]
    w = 320
    h = int(thumbs[0].height * w / thumbs[0].width)
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * w, rows * (h + 22)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, (im, t) in enumerate(zip(thumbs, times)):
        x, y = (i % cols) * w, (i // cols) * (h + 22)
        sheet.paste(im.resize((w, h)), (x, y))
        draw.text((x + 4, y + h + 4), f"#{i + 1}  {ts(t)}", fill="black")
    sheet.save(out, quality=85)
    return True


# ---------- shot list ----------

def write_shots(folder, title, times, dur, paths, cues):
    lines = [f"# Shot list: {title}", "",
             f"{len(times)} shots in {ts(dur)}, average {dur / max(len(times), 1):.1f} s per shot.", "",
             "| # | Start | Length | Frame | Said during this shot |", "|---|---|---|---|---|"]
    for i, t in enumerate(times):
        end = times[i + 1] if i + 1 < len(times) else dur
        said = " ".join(c[2] for c in cues if t <= c[0] < end)  # each caption goes to the shot it starts in
        rel = paths[i].relative_to(folder).as_posix()
        lines.append(f"| {i + 1} | {ts(t)} | {end - t:.1f} s | ![]({rel}) | {said.replace('|', '/')} |")
    (folder / "shots.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", help="YouTube URL")
    ap.add_argument("--file", help="use a local video instead of downloading")
    ap.add_argument("--subs", help="local .vtt captions to use with --file")
    ap.add_argument("--out", default="yt_study_out", help="output root folder")
    ap.add_argument("--scene", type=float, default=0.3,
                    help="shot-change sensitivity, 0.2 catches more cuts, 0.4 fewer (default 0.3)")
    ap.add_argument("--every", type=float, default=0,
                    help="instead of shot detection, take one frame every N seconds")
    ap.add_argument("--lang", default="en", help="caption language (default en)")
    ap.add_argument("--cookies-from-browser", dest="browser",
                    help="chrome, firefox, edge or safari: use that browser's YouTube sign-in "
                         "if YouTube asks you to confirm you're not a bot")
    a = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            sys.exit(f"{tool} not found. Install ffmpeg first (https://ffmpeg.org/download.html).")

    out_root = Path(a.out)
    if a.file:
        video = Path(a.file)
        folder = out_root / slug(video.stem)
        folder.mkdir(parents=True, exist_ok=True)
        subs, title = (Path(a.subs) if a.subs else None), video.stem
    elif a.url:
        print("Downloading...")
        try:
            folder, video, subs, title = download(a.url, out_root, a.lang, a.browser)
        except Exception as e:
            msg = str(e)
            if "not a bot" in msg:
                sys.exit("YouTube asked to confirm you're not a bot. Run again with "
                         "--cookies-from-browser chrome (or firefox, edge, safari) while signed in to YouTube.")
            sys.exit(f"Download failed: {msg}\nTry `pip install -U yt-dlp`; YouTube changes often.")
    else:
        ap.error("give a URL or --file")

    cues = parse_vtt(subs) if subs else whisper_transcript(video)
    if cues:
        (folder / "transcript.txt").write_text(
            "\n".join(f"[{ts(s)}] {t}" for s, _, t in cues) + "\n", encoding="utf-8")
    else:
        print("No captions and faster-whisper not installed: skipping the transcript.")

    print("Finding shots...")
    times, dur = shot_times(video, a.scene, a.every)
    print(f"Grabbing {len(times)} frames...")
    paths = grab_frames(video, times, folder / "frames")
    contact_sheet(paths, times, folder / "contact_sheet.jpg")
    write_shots(folder, title, times, dur, paths, cues or [])
    print(f"Done: {folder}")


if __name__ == "__main__":
    main()

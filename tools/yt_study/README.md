# yt_study

Downloads a YouTube video, saves one frame per shot and the transcript, and builds a shot list. Use it to study how a video is paced and cut. It is for reference only, so don't re-upload the material or recreate the video.

## Setup (once)

1. Install Python 3.9 or newer, and ffmpeg (https://ffmpeg.org/download.html). On a Mac with Homebrew: `brew install ffmpeg`.
2. `pip install yt-dlp pillow`
3. Optional: `pip install faster-whisper`. With it, the script makes a transcript when a video has no captions.

## Run

```
python yt_study.py "https://www.youtube.com/watch?v=PcK2W5cNqP4"
```

If YouTube says "confirm you're not a bot", sign in to YouTube in your browser and run:

```
python yt_study.py "URL" --cookies-from-browser chrome
```

Options:
- `--scene 0.2` catches more cuts. `--scene 0.4` catches fewer. The default is 0.3.
- `--every 2` takes one frame every 2 seconds instead of detecting cuts.
- `--lang fr` picks the caption language.
- `--out DIR` sets the output folder. The default is `yt_study_out`.
- `--file video.mp4 --subs video.en.vtt` uses files you already have and skips the download.

## Output (one folder per video)

| File | What it is |
|---|---|
| `video.mp4` | The video, at 720p or lower |
| `info.json` | Title, channel, date, views, duration |
| `frames/` | One JPG per shot, named by timestamp |
| `transcript.txt` | Timestamped captions, with YouTube's repeated lines removed |
| `shots.md` | Each shot's number, start time, length and frame, plus what was said during it. The header gives the average shot length. |
| `contact_sheet.jpg` | Every frame on one page |

If yt-dlp stops working, run `pip install -U yt-dlp`, because YouTube changes often.

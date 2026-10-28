# Cut Paper Noir: style guide

A portable visual style for animation, thumbnails, covers and title cards. It works in any project: swap the palette and keep the rules.

**In one line:** the world is built from hand-cut and torn paper, black does most of the work, a character is a silhouette with one or two features, and a single accent colour points the eye.

**Where it comes from:** Saul Bass's title sequences and posters (*The Man with the Golden Arm*, 1955; *Vertigo*, 1958; *Anatomy of a Murder*, 1959), Victor Haboush's giant-silhouette concept paintings for John Sutherland Productions (*The Littlest Giant*, 1955), and the Zagreb Film shorts of the late 1950s and 1960s. All three are covered in Amid Amidi's *Cartoon Modern* (Chronicle Books, 2006). Take the techniques, never copy a specific design.

---

## 1. Core rules

1. **Silhouette first.** Every subject must read from its outline alone. If you fill it solid black and can't tell what it is, redesign it.
2. **Paper, not vector.** Edges are cut with scissors or torn by hand. Nothing is perfectly straight or perfectly round.
3. **Black carries the frame.** Ink black covers 30 to 60 percent of most frames. Paper colour is the light.
4. **One or two features per character.** Eyes, a hatband, a cigar, a moustache. Everything else stays in the silhouette.
5. **Negative space is a shape.** Plan the empty paper as carefully as the figures. At least a third of the frame stays empty.
6. **One accent, used once.** The accent colour (red by default) appears once per frame, at the point of the story.
7. **Flat, always.** No gradients, no airbrush, no 3D lighting, no soft shadows. Depth comes from overlapping layers.

## 2. Palette

The palette is always four parts. Pick values per project; keep the proportions.

| Role | Share of frame | Default (Dream Job) | Rules |
|---|---|---|---|
| Ink | 30 to 60% | `#24211D` warm black | Never pure `#000000`; a warm or cool black reads as paper |
| Paper | 20 to 40% | `#EFE3C8` cream | Never pure white; it should look like stock |
| Flat colours (1 or 2) | 10 to 30% | mustard `#D9A23A`, teal `#2F7C78` | Mid-tones that sit between ink and paper |
| Accent | under 5% | stamp red `#C23A2B` | Once per frame, on paper or a light colour |

**Greyscale check:** convert every key frame to greyscale. The four roles must be four clearly different greys. In the default palette, red and teal are the same grey, so red never sits on teal.

**Other projects:** keep a warm or cool black, an off-white paper, two mid-tones and one hot accent. Examples: navy ink, bone paper, rust and sage, with signal orange; or plum ink, pink paper, olive and ochre, with vermilion.

## 3. Shapes and edges

- **Two edge types, two meanings.** Cut edges (clean, slightly wobbly scissor lines) for people, objects and architecture. Torn edges (rough, with a thin pale fibre line along the tear) for ground, sky, smoke, water and anything violent or chaotic.
- **Simple geometry, slightly off.** Rectangles that aren't quite square, circles that are a little flat. Verticals lean 2 to 6 degrees.
- **Overlap for depth.** Three to five paper layers per frame. Each layer can carry a very small drop shadow (1 to 3 px, ink at 25 to 40% opacity, offset down-right) to show it is paper lying on paper. Never a soft glow.
- **Scale contrast.** Put one huge shape against one tiny one: a giant shadow and a small man, a huge hand and a small coin.
- **Diagonals for tension.** Calm scenes sit on horizontals; danger tilts.

## 4. Characters

**Construction:** a character is two to five paper pieces: head, body, hat or hair, one or two hands. Arms and legs are simple strips or wedges. The silhouette must be unique in the cast (different hat, posture, size).

**Features:** cut separately and laid on top of the silhouette.

- Eyes: cream paper dots or slits on the black head. They carry most of the acting.
- One identifying detail in a flat colour: hatband, tie, lips, a scar cut as a light slash.
- No noses, mouths or ears unless one is the character's identifying detail.

**Expression kit:** silhouettes can still act. Change these cut-outs, not the whole drawing:

| Expression | Eyes | Lids and brows (a black strip over the eye) | Posture |
|---|---|---|---|
| Neutral, deadpan | Two round dots | None | Upright, centred |
| Smug | Half-circles, flat side up | Strip covering the top half | Leaning back, chin up |
| Sly, scheming | Narrow slits, both looking sideways | Slanted strip | Head tilted, shoulders up |
| Angry | Small dots | Two strips meeting in a V | Leaning forward, hands as fists or wedges |
| Surprised | Large circles with small ink pupils | Strips raised high, apart | Body stretched upward |
| Afraid | Large circles, pupils at the edge | Strips slanting up toward the centre | Hunched, smaller than usual |
| Sad, defeated | Small dots low in the face | Strips slanting down toward the outside | Drooping shoulders, hat low |
| Asleep, dead to the world | Two flat lines | None | Slumped |

A mouth may appear for one big moment (a wide grin, a shout) as a single cut shape in paper colour. Use it rarely so it lands.

## 5. Composition

- Two or three big shapes per frame, not ten small ones.
- Frame inside the frame: doorways, windows, prison bars, a spotlight circle, a picture frame.
- Put the accent where the eye should land last.
- Leave space for type in title cards and thumbnails: one clean paper area.
- Repeat a shape as a motif across a piece (a hat, a bar, a jagged tear) so a sequence feels designed.

## 6. Typography

- Best: hand-cut letters, uneven baselines, slightly different letter widths.
- Digital stand-in: a condensed grotesk or slab in heavy weight (for example Alfa Slab One or Archivo Black on Google Fonts), set in caps, with a subtle displacement filter on the edges so it looks cut.
- Text sits on paper strips or directly on black, never with a glow or outline.
- Stamps (HIRED, TERMINATED, CLASSIFIED) are paper rectangles in the accent colour with a rough edge, rotated 5 to 12 degrees.

## 7. Motion (for animation)

- **Cut-out animation.** Pieces slide, rotate on pins and snap into place. No morphing or smooth deformation.
- **Stepped timing.** Characters move on twos or threes (12 or 8 drawings per second); the camera and paper layers can move on ones.
- **Paper physics.** Pieces arrive with a slight overshoot and settle. A layer can flutter once when it lands.
- **Bass bars.** Long strips of paper slide across the frame to wipe between scenes or to build a title.
- **Reveal by cutting.** A shape is cut away to reveal what's behind it, or a torn strip is pulled off.
- **Camera.** Slow pushes and pans across flat layers, at most three parallax planes. No 3D camera moves.
- **Finish.** Fine paper grain over everything, a very light gate weave (1 to 2 px), and an occasional dust speck.

## 8. When to use it, and when not

**Strong for:** title sequences, thumbnails, book and album covers, posters, serious or tragic moments, scenes of threat, chapter openers, logos and channel art.

**Weak for:** long stretches of dialogue, comedy that depends on a detailed face, and anything that must explain a complicated object. Over more than a few minutes it tires the eye; mix it with a richer style and keep Cut Paper Noir for the moments that matter.

**Violence and sensitive subjects:** imply, don't show. A torn red strip, an empty chair, a falling hat, a shadow. The style is good at weight without gore.

## 9. Prompt template for image models

Paste this, then describe the scene in one or two sentences. Replace the palette if the project uses its own.

```
Cut-paper illustration in the manner of Saul Bass title sequences and late-1950s Zagreb Film animation, with giant silhouettes like Victor Haboush's concept paintings. Hand-cut and torn paper shapes with slightly rough edges and a thin pale fibre line on torn edges, layered with very small paper shadows. Mostly ink black and cream paper, with flat mustard and teal. Characters are bold black silhouettes showing only one or two features cut from paper (dot eyes, a hatband). One small red accent shape. Strong graphic composition, large negative space, flat colour. Palette only: cream #EFE3C8, mustard #D9A23A, teal #2F7C78, ink #24211D, red #C23A2B. No gradients, no 3D, no photorealism, no text.

Scene: [what happens, who is in it, where the accent goes].
```

**Add for expression:** "His eyes are [smug half-circles under a slanted black brow strip]; posture [leaning back, chin up]."

**Avoid in prompts:** "vector", "flat design", "minimalist icon" (these give clean digital shapes, not paper); "noir film still" (gives photographic lighting).

## 10. Building assets

1. Generate or cut each character as separate pieces on a plain background: body, head, hat, each hand, and a sheet of eye and brow cut-outs.
2. Generate backgrounds as separate layers: far, middle, near.
3. Remove backgrounds, keep the rough edges, and add the small paper shadow in the compositor, not in the art.
4. Keep a library per character: silhouette, feature pieces, eye kit. Reuse it everywhere (video, thumbnail, print).
5. All lettering is live text in the editor, never baked into generated art.

## 11. Checklist before using a frame

- [ ] Every subject reads as a solid black silhouette.
- [ ] Edges look cut or torn, not vector-clean.
- [ ] Black covers about a third of the frame or more; a third or more is empty.
- [ ] Four roles, four different greys in greyscale.
- [ ] The accent appears once, at the point of the story, never on a colour of the same grey.
- [ ] No gradients, glows, soft shadows or 3D light.
- [ ] Characters show at most two features, and the eyes say what they feel.
- [ ] The frame still reads at 168 px wide (thumbnail size).

# Blueprint: style guide

A portable visual style for explainer video, heist and engineering stories, maps, thumbnails and book interiors. It works in any project: swap the palette and keep the rules.

**In one line:** everything is a technical drawing: plans, sections, cutaways and maps drawn in pale lines on a dark sheet, with people as tiny anonymous scale figures and the plan itself as the hero.

**Why it is face-free:** architects' scale figures have no faces; they are there only to show size. The characters of the story are the building, the route, the machine and the plan. A person, when one matters, is a scale figure with a label and one attribute (a hat), seen from far away.

**Where it comes from:** cyanotype and diazo engineering prints of the 19th and 20th centuries, mid-century cutaway illustration in popular-science magazines, the diagram sequences of 1950s industrial and educational films (such as those by John Sutherland Productions covered in Amid Amidi's *Cartoon Modern*, Chronicle Books, 2006), and the precise plan-view title designs of the period. *References from memory: check before quoting them on screen.* Take the technique, never copy a specific drawing.

---

## 1. Core rules

1. **Drawn, not painted.** Everything is line: outlines, hatching, dimension lines. Fills are allowed only as flat tints inside closed shapes.
2. **Orthographic views only.** Plan (from above), section (sliced), elevation (from the side) and isometric cutaway. Never a camera perspective.
3. **The plan is the hero.** A scene answers "where" and "how": the route, the vault, the tunnel, the ship's hold.
4. **People are scale figures.** Tiny, faceless, in simple poses, always smaller than 10% of frame height.
5. **Annotate like an engineer.** Dimension lines, callout circles with numbers, north arrows, scale bars, title blocks. The deadpan lives in the annotations.
6. **One accent line.** The accent colour draws the one thing that happens: the route taken, the tunnel dug, the wall breached.
7. **The sheet is the frame.** Every shot is a drawing sheet with a margin and a title block. Change the sheet number to change the scene.

## 2. Palette

| Role | Share of frame | Default (Dream Job) | Rules |
|---|---|---|---|
| Sheet | 60 to 80% | teal-ink `#1F4F4C` (a darkened teal) | Dark, flat, slight paper grain |
| Line | 10 to 25% | cream `#EFE3C8` | All drawing; 2 line weights only |
| Tint | 5 to 15% | mustard `#D9A23A` at 60% | Fills for walls cut in section, water, the zone in play |
| Accent | under 5% | stamp red `#C23A2B` | The route, the breach, the X |

**Greyscale check:** the accent line must be clearly brighter or darker than the sheet in greyscale. Red on dark teal is weak in greyscale, so the accent line is always drawn with a cream 1 px edge either side, or a thicker weight than any other line.

**Light version (for print and book interiors):** cream sheet, ink lines, mustard tint, red accent. Same rules.

**Other projects:** classic blueprint (Prussian blue `#1D3B6E`, white lines, yellow route); sepia engineering print (tan sheet, brown lines, oxblood route); night-ops (near-black sheet, pale green lines, amber route).

## 3. Lines and shapes

- **Two weights.** Heavy (3 px at 1080p) for cut walls and outlines; light (1 px) for hatching, dimensions and furniture.
- **Hatching** marks cut material: 45-degree lines for masonry, cross-hatch for steel, dots for earth.
- **Slightly hand-drawn.** Lines are near-straight with tiny wobble; corners overlap a hair, as in a hand-inked drawing.
- **Callouts.** Numbered circles with leader lines; the legend sits in a box bottom right.
- **Title block.** Bottom right of every sheet: project name, sheet title, sheet number, date, a "drawn by" field (the deadpan line goes here: "DRAWN BY: THE COMPETITION").

## 4. Characters without faces

| Element | Rule |
|---|---|
| Body | Architect scale figure: oval head, simple body, no features, line only or flat tint |
| Identity | One attribute in silhouette (hat, cane, tricorn) and a callout label |
| Groups | Gangs, police, crews: clusters of scale figures with a group tint |
| Seen from above | In plan view a person is a circle (head) with a shoulder oval; the label does the work |
| Movement | A person is a dot moving along a dashed line; the accent line traces his route |

The case study can also be represented by his **object in plan**: a car, a ship, a safe, seen from above with a callout.

## 5. Composition

- One drawing per sheet; a second small detail view is allowed (circled, "DETAIL A").
- The drawing sits off-centre; the legend, scale bar and north arrow fill the rest.
- Use the section view for reveals: the camera slices through the wall and shows what is inside.
- Thumbnails: one bold plan, one red X or route, a three-word title in the title block style.
- 9:16: use elevation and section views (tall buildings, ship hulls, tunnels going down).

## 6. Typography

- Technical lettering in caps: a monoline, slightly condensed face (for example Archivo Narrow or a stencil face for labels).
- Labels sit on leader lines, never inside busy areas.
- Numbers are dimensions and quantities: "4.2 M", "11 YEARS", "$1,000,000". Set them plain.

## 7. Motion (for animation)

- **Draw-on.** Lines draw themselves in, like a pen plotter: outlines first, then hatching, then labels.
- **Route trace.** The accent line traces the action along a dashed path, with a dot for the person.
- **Section slide.** A cutting plane slides across the drawing and reveals the inside.
- **Sheet flip.** Scene changes are a new sheet sliding over the old one, with the sheet number changing.
- **Callout pop.** Circled numbers pop in on the beat the voice names them.
- **Camera.** Locked, or slow pans and pushes across the sheet. No rotation.
- **Finish.** Paper grain, a slight vignette, faint fold lines on the sheet.

## 8. When to use it, and when not

**Strong for:** heists, escapes, tunnels, sieges, prisons, ships, routes and journeys, inventions and machines, explainers, "how it was done" Shorts, book interiors (prints crisply in black and white).

**Weak for:** emotion, close personal moments, comedy that needs a performance. Mix with a mood style for those.

**Violence and sensitive subjects:** an X on a plan, a callout reading "SITE OF THE INCIDENT", a filled tint in a room. Distance gives dignity.

## 9. Building it

Mostly code, a little generation.

1. **Code (Remotion + SVG):** sheets, title blocks, scale bars, callouts, routes, dimension lines, scale figures (a small SVG set: standing, walking, sitting, group of three; each with optional hat). Draw-on animation uses SVG stroke-dashoffset.
2. **Generated, then vectorised:** complex plans and cutaways (a bank floor plan, a ship's section). Generate in line only, on a plain background, then vectorise so lines can be animated.

```
Technical drawing in the manner of a mid-century engineering blueprint. [Plan / section / isometric cutaway] of [subject]. Cream line work on a flat dark teal #1F4F4C sheet, two line weights, 45-degree hatching on cut walls, no shading, no perspective, no people, no text, no labels, clean margins.
```

3. For real places, base the plan on a documented source (period plan, court exhibit, map) and say so; otherwise label the drawing "ILLUSTRATIVE" in the title block.

**Avoid in prompts:** "blueprint style poster", "sci-fi HUD", "hologram" (gives glowing neon and fake UI).

**Credit budget:** 1 to 3 generations per episode for plans; everything else is code.

## 10. Checklist before using a frame

- [ ] Orthographic view only; no camera perspective.
- [ ] Only two line weights.
- [ ] People are tiny, faceless, labelled.
- [ ] One accent line or mark, readable in greyscale.
- [ ] A title block with sheet number is present.
- [ ] Real places are based on a documented source, or labelled illustrative.
- [ ] The frame still reads at 168 px wide (thumbnail size).

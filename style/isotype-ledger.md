# Isotype Ledger: style guide

A portable visual style for explainer video, thumbnails, book interiors and infographics. It works in any project: swap the palette and the pictogram set, keep the rules.

**In one line:** people are identical pictograms, numbers are rows of pictograms, and the story is told by counting, sorting and moving them on a clean flat page, like a 1950s company training chart.

**Why it is face-free:** a pictogram has no face by design. Every "person" is the same symbol; identity comes from one attribute (a hat, a colour, a position in the row). Nothing can drift because nothing is drawn twice: one SVG symbol is reused for the whole series.

**Where it comes from:** the Isotype method (International System of Typographic Picture Education) developed in Vienna from 1925 by Otto Neurath, Marie Neurath (née Reidemeister) and the woodcut artist Gerd Arntz, and the charts and diagram sequences in American industrial and educational films of the 1950s, such as John Sutherland Productions' *A Is for Atom* (1953) and *Destination Earth* (1956), covered in Amid Amidi's *Cartoon Modern* (Chronicle Books, 2006). Take the method, never copy Arntz's actual symbols. *Dates and names here are from memory: check before quoting them on screen.*

---

## 1. Core rules

1. **One symbol, one meaning.** A man is always the same man-symbol. A dollar is always the same coin. Never redraw a symbol for one scene.
2. **More means more symbols, never a bigger symbol.** Ten thousand dollars is ten coins, not one big coin. This is the Isotype rule and the source of the deadpan.
3. **Every symbol stands for a fixed unit.** State the unit once on screen ("1 figure = 100 employees") and keep it for the whole piece.
4. **Rows, not piles.** Symbols line up on a grid, evenly spaced, reading left to right. Rounding is shown as a cut symbol (half a man is half a man).
5. **No faces, no perspective, no shading.** Symbols are flat solid shapes seen from the front or the side. Depth does not exist.
6. **Colour sorts, it doesn't decorate.** A colour means a group (police, gang, public). Keep the meaning for the whole piece.
7. **One accent, for the point.** The accent colour marks the one symbol or number the story is about.

## 2. Palette

The palette is always four parts. Pick values per project; keep the proportions.

| Role | Share of frame | Default (Dream Job) | Rules |
|---|---|---|---|
| Paper | 50 to 70% | `#EFE3C8` cream | The page. Never pure white |
| Ink | 15 to 30% | `#24211D` warm black | Default symbol colour, rules, type |
| Group colours (2) | 10 to 25% | mustard `#D9A23A`, teal `#2F7C78` | Each one means one group, all piece long |
| Accent | under 5% | stamp red `#C23A2B` | The one thing the scene is about |

**Greyscale check:** every group colour must be a different grey from the others and from the ink. In the default palette, red and teal are the same grey, so a red symbol never sits in a teal row.

**Other projects:** a finance channel might use bone paper, navy ink, green and grey groups, orange accent. A history channel: parchment paper, sepia ink, oxblood and slate, gold accent.

## 3. Symbols

- **Built on a grid.** Draw each symbol on a 24 by 24 unit grid with a 2-unit margin. Heads are circles, bodies are trapezoids or rounded rectangles, limbs are straight bars. No curves you can't draw with a compass and ruler.
- **Solid fills only.** No outlines, no inner lines except cut-out gaps (a gap between arm and body, a gap at the waist).
- **Variants by one attribute.** The base figure plus a hat = a gangster. Plus a peaked cap = a policeman. Plus a briefcase = an accountant. Plus a crown = the boss. Never more than one attribute per symbol.
- **Objects follow the same grid.** Coin, bottle, gun, car, barrel, ship, building, document. Each is readable at 24 px.
- **The library is the cast.** One SVG file per symbol, stored once, reused across every episode and every project that shares the style.

**Starter library (about 30 symbols, covers most stories):** man, woman, child, boss (crown or top hat), worker (cap), police (peaked cap), judge (wig or gavel), prisoner (stripes), soldier, sailor; coin, banknote, money bag, bottle, barrel, gun, knife, car, truck, ship, train, house, bank, factory, jail, courthouse, newspaper, letter, ledger, clock, calendar page.

## 4. Characters without faces

The case study is not a different drawing. He is the same man-symbol with:

- **one attribute** (Capone: the fedora; Blackbeard: the tricorn; Ponzi: the cane),
- **the accent colour** while the story is about him,
- **a label** in small caps under him the first time he appears.

**Acting through arrangement, not expression:**

| Story beat | What the symbols do |
|---|---|
| Hired | The figure steps out of a grey crowd row into the empty space |
| Promoted | He moves up a row; the row above loses one figure |
| Rich | Coins stack beside him, row by row |
| Rivals | Two coloured groups face each other across a gap |
| Betrayal | One figure in his row turns to face the other way |
| Arrest | Police symbols close around him on the grid |
| Prison | Bars (vertical ink rules) drop over his cell of the grid |
| Death | The symbol is removed, leaving its grid cell empty. Told straight, held for a beat |

## 5. Composition

- One chart per frame: a row, a column chart, a flow, or a map. Never two.
- Half the frame is empty paper. Put the title of the chart in it.
- Strong baseline: symbols stand on a thin ink rule.
- Comparisons sit side by side at the same scale, never at two scales.
- For 9:16, stack rows vertically; never shrink symbols below 48 px tall.

## 6. Typography

- A clean grotesk in caps for labels (for example Archivo or Futura-like fonts), a slab for titles (Alfa Slab One).
- Labels sit under symbols, never on them.
- Numbers are set large and plain. Deadpan comes from the number, not from the type.
- The unit key ("1 figure = 1,000 cases") appears bottom left, small.

## 7. Motion (for animation)

- **Symbols count in.** Each new symbol pops in on a beat, left to right, 3 to 5 frames apart. Counting is the animation.
- **Slide on the grid.** Symbols move only along rows and columns, snapping to cells with a small overshoot.
- **Sort and regroup.** The signature move: a mixed crowd sorts itself into coloured rows.
- **No bending.** Symbols never walk, bend or deform. They slide, pop, flip (to face the other way) and vanish.
- **Camera.** Mostly locked. Slow zoom out to reveal that the row is much longer than you thought.
- **Finish.** A very light paper grain and a slight print mis-registration (1 px colour offset) to feel printed, not digital.

## 8. When to use it, and when not

**Strong for:** money, scale, crowds, before/after, "how many", career timelines, organisation charts, maps of territory, book interiors (it prints perfectly in black and white), Shorts of the "Tricks of the trade" type.

**Weak for:** emotion, atmosphere, a single dramatic moment, landscapes. Mix it with a mood style (Cut Paper Noir, Silhouette Theatre) for the moments that need weight.

**Violence and sensitive subjects:** a removed symbol and an empty cell carry a death with dignity. Never animate a symbol falling over.

## 9. Building it (no image model needed)

This style is built in code, not generated. That is its main advantage.

1. Draw the starter library once as SVG (by hand in Figma or Illustrator, or written directly as SVG paths on the 24-unit grid).
2. In Remotion, a `<SymbolRow symbol="man" count={12} accent={3} />` component lays symbols on the grid and staggers their entrance. A `<Chart>` component holds the baseline, title and unit key.
3. Per episode, only data changes: counts, labels, which symbol is accented.
4. For print (book interiors), export the same SVGs in black on cream; group colours become ink, 50% tint and outline-free hatch.

**If an image model is used at all**, only for one-off objects missing from the library, with this prompt, then vectorise and clean by hand:

```
Isotype pictogram in the manner of 1930s Vienna-method picture statistics. A single flat solid symbol of [object], front view, built from simple geometric shapes on a square grid, no outline, no shading, no face, no perspective. One flat colour #24211D on a plain #EFE3C8 background. No text.
```

**Avoid in prompts:** "icon", "emoji", "infographic" (gives glossy app icons and gradients).

## 10. Checklist before using a frame

- [ ] Every symbol comes from the library; none was redrawn for this scene.
- [ ] Quantities are shown by count, never by size.
- [ ] The unit key is on screen whenever a count is.
- [ ] Each colour still means the same group as in the first scene.
- [ ] The accent marks one thing only.
- [ ] Half the frame is empty paper.
- [ ] No faces, outlines, gradients or perspective.
- [ ] The chart still reads at 168 px wide (thumbnail size).

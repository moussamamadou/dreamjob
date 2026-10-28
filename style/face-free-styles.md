# Face-free styles: overview

Six visual styles that never depend on a face or on drawing the same character twice. Each one is a standalone guide that works for any channel: swap the palette and the props, keep the rules.

## The six

| Style | Guide | The character is... | Built with | Image credits per episode | Best for |
|---|---|---|---|---|---|
| Cut Paper Noir | [cut-paper-noir.md](cut-paper-noir.md) | a black silhouette with dot eyes and one feature | Image model + compositor | about 10 to 20 | Titles, thumbnails, covers, threat and tragedy |
| Silhouette Theatre (WHO AM I?) | the power-channel-episode skill | a black puppet in profile, lit from behind | Image model (puppet kit) + Remotion light | about 5 to 15 | Mystery, biography, emotion |
| **Isotype Ledger** | [isotype-ledger.md](isotype-ledger.md) | the same pictogram as everyone, plus one hat and the accent colour | **Code only (SVG + Remotion)** | **0** | Money, scale, careers, org charts, book interiors |
| Evidence Table | [evidence-table.md](evidence-table.md) | his objects and his sleeve cuff, seen from above | Image model for objects, code for documents | about 7 to 10 per character, then reused | Deals, crimes, documents, artefacts, thumbnails |
| Blueprint | [blueprint.md](blueprint.md) | a tiny labelled scale figure; the plan is the hero | Mostly code, 1 to 3 generated plans | 1 to 3 | Heists, escapes, routes, ships, machines |
| Game Board | [game-board.md](game-board.md) | a game token with one hat, in one colour | Code board + 1 generated token per character | 1 token per character, 2 to 4 board pieces | Journeys, rivalries, territory, series casts |

## Recommendation

**Make Isotype Ledger the workhorse and keep Cut Paper Noir for the big moments.**

- **Zero drift, zero credits.** The cast is one SVG library drawn once. Nothing is generated per episode, which matters with about 40 Recraft credits left and Scenario near its free limit.
- **It is the 1950s training film.** Pictogram charts of employees, rows of coins and org charts are exactly what a company training film showed. The voice ("Here's Bob") and the picture finally say the same thing.
- **It carries the jokes.** Promotion as a figure moving up a row, "early retirement" as a greyed-out figure, a fortune as a row of coins: the deadpan is in the counting.
- **It prints.** Book interiors are black on cream; Isotype was designed for print and survives black and white with no extra work.
- **It travels.** A finance, history or explainer channel reuses the same components with a new palette and a few new symbols.
- **Where it is weak** (emotion, atmosphere, deaths), Cut Paper Noir takes over for 10 to 20 percent of the runtime: the title card, the thumbnail, the arrest, the exit interview. That split also caps image generation at a handful of frames per episode.

Second choice: **Evidence Table**, if a richer, more illustrated look is wanted. It needs credits per character, but objects stay consistent far better than faces.

## What this changes for Dream Job

- The "one model sheet per outlaw" rule becomes "one symbol attribute and one silhouette per outlaw": a hat for Isotype, a silhouette for Cut Paper Noir.
- Thumbnails: the Cut Paper Noir silhouette on the career file with the red stamp, which already fits the thumbnail rule.
- Remotion: three components cover most of an episode: `SymbolRow`, `Chart` (baseline, title, unit key) and `CareerFile`.

## Samples (built in code, no credits)

- [face-free-samples/isotype-ledger-sample.png](face-free-samples/isotype-ledger-sample.png): "Promotion, 1925", the boss row and an early retirement.
- [face-free-samples/blueprint-sample.png](face-free-samples/blueprint-sample.png): a bank floor plan with a tunnel route.
- [face-free-samples/make-samples.js](face-free-samples/make-samples.js): the script that draws them (Playwright + SVG); the same shapes port straight to Remotion.

Both samples are illustrative; no data or plan in them is sourced.

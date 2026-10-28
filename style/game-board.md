# Game Board: style guide

A portable visual style for history, geography, strategy and career stories, in video, thumbnails, covers and Shorts. It works in any project: swap the board and the tokens, keep the rules.

**In one line:** the story is played as a mid-century board game: characters are wooden or tin game pieces, places are squares on an illustrated board, and events are cards drawn from the deck.

**Why it is face-free:** a game piece has no face. Each character is a token with one shape (a pawn wearing a fedora, a tricorn, a crown) and one colour, drawn once and reused forever. Consistency is automatic because the piece is a fixed asset, not a drawing of a person.

**Where it comes from:** printed board games and pictorial maps of the 1930s to 1950s (track games like snakes-and-ladders and race games, illustrated city and state maps), playing-card design, and the flat graphic language of 1950s animation covered in Amid Amidi's *Cartoon Modern* (Chronicle Books, 2006). *References from memory: check before quoting them on screen.* Take the language, never copy a specific game's board, pieces or trademarks.

---

## 1. Core rules

1. **The board is the world.** Every place is a square, a space or a region on one board. The whole career is one route across it.
2. **Pieces, not people.** Characters are game tokens. They never bend, gesture or speak. They move, wobble, fall over (only when that is the honest picture of a defeat, never of a death) and are removed from the board.
3. **One token per character, for life.** Shape and colour never change. Promotion adds an object beside the token (a little crown, a stack of chips), never a new token.
4. **Events are cards.** A turn of fortune is a card flipped face up: "ADVANCE TO CHICAGO", "GO DIRECTLY TO ALCATRAZ", "PAY $215,000 IN BACK TAXES". The narrator reads it deadpan.
5. **Money is chips and play money.** Counted, stacked, paid out. Real figures, real dates.
6. **Seen from slightly above.** A flat three-quarter top view (about 60 degrees), or straight down for map moments. No dramatic camera angles.
7. **One accent, the case study.** His token is the only piece in the accent colour.

## 2. Palette

| Role | Share of frame | Default (Dream Job) | Rules |
|---|---|---|---|
| Board | 40 to 60% | cream `#EFE3C8` | Printed card stock, light grain |
| Board colours (2) | 20 to 35% | mustard `#D9A23A`, teal `#2F7C78` | Spaces, regions, card backs |
| Ink | 10 to 20% | `#24211D` | Printed lines, type, rival tokens |
| Accent | under 5% | stamp red `#C23A2B` | The case study's token and its route only |

**Greyscale check:** red and teal are the same grey in the default palette, so the red token never stands on a teal space without a cream ring under its base.

**Other projects:** a geography channel could use a sea-blue board with sand, olive and coral; a history channel, parchment board with oxblood, navy and gold.

## 3. Board, pieces and cards

- **Board:** printed look, slightly off-register colours, a coarse halftone in large areas, space names in a slab face. Paths are numbered squares; regions are flat colour fields with a thick ink border.
- **Tokens:** simple turned-wood or die-cast shapes: a pawn body with one hat or prop moulded on top. Solid colour, one highlight shape, one hard shadow.
- **Cards:** playing-card proportions, rounded corners, a flat-colour back with the series emblem, a cream face with a typewriter instruction and a small pictogram.
- **Dice, chips, play money, a sand timer:** shared props for every story.

## 4. Characters without faces

| Character type | Token |
|---|---|
| The case study | Accent-coloured pawn with his signature hat (fedora, tricorn, cowboy hat) |
| His crew | Smaller ink pawns, same hat, in a cluster |
| Rivals | Pawns in a board colour with a different hat |
| The law | Tall ink pawn with a peaked cap; the judge is a gavel-topped piece |
| The public | Plain unpainted wooden pawns |

**Acting through play:**

| Beat | What happens on the board |
|---|---|
| Hired | His token is placed on START |
| Lucky break | Dice roll, he jumps several squares |
| Promotion | Chips stack beside him; a small crown piece is added |
| Rivalry | Two tokens on the same space; one is pushed off |
| Arrest | Card: "GO DIRECTLY TO JAIL"; the token slides into the jail corner |
| Exit | The token is lifted off the board and laid on its side next to it. The board stays. Told straight, held |

## 5. Composition

- One area of the board per shot: a space, a corner, a region.
- The token sits on a third line; the card, when there is one, enters on the opposite third.
- The full board shot is the map of the whole career: use it at the start and the end.
- Thumbnail: one token, one card with three words, cream ground.
- 9:16: use the vertical track sections of the board, or a single card full frame.

## 6. Typography

- Space names and card titles in a heavy slab (Alfa Slab One), all caps.
- Card instructions in a typewriter face (Special Elite).
- Prices and numbers printed as on a game board: "$500", "MISS 2 TURNS".
- Every piece of text is live in the editor, never generated in the art.

## 7. Motion (for animation)

- **Hop moves.** Tokens move square to square in small arcs with a click, on twos.
- **Card flip.** Cards flip on a single axis with a slight hold before reading.
- **Dice.** A short, flat roll; the result is always the true event, not chance.
- **Board pans.** Slow pans along the route; a pull-out to the whole board at chapter ends.
- **Pieces settle.** Tokens land with a small wobble; chips stack with a tick each.
- **Finish.** Card-stock grain, slight print mis-registration, soft table-edge vignette.

## 8. When to use it, and when not

**Strong for:** careers, journeys, territories, rivalries, money, empires and wars told at a distance, series with recurring characters (the tokens are the cast), Shorts and thumbnails (a token plus a card reads instantly), merch and book covers.

**Weak for:** intimate scenes, grief, anything where the "game" framing would trivialise real victims. In those moments, step out of the game: the board goes dark and the narrator tells it straight over a still frame, or switch to a mood style.

**Violence and sensitive subjects:** never make a death a game move ("lose a life" cards, knocked-over pieces). Use the exit rule above, and never use the game for victims: victims are not pieces.

## 9. Building assets

1. **Tokens:** generate each token once on a plain background, then remove the background. Hats are the only per-character change, so one base pawn plus hat variants is enough.

```
Single painted wooden board-game pawn wearing a moulded [fedora / tricorn / cowboy hat], seen from slightly above, flat mid-century illustration, solid [colour] paint, one simple highlight shape, coarse halftone texture, centred on a plain #EFE3C8 background, no shadow, no face, no text.
```

2. **Board sections:** build in code where possible (squares, regions, borders, space names). For an illustrated region (a city skyline as a board corner), generate it without text:

```
Section of a 1950s printed board game, flat mid-century illustration, [subject] as a simple pictorial corner space, off-register flat colours, coarse halftone, palette only: cream #EFE3C8, mustard #D9A23A, teal #2F7C78, ink #24211D. No pieces, no text, no people.
```

3. **Cards, chips, money, dice:** code components, shared across projects.
4. Shadows added in Remotion, one direction for everything.

**Credit budget:** 1 token per character (6 per book), 2 to 4 board sections per episode; shared props are free.

## 10. Checklist before using a frame

- [ ] Every character is a token from the library; no new token was drawn for this scene.
- [ ] Only the case study's token is in the accent colour.
- [ ] Events shown as cards are true and sourced.
- [ ] No death or victim is shown as a game move.
- [ ] All text is live.
- [ ] The frame still reads at 168 px wide (thumbnail size).

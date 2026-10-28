# Evidence Table: style guide

A portable visual style for documentary video, thumbnails, covers and Shorts. It works in any project: swap the palette and the props, keep the rules.

**In one line:** the camera looks straight down at a table, and the story is told by the objects on it and the hands that move them; nobody's face is ever in frame.

**Why it is face-free:** people are present only as hands, cuffs and sleeves. A character is identified by his props (the cigar, the ledger, the fedora on the desk) and his sleeve (a pinstripe cuff, a lace cuff, a prison-stripe cuff). Objects are what image models keep consistent most easily, and a sleeve is far easier to repeat than a face.

**Where it comes from:** mid-century flat illustration of still lifes and desks in magazine and advertising art, the overhead object sequences in Charles and Ray Eames's films (such as *Toccata for Toy Trains*, 1957), Saul Bass's object-based title cards, and today's "knolling" flat-lay photography. *References from memory: check before quoting them on screen.* Take the method, never copy a specific design.

---

## 1. Core rules

1. **Top-down, always.** The camera is at 90 degrees over the table. No perspective, no horizon, no wall.
2. **Objects are the actors.** Every scene is said with 3 to 7 objects. If a beat cannot be shown by an object, it is shown by a document on the table.
3. **Hands only.** People appear as one or two hands with a cuff, entering from a frame edge. Never above the wrist cuff past the frame edge, never a face, never a reflection of one.
4. **One sleeve per character.** Each character owns one cuff design for the whole series. It is the face.
5. **The table is the set.** Change the surface to change the place or the era: green baize (casino), oak desk (office), steel (police lab), deck planks (pirate ship), courtroom table.
6. **Flat illustration, not photo.** Objects are drawn flat with one hard shadow each, like a printed catalogue.
7. **One accent object.** One object per frame carries the accent colour. It is the point of the beat.

## 2. Palette

| Role | Share of frame | Default (Dream Job) | Rules |
|---|---|---|---|
| Table surface | 40 to 60% | teal `#2F7C78` baize or ink `#24211D` desk | One surface colour per location |
| Paper and light objects | 15 to 30% | cream `#EFE3C8` | Documents, cards, cuffs |
| Object colour | 10 to 25% | mustard `#D9A23A` | Brass, wood, gold, tobacco |
| Ink | 10 to 20% | `#24211D` | Shadows, type on documents, dark objects |
| Accent | under 5% | stamp red `#C23A2B` | One object, once per frame |

**Greyscale check:** in the default palette red and teal are the same grey, so the red object must sit on a cream document, never straight on teal baize.

**Other projects:** a cooking channel could use a butcher-block surface, white plates and one tomato red; a science channel, black lab bench, steel grey and one signal green.

## 3. Objects and shadows

- **Drawn from directly above.** A glass is a circle with a rim; a hat is an oval with a band; a gun is its plan view.
- **One hard shadow per object**, offset down-right by the same amount for the whole piece (default 3% of object size), ink at 35% opacity. The light never moves.
- **Simplified, slightly hand-made.** Mid-century flat shapes, a little off-true, a coarse halftone dot allowed on large areas.
- **Real scale between objects.** A coin is smaller than a glass. Scale tells the truth even when the tone is dry.
- **Documents are readable props.** Contracts, newspapers, telegrams, ledgers, receipts: their text is set live in the editor, never generated.

## 4. Characters without faces

A character is a **prop kit** plus a **cuff**:

| Element | Example (Capone) | Example (Blackbeard) |
|---|---|---|
| Cuff | Grey pinstripe, white shirt cuff, diamond cufflink | Black coat cuff with a frayed lace edge |
| Signature object | Cigar in a brass ashtray | Slow-match fuse, smoking |
| Desk object | Ledger with a red ribbon | Brass compass |
| Status object | Fedora, upside down on the table | Tricorn |

**Acting through hands:**

| Feeling | Hands |
|---|---|
| Calm, in charge | One hand flat on the table, still |
| Greedy | Fingers spread over coins, pulling them in |
| Nervous | Fingers drumming, a coin turning |
| Angry | A fist landing; objects jump one frame |
| Signing a deal | Pen, two cuffs, a handshake over the document |
| Arrested | A second cuff (police) enters; a handcuff closes on the wrist |
| Gone | His objects stay; his hand doesn't come back. The ashtray smokes, then stops |

## 5. Composition

- The table fills the whole frame; no edge of the table is visible unless a hand comes from there.
- Rule of three: the accent object on a third line, never dead centre unless it is alone.
- Leave one clean area of table for live text in thumbnails and title cards.
- Over a sequence, objects accumulate: what the career built is literally on the table, and the exit interview clears it.
- In 9:16, crop to a column of the table; the camera can pan down the table as the story goes.

## 6. Typography

- Text belongs to objects: typed on a file card, stamped on a document, printed on a newspaper, written on a luggage tag. Use a typewriter face (Special Elite) for documents and a slab (Alfa Slab One) for headlines and stamps.
- Stamps (HIRED, PROMOTED, TERMINATED) are real stamps landing on a document, rotated 5 to 12 degrees.
- No floating captions over the table except the episode title card.

## 7. Motion (for animation)

- **Hands do everything.** Objects move only when a hand moves them, or when they are slid in from a frame edge as if by an unseen hand.
- **Slides and drops.** Objects slide in fast and stop with a small settle; dropped objects land with a 1-frame jump of everything nearby.
- **Swap cuts.** Cut between two states of the same table (before and after) on the same object positions.
- **Camera.** Locked overhead. Slow pans across the table or slow push-ins on one object. No rotation, no tilt.
- **Hands on twos.** Hand poses are a small library of drawings swapped on twos (12 per second), not smoothly animated.
- **Finish.** Paper grain, light halftone, an occasional cigarette-smoke wisp crossing frame (as flat cream shapes).

## 8. When to use it, and when not

**Strong for:** crime, money, deals, documents, heists, recipes, inventions, history told through artefacts, thumbnails (one object plus a stamp reads instantly), Shorts of the "Tricks of the trade" type, book chapter openers.

**Weak for:** crowds, landscapes, journeys, battles. Mix with a map or pictogram style for those.

**Violence and sensitive subjects:** imply with objects: a spilled glass, an empty chair pushed back into frame, a hat left on the table, a bullet casing. Never blood.

## 9. Prompt template for image models

Generate each object on its own, never a full table scene: separate objects are reusable, consistent and composited in Remotion.

```
Flat mid-century illustration of a single [object], seen from directly above, centred on a plain #EFE3C8 background. Simple slightly hand-made shapes, flat colour with a coarse halftone texture, no gradients, no perspective. Palette only: cream #EFE3C8, mustard #D9A23A, teal #2F7C78, ink #24211D, red #C23A2B. No shadow, no text, no hands, no people.
```

**Hands:** generate one cuff design as a set of 6 to 8 hand poses on one sheet (flat, open, fist, pointing, holding a pen, holding a glass, drumming, palm up), cropped at mid-forearm, seen from above:

```
Sheet of eight hand poses seen from directly above, cropped at mid-forearm, each with the same [cuff description] sleeve. Flat mid-century illustration, simple shapes, flat colour, coarse halftone texture, plain #EFE3C8 background, evenly spaced, no shadows, no faces, no text.
```

**Avoid in prompts:** "desk scene", "photo", "realistic", "3D" (gives perspective rooms and photographic light).

## 10. Building assets

1. Prop library per character: 4 to 8 objects, each a separate PNG with the background removed.
2. One hand sheet per cuff; cut each pose to its own PNG.
3. Table surfaces as tileable flat textures (one per location), which can also be made in code.
4. Shadows are added in Remotion (one shared offset), never baked into the art.
5. Documents are built in code: a cream rectangle, typewriter text, a stamp component.

**Credit budget:** about 6 objects plus 1 hand sheet per character, so roughly 7 to 10 generations per outlaw. Shared objects (coins, glasses, guns, telephones, newspapers) are made once and reused across every episode.

## 11. Checklist before using a frame

- [ ] The view is straight down; no perspective anywhere.
- [ ] No face, no head, no reflection of one.
- [ ] Every hand wears its character's cuff.
- [ ] All shadows share one direction and length.
- [ ] One accent object, not on a colour of the same grey.
- [ ] All text is live, on an object.
- [ ] The frame still reads at 168 px wide (thumbnail size).

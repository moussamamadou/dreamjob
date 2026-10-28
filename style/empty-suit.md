# Empty Suit: style guide

A portable visual style for video, thumbnails, covers and Shorts. It works in any project: swap the palette and the props, keep the rules.

**In one line:** every character is his clothes with nobody inside: a floating hat, an empty suit, gloves that hold the cigar.

**The twist:** The invisible man. Absence is the joke and the point: a career with no person in it, just the job.

**Why it is face-free:** There is no head at all, so there is no face to drift. Clothes are far more stable for models than people, and the costume is the character.

**Where it comes from:** H. G. Wells's *The Invisible Man* (1897) and its film versions, the floating-clothes gags of 1930s to 1950s cartoons, and flat mid-century magazine illustration. *References from memory.* Take the technique, never copy a specific design.

---

## 1. Core rules

1. Nobody inside. A gap where the head and neck would be, empty cuffs, an empty collar.
2. The hat floats a hand's width above the collar, always at the same height.
3. Gloves are the hands. White gloves for the case study; other characters wear their own glove colour.
4. The costume is fixed per character: hat, suit, tie, gloves.
5. Flat sets: wall, floor, one desk or doorway.
6. One accent: the tie, the cigar tip, a stamp.
7. Death is told by the clothes falling: the suit slumps empty onto the chair, the hat lands last. Told straight, held.

## 2. Palette

| Role | Share | Default (Dream Job) |
|---|---|---|
| Ground | 40 to 60% | cream `#EFE3C8` or the set colour |
| Main colours | 20 to 35% | mustard `#D9A23A`, teal `#2F7C78` |
| Ink | 10 to 20% | `#24211D` |
| Accent | under 5% | red `#C23A2B`, once per frame |

**Greyscale check:** red and teal are the same grey in the default palette, so the accent never sits on teal. Other channels keep the structure: one ground, two mid-tones, an ink, one hot accent.

## 3. Cast

Case study: his hat, suit and white gloves. Crew: same hat, darker suits. Police: peaked cap and badge on an empty uniform. Public: plain empty coats.

Make one reference sheet per recurring character (front, side, back, on a plain background) and use it as the image reference for every later shot.

## 4. Composition and type

- One or two characters per frame, one clear action.
- Leave one clean area for live text in thumbnails and title cards.
- All text, stamps and the career file are added in Remotion, never generated.

## 5. Motion

**In MiniMax:** Very good. Cloth drifts and falls naturally; the hat bobbing, gloves counting money, a suit walking away. Risk: models may fill the suit with a body or a head; prompt 'the clothes are empty, no head, no body' and cut those clips.

General MiniMax rules: one motion per clip, describe camera and motion only, no text in the frame, and QA the contact sheet for faces appearing, extra limbs and duplicated objects. Remotion handles cuts, text, stamps and counters.

## 6. Prompt template

```
Flat mid-century illustration. An invisible man: an empty [suit] and a [hat] floating in mid-air with nobody inside, empty space where the head should be, [glove colour] gloves [action], [location as flat planes]. Simple shapes, one hard shadow, coarse halftone grain. Palette: cream #EFE3C8, mustard #D9A23A, teal #2F7C78, ink #24211D, red #C23A2B. No text, no face, no head, no body visible.
```

## 7. When to use it

**Strong for:** Careers, business, satire, any 'it could be anyone' story, finance and self-help channels.

**Weak for:** Crowds (too many floating hats get busy), victims (never show a victim as empty clothes).

## 8. Checklist

- [ ] No face, eyes or mouth anywhere.
- [ ] Each character matches his reference sheet.
- [ ] One accent, not on teal.
- [ ] No text in the art.
- [ ] Deaths and victims told straight, never as a gag.
- [ ] Reads at 168 px wide (thumbnail size).

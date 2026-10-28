# Wooden Manikin: style guide

A portable visual style for video, thumbnails, covers and Shorts. It works in any project: swap the palette and the costumes, keep the rules.

**In one line:** every person is the same faceless wooden artist's manikin, dressed in a costume and a hat, acting in flat mid-century sets.

**Why it is face-free:** the drawing manikin has a blank oval head by nature. One base figure is the whole cast; a character is a costume (fedora and pinstripes, tricorn and coat, cowboy hat and duster). Image and video models keep a jointed wooden figure far more stable than a face, and the joints make poses easy to describe.

**Where it comes from:** the jointed wooden lay figure used by painters since the Renaissance, the faceless mannequins of Giorgio de Chirico's metaphysical paintings, and flat mid-century set design from 1950s animation (Amid Amidi, *Cartoon Modern*, Chronicle Books, 2006). *References from memory: check before quoting them on screen.*

---

## 1. Core rules

1. **One manikin for everyone.** Same pale wood, same oval head, same ball joints. Never carve a face, never paint eyes.
2. **The costume is the character.** One hat, one jacket, one prop per character, fixed for the series.
3. **Body language does the acting.** Lean, slump, reach, clench. The joints make poses clear; use big, readable poses.
4. **Flat sets, real wood.** The manikin has gentle matte shading and wood grain; the set behind it is flat colour planes with one hard shadow.
5. **Scale tells status.** A boss manikin can be the same figure on a taller chair, never a bigger figure.
6. **One accent object per frame**, at the point of the beat.
7. **Death is told by stillness.** A manikin lying folded at the joints, or an empty costume on a chair. Never broken limbs.

## 2. Palette

| Role | Share | Default (Dream Job) | Rules |
|---|---|---|---|
| Set walls | 40 to 60% | mustard `#D9A23A` or teal `#2F7C78` | One wall colour per location |
| Floor and paper | 15 to 30% | cream `#EFE3C8` | |
| Wood | 5 to 15% | natural pale wood | The same wood in every shot |
| Ink | 10 to 20% | `#24211D` | Shadows, suits, furniture lines |
| Accent | under 5% | stamp red `#C23A2B` | One object |

## 3. Characters

| Element | Rule |
|---|---|
| Base | Pale wooden manikin, blank oval head, visible ball joints at neck, shoulders, elbows, wrists, hips, knees |
| Costume | Real cloth-looking clothes over the wood: jacket, coat, hat. Hands stay bare wood |
| Identity | One hat + one costume + one prop (cigar, cane, cutlass) |
| Groups | Crews wear the same hat in another colour; the public wears no costume at all |

**Expression kit (pose only):** confident (chest out, hand on hip), smug (leaning back, feet on desk), scheming (head tilted down, hands together), angry (leaning forward, fist on table), afraid (shoulders up, arms in), defeated (head down, arms hanging), arrested (hands behind back, flanked by two cap-wearing manikins).

## 4. Composition and type

- One or two manikins per frame, medium or wide shot; the whole body or the top half, never a close-up of the head.
- Sets are simple: a wall, a floor line, two or three props.
- Leave a clean wall area for live text in thumbnails.
- All text is added in Remotion. Typography as in the series: slab for titles, typewriter for documents.

## 5. Motion

- **In MiniMax: very good fit.** Jointed wooden figures move plausibly: a turn of the head, a reach for coins, standing up, sitting down. One action per clip, camera locked or a slow push.
- Prompt motion as body mechanics ("the wooden manikin slowly turns its head toward the door and lowers its hand"), never as emotion.
- Remotion for cuts, text, stamps and transitions.
- QA for: extra joints or fingers, the head growing features, the costume changing colour.

## 6. Prompt template

```
A smooth wooden artist's drawing manikin with no face, blank oval head, visible ball joints, wearing [costume and hat], [pose and action]. Flat mid-century set: [location as two or three flat colour planes]. Simple stylised illustration, soft matte surfaces on the wood, one hard shadow. Palette: cream #EFE3C8, mustard #D9A23A, teal #2F7C78, ink #24211D, one small red #C23A2B [accent object]. No text, no human faces.
```

**Avoid:** "mannequin" alone (gives shop-window dummies with faces), "robot", "puppet" (gives painted faces).

## 7. Building assets

1. Make one costume sheet per character: the manikin in costume, front, side and back, on a plain background. Use it as the image reference for every later shot.
2. Generate sets empty, then generate or composite the manikin in.
3. Credit budget: 1 costume sheet per character, then about 1 frame per shot.

## 8. When to use it

**Strong for:** any story with people doing things: careers, deals, arguments, self-help, history, business explainers. Reusable across channels with only new costumes.

**Weak for:** crowds (use few figures), grief close-ups (go wide and still).

## 9. Checklist

- [ ] No face, eyes or mouth on any head.
- [ ] Each character wears exactly his costume and hat.
- [ ] The pose reads clearly at thumbnail size.
- [ ] One accent object.
- [ ] No text in the art.

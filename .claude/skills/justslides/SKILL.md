---
name: justslides
description: Build a self-contained HTML slide deck (960×540, click-by-click reveals, speaker notes synced to clicks, presenter view, overview grid, print to PDF) in the JustSlides house style from just a topic. Use whenever the user asks for slides, a deck, a presentation, a lecture, a discussion section, a paper presentation, a micro-teaching lesson, 幻灯片, PPT or 课件, unless they explicitly ask for .pptx / Google Slides / Keynote.
---

# JustSlides: HTML slide decks in the house style

**Made for presenting, not decorating.** Every choice serves the person giving the talk and
the audience following the argument: a click reveals the next step of the reasoning, the
notes say what to say after that click, and the style stays plain so nothing competes with
the content. When in doubt, cut decoration and add a click or a sentence of notes.

You produce **one `.html` file** that opens in any browser with no build step and no network
dependency except Google Fonts (which degrades gracefully to Times New Roman). The file contains:

- a fixed 960×540 canvas scaled to the window, white slides on a dark chrome;
- per-slide **click steps**: elements appear (or disappear, or glide) one click at a time;
- **speaker notes** keyed to clicks with `★` markers, a **presenter view** (press `P`) with
  timer, next-slide preview and "N more clicks" indicator, an overview grid (`G`), fullscreen
  (`F`), animation toggle (`A`), and `@media print` so "Print → PDF" gives one page per slide.

The engine (CSS + JS) already exists in `template.html` next to this file. **Never rewrite the
engine. Copy the template and fill in the slides and the notes.** Everything you author lives
between the `SLIDES START/END` markers and inside the `NOTES` array.

Finished decks that show the quality bar live in `examples/` at the repository root, named
`<type>-<topic>.html`. Read the one matching your deck type before your first deck:
`examples/lesson-binary-search.html` (teaching lesson with an interactive widget, flow layout),
`examples/discussion-agents-and-images.html` (course discussion with diagrams and SVG arrows),
`examples/paper-native-sparse-attention.html` (paper presentation with magic move, fade-outs,
count-ups, images). Name new decks the same way, `lesson-`, `discussion-` or `paper-` plus a
kebab-case topic, and write them to `output/` in the working directory.

## Workflow

1. **Pin down the brief.** Before writing anything, make sure you know **who the presenter
   is**: the name goes on the title slide and into the opening line of the notes. Use it if
   the user said it, or if your memory / project context already records it. Otherwise ask,
   in one short question, and wait for the answer; also ask whether a course or venue line is
   wanted. Never invent a name and never reuse one from the examples. If you are running
   somewhere that cannot ask (a batch job, a non-interactive agent), write `Presented by
   [PRESENTER]` and say so in your report.
   For everything else, infer from the topic and state your assumptions in one line: audience
   (students in which course / lab group / general) and length in minutes. Do not block on
   these; the default is 15 minutes.
2. **Outline before HTML.** Plan ~1 slide per 1–1.5 minutes (12–15 slides for 15 min). Every
   slide gets a one-sentence takeaway and a list of what each click reveals. Use the standard arc:
   title → hook or question → the core idea built up piece by piece (one running example
   reused across slides) → evidence / comparison → "Your turn" or Discussion questions →
   Takeaways + "Thank you! Questions?". For papers: problem → background the audience needs →
   method, one component per slide → results → discussion (is it used, follow-ups, weaknesses)
   → takeaways.
3. **Copy `template.html`** to `output/<type>-<kebab-topic>.html` (create `output/` if needed) and set `<title>`.
4. **Write the slides** following the rules below. Prefer a diagram the audience watches being
   built over a list they read.
5. **Write `NOTES`**: a full spoken script, one string per slide, `★` before the text for each
   click. Counts must match `data-steps` exactly (the checker enforces this).
6. **Check**: `python3 .claude/skills/justslides/scripts/check_deck.py <deck>.html` must print `OK`.
   Then look at every slide: run `.claude/skills/justslides/scripts/screenshot.sh <deck>.html`
   (headless Chrome, one PNG per slide with all clicks revealed; `<deck>.html?all#5` shows the
   same in a browser) and read the images, or open the deck and step through with `→` and `G`.
   Look for wrapped titles, text spilling out of boxes, overlaps near the footnote, and empty
   half-slides. Fix and recheck. Expect one round of fixes; that is normal.
7. Report: file path, slide count, total clicks, the keyboard hints (`← →` step, `P` presenter,
   `N` notes, `G` grid, `F` fullscreen, print to PDF), any assumption you made, and any
   placeholder left in the deck.

## Slide anatomy

```html
<section class="slide" style="background:#fff" data-i="qkv" data-steps="3">
  <div class="ttl a fx-down" data-s="0">Slide Title in Title Case</div>
  <div class="bd">
    <p class="sub a fx-fade" data-s="0">One-line framing that appears with the title.</p>
    <div class="pts a fx-up" data-s="1"> ... </div>
    <div class="call a fx-up" data-s="2" style="margin-top:24px">The takeaway.</div>
    <div class="a fx-fade" data-s="3"> ... </div>
  </div>
  <div class="pnum">5</div>
</section>
```

- `data-steps="N"` = number of clicks on the slide = the largest `data-s` (or `data-o`) inside.
- `data-s="k"`: element appears after click `k` (`0` = with the slide). Every element with
  `data-s` must also have `class="a fx-<name>"`, otherwise it is invisible forever.
- `--d:.3s` in the inline style delays an element within its click; stagger siblings by
  `0.1–0.15s` (`--d:0s`, `.12s`, `.24s` …) so a row of cards cascades in.
- `fx-down` for titles, `fx-up` for text blocks and cards, `fx-fade` for labels, lines and
  anything that should not move, `fx-left` for a row that slides in behind a `fx-growy` bar,
  `fx-growx` for horizontal rules and arrows, `fx-growy` for vertical bars, `fx-pop` for a
  highlighted box or a big number, `fx-draw` for SVG paths (needs `pathLength="1"
  stroke-dasharray="1"`).
- `data-o="k"`: element fades **out** at click `k` (use to replace a label, remove a wrong
  answer, or swap a diagram state). An element can have both `data-s` and `data-o`.
- `data-count="0.3"`: the first numeric text inside counts up from 0 after a 0.3s delay.
- `data-mm="key"`: Keynote-style magic move. Elements with the same key on consecutive slides
  glide from the old position/size to the new one when the slide changes.
- `data-i` is a free label for your own reference; `.pnum` is the visible page number (omit on
  the title slide).
- Slides must not overflow 960×540. Check with `G`.

Two layout modes, mix freely:

- **Flow mode** for text-led slides: `.ttl` + `.bd` and the helper classes in the template
  (`.h .sub .lab .txt .two .vr .stack .pts .pt .steps .tag .box .call table.cmp .src`).
- **Absolute mode** for diagrams: `<div class="el sh a fx-up" data-s="1" style="left:48px;
  top:108px;width:200px;height:60px;background:#eceef1;border-radius:3px"><div class="tx"
  style="inset:8px;justify-content:center;text-align:center"><p style="font-size:16px">
  label</p></div></div>`. Arrows and connectors go in one `<svg class="lines" viewBox="0 0 960
  540">` overlay per slide, in the same coordinate space as the boxes.

**Diagram-heavy decks are easier to build with a short Python script** that defines helpers
(`box(x, y, w, h, html, s, fx)`, `arrow(...)`, `callout(...)`), assembles the slides, checks
`★` counts, and splices the result into a copy of the template. Hand-typed coordinates drift;
generated ones stay consistent. Keep the script in the scratch directory, not the repo.

Snippets for every common slide type (cards, comparison table, big question, SVG arrows,
swap with `data-o`, magic move, count-up stat, image, interactive widget, discussion, takeaways)
are in `reference/patterns.md`. Copy from there rather than inventing new markup.

## Visual system (do not deviate)

| Role | Value |
|---|---|
| Slide font | `'Times New Roman', Tinos, serif` (set on `.slide`, so inline `font-family` is optional) |
| Title | 42.67px, `#1f2933`, left 48px, top ~29–38px, one line |
| Big title-slide heading | 53.33–64px |
| Body text | 21.33px (flow) or 16–19px (dense diagrams); never below 12.5px, and 11px only for the sources footnote |
| Section label | 13px uppercase, letter-spacing .06em, `#5f6b7a` |
| Ink | `#1f2933` |
| Muted | `#5f6b7a` |
| Accent (headings, bars, borders, highlighted cells) | `#3b5b7a` |
| Panel background | `#eceef1` (3px radius) |
| Highlighted panel / callout background | `#e1e8f0` with `border-left:4px solid #3b5b7a` |
| Success / "this one" / correct | `#4f7d5c` (text) with `#e8efe9` background |
| Warning / wrong / cost | `#9b3b3b` text, `#f4e7e7` background; `#b42318` for an alarming number |
| Hairlines, table rules | `#c5cbd3`; header rule `1.5px solid #1f2933` |
| Diagram tints (categories) | `#9db1c6` blue-grey, `#a9c3b1` sage, `#cfe0ef` pale blue, `#8a6f4e` brown |

Margins 48px left/right; content column ends at 912px. Title block occupies the top ~100px;
body runs from `top:108–116px` to `bottom:40px`; footnote sits at `bottom:12px`. Square
corners or 3–4px radius only. No shadows inside slides, no gradients, no icons or emoji, no
bold walls: bold is for the one key term per sentence and for the lead-in word of a point.

Sizing rules of thumb learned the hard way (960px wide, serif at these sizes):

- A 42.67px title fits about 45 characters on one line; shorten rather than wrap.
- A 40px number or short phrase needs about 11px per character of width.
- A callout at 16–17px that wraps to two lines needs `height ≥ 56px`.
- `table.cmp` rows are ~50px tall at the default padding; use `class="cmp num tight"` (~36px)
  when a table has four or more rows under a diagram.
- Content must end by `y ≈ 470` when the slide has a `.src` footnote (it sits at `bottom:12px`).
- A row of 4 cards at 204px wide takes 17px headings and 14px body; a 2 × 2 grid of 420 × 152px
  cards takes 19px headings and 16px body, about 35 words each.

## Writing rules

- Titles are claims or questions in Title Case ("Why Only 20 Guesses?", "No Single Best
  Attention"), not topics ("Complexity").
- One idea per slide, at most ~60 words visible at the end of all clicks. If you need more,
  split the slide or move words to the notes.
- Build arguments click by click: show the setup, ask the audience, then reveal. Polls, "Your
  turn" questions with answers behind a click, and live demos are encouraged for teaching decks.
- Numbers get `class="num"` (tabular figures) and thousands separators. Formulas use plain
  HTML (`<sub>`, `<sup>`, `<i>`), never LaTeX syntax.
- Cite real sources in an 11px `.src` footnote on slides that use external facts; never invent
  citations, numbers or results. If you are not sure of a fact, say so in the notes and keep it
  off the slide.
- Last two slides are usually Discussion (3–5 numbered open questions) and Takeaways (3–4
  `.pt` rows, then "Thank you! Questions?").

## Speaker notes rules

- `NOTES[i]` is the complete spoken script for slide `i` in a natural first-person voice,
  roughly 100–150 words per minute of talk. It must stand alone: a presenter who only reads
  the notes could deliver the talk.
- The text before the first `★` is said when the slide appears; the text after the k-th `★`
  is said right after click k. Therefore `NOTES[i].count('★') === data-steps` of slide i.
- Include stage directions where useful: "Ask the class…", "Pause for hands", "Click Start".
- Use double-quoted JSON-compatible strings (escape inner `"` as `\"`); the checker parses
  the array as JSON.

## Interactive widgets

Teaching decks may embed small interactive demos (a guessing game, a sorter, a slider). Put the
widget's root `<div id="…">` in the slide, its CSS in the content-helpers block, and its JS
**above** the engine code in the same `<script>`. Keep it dependency-free, make its buttons
`type="button"`, and give it a visible Restart button (the engine ignores clicks on buttons
when turning pages). See the `makeGame` code in `examples/lesson-binary-search.html` for a model.

## Hard constraints

- One file, no external JS or CSS except the Google Fonts link already in the template.
- Do not edit the engine CSS/JS; add new content CSS only in the content-helpers block.
- `check_deck.py` must pass and you must have looked at every slide (screenshots or browser)
  before declaring it done.
- Images: inline as `data:` URIs or reference a file next to the deck; keep the deck under
  ~2 MB unless the user supplies large figures.

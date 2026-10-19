# Slide patterns

Copy-paste snippets in the house style. All coordinates are in the 960×540 slide space.
`data-steps` on the `<section>` must equal the largest `data-s`/`data-o` used.

## 1. Title slide (no clicks)

```html
<section class="slide" style="background:#fff" data-i="title" data-steps="0">
<div class="el a fx-down" data-s="0" style="left:57.6px;top:96px;width:830px;font-size:53.33px;line-height:1.15;color:#1f2933">How Many Questions Does It Take to Find a Number?</div>
<div class="el a fx-up" data-s="0" style="--d:.4s;left:57.6px;top:268px;width:830px;font-size:29.33px;color:#3b5b7a">An introduction to binary search</div>
<div class="el a fx-up" data-s="0" style="--d:.7s;left:57.6px;top:372px;width:830px;font-size:21.33px;color:#5f6b7a">CS 495 Micro-Teaching</div>
<div class="el a fx-up" data-s="0" style="--d:.7s;left:57.6px;top:404px;width:830px;font-size:21.33px;color:#1f2933">Presented by PRESENTER</div>
</section>
```

Short variant: a 64px course name at `top:170px` and a 21.33px "Presented by …" at `top:290px`.

## 2. Framing question slide (hook)

A "so far" strip, two horizontal rules that grow, a 50px centred question, then an italic spoiler.

```html
<section class="slide" style="background:#fff" data-i="topic" data-steps="2">
<div class="ttl a fx-down" data-s="0">Today’s Topic</div>
<div class="el a fx-fade" data-s="0" style="left:48px;top:112px;width:140px;height:40px;display:flex;align-items:center;font-size:17px;color:#5f6b7a;font-style:italic">So far</div>
<div class="el sh a fx-up" data-s="0" style="--d:.1s;left:160px;top:112px;width:150px;height:40px;background:#eceef1;border-radius:4px"><div class="tx" style="inset:4px;justify-content:center;text-align:center"><p style="font-size:15px">read text</p></div></div>
<div class="el sh a fx-up" data-s="0" style="--d:.2s;left:330px;top:112px;width:150px;height:40px;background:#eceef1;border-radius:4px"><div class="tx" style="inset:4px;justify-content:center;text-align:center"><p style="font-size:15px">write text</p></div></div>
<div class="el sh a fx-up" data-s="0" style="--d:.3s;left:500px;top:112px;width:150px;height:40px;background:#eceef1;border-radius:4px"><div class="tx" style="inset:4px;justify-content:center;text-align:center"><p style="font-size:15px">call tools</p></div></div>
<div class="el sh a fx-growx" data-s="1" style="left:48px;top:196px;width:864px;height:2px;background:#3b5b7a"></div>
<div class="el sh a fx-up" data-s="1" style="--d:.15s;left:48px;top:216px;width:864px;height:150px"><div class="tx" style="inset:0;justify-content:center;text-align:center"><p style="font-size:50px;color:#3b5b7a;line-height:1.25">How do agents work with<br><b>2D images</b> and <b>3D scenes</b>?</p></div></div>
<div class="el sh a fx-growx" data-s="1" style="--d:.1s;left:48px;top:384px;width:864px;height:2px;background:#3b5b7a"></div>
<div class="el sh a fx-fade" data-s="2" style="left:48px;top:412px;width:864px;height:44px"><div class="tx" style="inset:0;justify-content:center;text-align:center"><p style="font-size:22px;color:#4f7d5c;font-style:italic">Spoiler: both come down to the same thing</p></div></div>
<div class="pnum">2</div>
</section>
```

## 3. Points with a left accent bar (flow mode)

```html
<div class="bd">
  <p class="h a fx-fade" data-s="0">Every turn, the same three steps</p>
  <ol class="steps a fx-up" data-s="1" style="margin-top:14px">
    <li><i>1</i><span>Guess the <b>middle</b> of what is left.</span></li>
    <li><i>2</i><span>Listen: higher or lower?</span></li>
    <li><i>3</i><span><b>Throw away the half</b> that cannot contain the answer.</span></li>
  </ol>
  <div class="call a fx-up" data-s="2" style="margin-top:26px">This strategy is called <b>binary search</b>.</div>
</div>
```

Takeaway rows (`.pts`) reveal all at once or one per click:

```html
<div class="pts">
  <div class="pt a fx-up" data-s="1"><b>Strategy</b>Guess the middle, throw away half, repeat.</div>
  <div class="pt a fx-up" data-s="2"><b>Requirement</b>The data must be sorted.</div>
</div>
```

## 4. Numbered rows, one per click (absolute mode, used for Discussion questions)

Each row = a `fx-growy` bar (6px wide) plus a `fx-left` text block delayed 0.1s. Rows are 54px tall, 66px apart starting at `top:108px`.

```html
<div class="el sh a fx-growy" data-s="1" style="left:48px;top:108px;width:6px;height:54px;background:#3b5b7a"></div>
<div class="el sh a fx-left" data-s="1" style="--d:.1s;left:68px;top:108px;width:844px;height:54px"><div class="tx" style="inset:0;justify-content:center"><p style="font-size:19px;line-height:1.35"><b style="color:#3b5b7a">1.</b>&nbsp;&nbsp;Should 3D agents keep looking through renders, or read meshes directly as tokens?</p></div></div>
<div class="el sh a fx-growy" data-s="2" style="left:48px;top:174px;width:6px;height:54px;background:#3b5b7a"></div>
<div class="el sh a fx-left" data-s="2" style="--d:.1s;left:68px;top:174px;width:844px;height:54px"><div class="tx" style="inset:0;justify-content:center"><p style="font-size:19px;line-height:1.35"><b style="color:#3b5b7a">2.</b>&nbsp;&nbsp;Second question…</p></div></div>
<!-- … -->
<div class="el sh a fx-fade" data-s="6" style="left:48px;top:446px;width:864px;height:40px"><div class="tx" style="inset:0;justify-content:center"><p style="font-size:24px;color:#3b5b7a">Thank you!</p></div></div>
```

## 5. Card grid

2×2 cards (420×152, gap 24, rows at top 104 and 270), one per click, then a full-width callout bar:

```html
<div class="el sh a fx-up" data-s="1" style="left:48px;top:104px;width:420px;height:152px;background:#eceef1;border-radius:3px"><div class="tx" style="inset:14px"><p style="font-size:19px;color:#3b5b7a;margin-bottom:8px">Card heading</p><p style="font-size:16px;line-height:1.4">Two or three sentences of body text.</p></div></div>
<div class="el sh a fx-up" data-s="2" style="left:492px;top:104px;width:420px;height:152px;background:#eceef1;border-radius:3px">…</div>
<div class="el sh a fx-up" data-s="3" style="left:48px;top:270px;width:420px;height:152px;background:#eceef1;border-radius:3px">…</div>
<div class="el sh a fx-up" data-s="4" style="left:492px;top:270px;width:420px;height:152px;background:#eceef1;border-radius:3px">…</div>
<div class="el sh a fx-up" data-s="5" style="left:48px;top:446px;width:864px;height:40px;background:#e1e8f0;border-radius:3px;border-left:4px solid #3b5b7a"><div class="tx" style="inset:10px;justify-content:center"><p style="font-size:16px;color:#3b5b7a">One-sentence conclusion across the four cards</p></div></div>
```

4 columns in one click with a cascade (204px wide at left 48/268/488/708), the featured one gets `background:#e1e8f0;border:1.5px solid #3b5b7a` and an italic 12.5px "this paper" label under it:

```html
<div class="el sh a fx-up" data-s="1" style="--d:0s;left:48px;top:106px;width:204px;height:132px;background:#eceef1;border-radius:3px"><div class="tx" style="inset:12px"><p style="font-size:17px;color:#3b5b7a;margin-bottom:6px">Family name</p><p style="font-size:14px;color:#5f6b7a;margin-bottom:8px">What it buys you</p><p style="font-size:14px">Examples</p></div></div>
<div class="el sh a fx-up" data-s="1" style="--d:.12s;left:268px;…">…</div>
<div class="el sh a fx-up" data-s="1" style="--d:.24s;left:488px;…;background:#e1e8f0;border:1.5px solid #3b5b7a">…</div>
<div class="el sh a fx-up" data-s="1" style="--d:.36s;left:708px;…">…</div>
<div class="el sh a fx-fade" data-s="1" style="--d:.5s;left:488px;top:242px;width:204px;height:18px"><div class="tx" style="inset:0;justify-content:center;text-align:center"><p style="font-size:12.5px;color:#3b5b7a;font-style:italic">this paper</p></div></div>
```

## 6. Two columns with a vertical rule (flow mode)

```html
<div class="bd two">
  <div class="stack"> …left column… </div>
  <div class="vr a fx-fade" data-s="3">
    <p class="h">Numbers still possible</p>
    <p class="sub">Worst case, starting from 100</p>
    …
  </div>
</div>
```

Set `style="grid-template-columns:430px 1fr"` on `.two` when one side is a fixed-width diagram.

## 7. Comparison table with a reveal

```html
<table class="cmp num a fx-up" data-s="0">
  <tr><td>How many numbers</td><td>Check one by one</td><td class="hl">Binary search</td></tr>
  <tr><td>1,000,000</td><td>1,000,000<small>≈ 11.6 days</small></td><td class="hl">20<small>20 seconds</small></td></tr>
  <tr><td>1,000,000,000</td><td>1,000,000,000<small>≈ 32 years</small></td>
      <td class="hl" style="position:relative;height:66px"><span data-o="1">?</span><span class="a fx-fade" data-s="1" style="position:absolute;right:12px;top:10px">30<small>30 seconds</small></span></td></tr>
</table>
```

## 8. Poll with the answer behind a click

```html
<div class="poll a fx-up" data-s="0">
  <div class="opt num"><span>A</span>1,000</div>
  <div class="opt num"><span>B</span>100</div>
  <div class="opt num"><span>C</span>50</div>
  <div class="opt num"><span>D</span>20<div class="hit a fx-fade" data-s="1">20</div></div>
</div>
```
with content CSS:
```css
.poll{display:grid;grid-template-columns:repeat(4,160px);gap:24px;justify-content:center;margin:34px 0 26px}
.opt{position:relative;height:96px;background:#eceef1;display:grid;place-items:center;font-size:40px}
.opt span{position:absolute;left:10px;top:6px;font-size:14px;color:#5f6b7a}
.opt .hit{position:absolute;inset:0;background:#3b5b7a;color:#fff;display:grid;place-items:center;font-size:40px}
```

## 9. Big number panel with count-up

```html
<div class="el sh a fx-pop" data-s="1" style="left:48px;top:110px;width:345px;height:307px;background:#eceef1"></div>
<div class="el sh a fx-pop" data-s="1" data-count="0" style="left:67px;top:130px;width:307px;height:88px"><div class="tx" style="inset:9.6px"><p style="font-size:53.33px;color:#4f7d5c">w = 512</p></div></div>
<div class="el sh a fx-pop" data-s="1" style="left:67px;top:226px;width:307px;height:172px"><div class="tx" style="inset:9.6px"><p style="font-size:21.33px">Explanation of the number in one sentence.</p></div></div>
```
`data-count` animates the first number found in the element's text (commas and decimals preserved).

## 10. Diagram boxes + SVG arrows

Boxes are `.el` blocks; arrows live in one overlay `<svg class="lines">` per slide, same coordinates. Give each arrow the same `data-s` as the box it points to.

```html
<div class="el sh a fx-up" data-s="1" style="left:150px;top:106px;width:160px;height:54px;background:#eceef1;border-radius:4px"><div class="tx" style="inset:6px;justify-content:center;text-align:center"><p style="font-size:15px">observation</p></div></div>
<div class="el sh a fx-up" data-s="1" style="--d:.1s;left:400px;top:106px;width:160px;height:54px;background:#eceef1;border-radius:4px">…</div>
<svg class="lines" viewBox="0 0 960 540">
  <defs>
    <marker id="m1" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="#5f6b7a"/></marker>
    <marker id="m1g" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="#4f7d5c"/></marker>
  </defs>
  <!-- straight arrow between two boxes -->
  <line class="a fx-fade" data-s="1" style="--d:.15s" x1="310" y1="133" x2="396" y2="133" stroke="#5f6b7a" stroke-width="1.3" marker-end="url(#m1)"/>
  <!-- feedback loop drawn as a stroke -->
  <path class="a fx-draw" data-s="2" style="--d:.5s" pathLength="1" d="M810,350 L810,378 L226,378 L226,356" fill="none" stroke="#4f7d5c" stroke-width="1.6" stroke-dasharray="1" marker-end="url(#m1g)"/>
  <text class="a fx-fade" data-s="2" style="--d:.8s" x="462" y="396" fill="#4f7d5c" font-size="13" font-family="'Times New Roman', Tinos, Times, serif" text-anchor="middle">act on the scene, render again</text>
</svg>
```

Marker ids must be unique per file: suffix them per slide (`m1`, `m2a`, …) if several slides define markers.

Small inline SVG diagrams (trees, grids) can also be placed inside a flow column with
`<svg viewBox="0 0 420 230" width="420" height="230">`, animating groups with `class="a fx-fade" data-s="1"`.

## 11. Swap a state with `data-o`

Show version A, then at click 2 fade A out and bring B in at the same position:

```html
<div class="el sh a fx-fade" data-s="1" data-o="2" style="left:560px;top:180px;width:352px;height:36px">…state A…</div>
<div class="el sh a fx-fade" data-s="2" style="left:560px;top:180px;width:352px;height:36px">…state B…</div>
```
Also used to remove a "?" placeholder (`<span data-o="1">?</span>`) when the real value appears.

## 12. Magic move across slides

Give the same `data-mm` key to the "same" object on two consecutive slides; on the page turn it glides between the two boxes. Works on position and size, not on text content.

```html
<!-- slide A -->
<div class="el sh a fx-fade" data-s="0" data-mm="tok0" style="left:48px;top:218px;width:70px;height:32px;background:#eceef1">…</div>
<!-- slide B -->
<div class="el sh a fx-fade" data-s="0" data-mm="tok0" style="left:120px;top:120px;width:70px;height:32px;background:#eceef1">…</div>
```

## 13. Image

```html
<img class="el a fx-fade" data-s="3" style="--d:.15s;left:564px;top:132px;width:288px;height:72px" src="data:image/png;base64,…" alt="attention heatmap from the paper">
```
Keep the aspect ratio of the source; a 3px radius panel behind it is optional. Caption with a 12.5px italic `#5f6b7a` label underneath.

## 14. Sources footnote

```html
<div class="src">Sources: DeepSeek-V3.2-Exp technical report; OpenAI gpt-oss model card; FSA (arXiv 2508.18224); InfLLM-v2 (ICLR 2026).</div>
```

## 15. "Your turn" exercise slide

Two `.box` columns, each a question with its answer behind a click:

```html
<div class="bd two" style="gap:0 28px;align-items:start">
  <div class="box a fx-up" data-s="0" style="display:flex;flex-direction:column;gap:12px">
    <p class="lab">Question 1</p>
    <p class="txt" style="flex:1">A dictionary has <b>1,000 pages</b> in alphabetical order. How many page checks, at most?</p>
    <div class="call a fx-up" data-s="1" style="background:#fff"><b>10.</b> 2<sup>10</sup> = 1,024, which is more than 1,000.</div>
  </div>
  <div class="box a fx-up" data-s="0" style="display:flex;flex-direction:column;gap:12px">…</div>
</div>
```

## 16. Interactive widget slide

```html
<section class="slide" style="background:#fff" data-i="demo" data-steps="0">
<div class="ttl a fx-down" data-s="0">Think of a Number from 1 to 100</div>
<button class="rst" type="button" data-reset="small">Restart</button>
<div class="bd"><div class="game" id="game-small"></div></div>
<div class="pnum">3</div>
</section>
```
Widget JS renders into `#game-small` with `innerHTML` and listens for clicks on its own root. Place it above the engine code in the `<script>`. Buttons must be `type="button"`. Style buttons as `font:19px 'Times New Roman',Tinos,serif;border:1px solid #3b5b7a;color:#3b5b7a;background:#fff`, primary = filled `#3b5b7a`.

## 17. Takeaways / closing slide

```html
<div class="ttl a fx-down" data-s="0">Takeaways</div>
<div class="bd">
  <div class="pts a fx-up" data-s="0">
    <div class="pt"><b>Strategy</b>Guess the middle, throw away half, repeat.</div>
    <div class="pt"><b>Requirement</b>The data must be sorted.</div>
    <div class="pt"><b>Speed</b>About log<sub>2</sub>(<i>N</i>) guesses.</div>
    <div class="pt"><b>Optimal</b>No strategy with yes/no answers can do better.</div>
  </div>
  <p class="sub a fx-up" data-s="1" style="margin-top:22px">Where you will see it: dictionary lookup, <i>git bisect</i>, database indexes.</p>
  <p class="a fx-up" data-s="1" style="margin-top:26px;font-size:32px;color:#3b5b7a">Thank you! Questions?</p>
</div>
```

## Notes example

```js
const NOTES = [
  "Hi everyone, I'm PRESENTER. Has anyone played the number-guessing game before? Today we'll find out how few questions we really need.",
  "Explain the rules: think of a number from 1 to 100, and you can only answer higher, lower or correct. ★ Ask two or three students what their first guess would be and why. Don't judge yet, just say: let's test it."
];
```
Slide 1 has `data-steps="0"` (no ★), slide 2 has `data-steps="1"` (one ★).

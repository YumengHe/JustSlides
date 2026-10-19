#!/usr/bin/env python3
"""Sanity-check a JustSlides deck. Usage: python3 check_deck.py deck.html

Checks the invariants the slide engine relies on:
  * one NOTES entry per <section class="slide">
  * data-steps on each slide == the largest data-s / data-o used inside it
  * the number of ★ in NOTES[i] == data-steps of slide i
  * the inline <script> parses (via `node --check`, if node is installed)
Exit code 1 if anything is wrong.
"""
import json, re, subprocess, shutil, sys, tempfile, os

def main(path):
    html = open(path, encoding='utf-8').read()
    errors, warnings = [], []

    # split into slides
    body_html = re.sub(r'<!--.*?-->', '', html, flags=re.S)          # ignore HTML comments
    parts = re.split(r'<section\s+class="slide"', body_html)[1:]
    slides = []
    for p in parts:
        body = p.split('</section>', 1)[0]
        m = re.search(r'data-steps="(\d+)"', p.split('>', 1)[0])
        steps = int(m.group(1)) if m else None
        ss = [int(x) for x in re.findall(r'data-s="(\d+)"', body)]
        os_ = [int(x) for x in re.findall(r'data-o="(\d+)"', body)]
        slides.append((steps, max(ss, default=0), max(os_, default=0), body))

    # NOTES array
    m = re.search(r'const NOTES\s*=\s*(\[.*?\]);', body_html, re.S)
    notes = None
    if not m:
        errors.append('no `const NOTES = [...]` found')
    else:
        try:
            notes = json.loads(m.group(1))
        except json.JSONDecodeError as e:
            errors.append(f'NOTES is not plain JSON-style strings ({e}); use double quotes, escape inner quotes as \\"')
    if notes is not None and len(notes) != len(slides):
        errors.append(f'{len(slides)} slides but {len(notes)} NOTES entries')

    for i, (steps, mx_s, mx_o, body) in enumerate(slides, 1):
        if steps is None:
            errors.append(f'slide {i}: missing data-steps'); continue
        need = max(mx_s, mx_o)
        if steps != need:
            errors.append(f'slide {i}: data-steps="{steps}" but elements use data-s/data-o up to {need}')
        if notes is not None and i - 1 < len(notes):
            stars = notes[i - 1].count('★')
            if stars != steps:
                errors.append(f'slide {i}: data-steps="{steps}" but NOTES[{i-1}] has {stars} ★')
        if i > 1 and 'class="pnum"' not in body:
            warnings.append(f'slide {i}: no <div class="pnum"> page number')
        if re.search(r'data-s="\d+"', body) and 'class="' not in body:
            warnings.append(f'slide {i}: elements with data-s should also carry class="a fx-..."')
        for tag in re.findall(r'<(?:div|p|span|img|svg|path|line|text|g)\b[^>]*data-s="\d+"[^>]*>', body):
            if ' a ' not in tag.replace('class="', 'class=" ').replace('"', ' " ') and 'class="a ' not in tag and ' a"' not in tag:
                warnings.append(f'slide {i}: element with data-s but without class "a": {tag[:90]}...')
                break

    # JS syntax
    if shutil.which('node'):
        for k, js in enumerate(re.findall(r'<script>(.*?)</script>', html, re.S)):
            with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
                f.write(js); tmp = f.name
            r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
            os.unlink(tmp)
            if r.returncode:
                errors.append(f'script #{k+1} has a syntax error:\n' + r.stderr.strip()[:600])
    else:
        warnings.append('node not installed, skipped JS syntax check')

    for w in warnings: print('warn:', w)
    for e in errors: print('ERROR:', e)
    print(f'{len(slides)} slides, {sum(s or 0 for s,_,_,_ in slides)} clicks total, '
          f'{"OK" if not errors else str(len(errors)) + " error(s)"}')
    return 1 if errors else 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))

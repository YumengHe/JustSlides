#!/usr/bin/env bash
# Screenshot every slide of a deck with all click steps revealed, using headless Chrome.
# Usage: scripts/screenshot.sh deck.html [outdir]   ->  outdir/slide-01.png ...
set -euo pipefail
deck="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
out="${2:-${TMPDIR:-/tmp}/justslides-shots}"; mkdir -p "$out"
for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "$(command -v google-chrome || true)" "$(command -v chromium || true)" "$(command -v chromium-browser || true)"; do
  [ -n "$c" ] && [ -x "$c" ] && CHROME="$c" && break
done
[ -n "${CHROME:-}" ] || { echo "no Chrome/Chromium found; open the deck in a browser instead" >&2; exit 1; }
n=$(grep -o '<section class="slide"' "$deck" | wc -l | tr -d ' ')
for i in $(seq 1 "$n"); do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,800 --virtual-time-budget=4000 \
    --screenshot="$out/slide-$(printf %02d "$i").png" "file://$deck?all#$i" >/dev/null 2>&1
done
echo "$n slides -> $out"

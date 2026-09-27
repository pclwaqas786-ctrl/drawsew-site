#!/bin/bash
# DrawSew post-images auto-sync: copies any new post-NN.jpg images into the
# website repo, resizes them, commits and pushes. Quiet when nothing new.
set -u
SRC="$HOME/workspace/your_files/drawsew/post-images"
DST="$HOME/workspace/drawsew-site/assets/posts"
SITE="$HOME/workspace/drawsew-site"
NEW=0
mkdir -p "$DST"
for f in "$SRC"/post-*.jpg; do
    [ -e "$f" ] || continue
    base=$(basename "$f")
    if [ ! -e "$DST/$base" ]; then
        cp "$f" "$DST/$base"
        NEW=1
    fi
done
if [ "$NEW" = "0" ]; then
    echo "no new post images"
    exit 0
fi
python3 - "$DST" << 'EOF'
import sys
from PIL import Image
from pathlib import Path
d = Path(sys.argv[1])
for f in sorted(d.glob("post-*.jpg")):
    img = Image.open(f)
    if max(img.size) > 800:
        img.thumbnail((800, 800))
        img.save(f, "JPEG", quality=72)
        print("resized", f.name)
EOF
cd "$SITE" && git add -A -q && git commit -qm "Auto-sync new post images" && git push -q && echo "synced and pushed"

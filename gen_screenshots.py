#!/usr/bin/env python3
"""Render PNG screenshots of each theme into screenshots/<bucket>/<name>.png.

Mirrors preview.py's panel content but draws with Pillow instead of ANSI
escapes. Output is what the README embeds.
"""
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from preview import (
    parse_palette, resolve, ANSI_NAMES, sample_rows, WIDTH, PAD,
)

FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
FONT_SIZE = 14
LINE_PAD = 4  # extra vertical pixels per line


def screenshot_rows(pal):
    """Banner + tagline + sample content + 16 ANSI swatches as a list of rows.
    Each row is either a list of segments (text, fg_key[, bg_key]) or 'DIVIDER'."""
    rows = []
    title = f'━━━ {pal["_name"]}  ·  {pal.get("_mode", "")} ━━━'
    rows.append([(title,)])
    if pal.get("_tagline"):
        rows.append([(pal["_tagline"], "dim")])
    rows.append([])
    rows.extend(sample_rows())
    rows.append([])
    for prefix in ("ANSI", "BR"):
        segs = []
        for n in ANSI_NAMES:
            if pal.get(f"{prefix}_{n.upper()}") is None:
                continue
            segs.append((f" {n:<8}", "auto", f"{prefix.lower()}:{n}"))
        rows.append(segs)
    rows.append([])
    return rows


def render_theme(path, font, char_w, char_h):
    pal = parse_palette(path)
    rows = screenshot_rows(pal)
    img_w = WIDTH * char_w
    img_h = len(rows) * char_h
    img = Image.new("RGB", (img_w, img_h), pal["BG"])
    draw = ImageDraw.Draw(img)
    BG = pal["BG"]
    pad_px = len(PAD) * char_w

    for i, row in enumerate(rows):
        y = i * char_h
        draw.rectangle([0, y, img_w, y + char_h], fill=BG)

        if row == "DIVIDER":
            inner = WIDTH - 2 * len(PAD)
            text = "─" * inner
            draw.text((pad_px, y + 2), text, font=font, fill=resolve(pal, "dim"))
            continue

        x = pad_px
        for seg in row:
            text = seg[0]
            fg_key = seg[1] if len(seg) > 1 else "fg"
            bg_key = seg[2] if len(seg) > 2 else None
            seg_bg = resolve(pal, bg_key) if bg_key else BG
            seg_fg = resolve(pal, fg_key, fallback_bg=seg_bg)
            text_w = len(text) * char_w
            if bg_key:
                draw.rectangle([x, y, x + text_w, y + char_h], fill=seg_bg)
            draw.text((x, y + 2), text, font=font, fill=seg_fg)
            x += text_w

    out = ROOT / "screenshots" / pal["_mode"] / f"{pal['_name']}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def main():
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE, index=0)
    char_w = math.ceil(font.getlength("M"))
    bbox = font.getbbox("Mg")
    char_h = (bbox[3] - bbox[1]) + LINE_PAD

    bucket_order = {"light": 0, "dim": 1, "dark": 2}
    files = sorted(
        (ROOT / "colors").glob("*/gen_*_theme.py"),
        key=lambda p: (bucket_order.get(p.parent.name, 99), p.name),
    )
    for f in files:
        out = render_theme(f, font, char_w, char_h)
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()

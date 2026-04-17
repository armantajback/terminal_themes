#!/usr/bin/env python3
"""Preview each theme by rendering Claude-Code-style sample content with 24-bit
ANSI truecolor escapes.

Reads RGB tuples directly from the generator scripts in ./colors/, so palettes
stay the single source of truth. Press Enter to advance, Ctrl-C to quit.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
COLORS_DIR = ROOT / "colors"

PALETTE_KEYS = [
    "BG", "FG", "BOLD", "CURSOR", "SELECTION",
    "ANSI_BLACK", "ANSI_RED", "ANSI_GREEN", "ANSI_YELLOW",
    "ANSI_BLUE", "ANSI_MAGENTA", "ANSI_CYAN", "ANSI_WHITE",
    "BR_BLACK", "BR_RED", "BR_GREEN", "BR_YELLOW",
    "BR_BLUE", "BR_MAGENTA", "BR_CYAN", "BR_WHITE",
]
ANSI_NAMES = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
WIDTH = 92
PAD = "  "
RESET = "\033[0m"


def parse_palette(path: Path) -> dict:
    text = path.read_text()
    pal: dict = {}
    for key in PALETTE_KEYS:
        m = re.search(rf"^{key}\s*=\s*color\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", text, re.M)
        if m:
            pal[key] = tuple(int(x) for x in m.groups())
    nm = re.search(r'"name"\s*:\s*"([^"]+)"', text)
    pal["_name"] = nm.group(1) if nm else path.stem
    pal["_mode"] = path.parent.name  # "light" or "dark", from the bucket folder
    # Tagline = the bit after " — " on the first line of the module docstring
    # (e.g. `"""Generate a 'Fiji' theme — teal lagoon over warm sand."""`).
    doc = re.search(r'"""([^\n"]+)', text)
    tagline = ""
    if doc:
        first = doc.group(1).strip().rstrip('"').rstrip(".")
        if " — " in first:
            tagline = first.split(" — ", 1)[1].strip()
    pal["_tagline"] = tagline
    return pal


def fg_esc(rgb): return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
def bg_esc(rgb): return f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m"


def readable_on(rgb):
    # WCAG-ish luminance pick: dark text on light bg, light on dark.
    r, g, b = rgb
    luma = 0.299 * r + 0.587 * g + 0.114 * b
    return (20, 20, 20) if luma > 140 else (245, 245, 245)


def lerp(a, b, t):
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))


def resolve(pal: dict, key: str, fallback_bg=None):
    if key == "fg":        return pal["FG"]
    if key == "bg":        return pal["BG"]
    if key == "bold":      return pal.get("BOLD", pal["FG"])
    if key == "cursor":    return pal.get("CURSOR", pal["FG"])
    if key == "selection": return pal.get("SELECTION", pal["BG"])
    if key == "dim":       return lerp(pal["FG"], pal["BG"], 0.55)
    if key == "auto":      return readable_on(fallback_bg if fallback_bg else pal["BG"])
    if key.startswith("ansi:"):
        return pal[f"ANSI_{key[5:].upper()}"]
    if key.startswith("br:"):
        return pal[f"BR_{key[3:].upper()}"]
    raise ValueError(f"unknown color key: {key}")


def render_row(pal: dict, segments) -> str:
    """segments: list of (text, fg_key) or (text, fg_key, bg_key)."""
    BG = pal["BG"]
    visible = len(PAD) + sum(len(s[0]) for s in segments)
    out = bg_esc(BG) + fg_esc(pal["FG"]) + PAD
    for seg in segments:
        text = seg[0]
        fg_key = seg[1] if len(seg) > 1 else "fg"
        bg_key = seg[2] if len(seg) > 2 else None
        seg_bg_rgb = resolve(pal, bg_key) if bg_key else BG
        seg_fg_rgb = resolve(pal, fg_key, fallback_bg=seg_bg_rgb)
        out += bg_esc(seg_bg_rgb) + fg_esc(seg_fg_rgb) + text
        if bg_key:
            out += bg_esc(BG)  # reset back to line bg
    out += " " * max(0, WIDTH - visible) + RESET
    return out


def divider(pal: dict) -> str:
    BG = pal["BG"]
    line = "─" * (WIDTH - len(PAD) * 2)
    return f"{bg_esc(BG)}{fg_esc(resolve(pal, 'dim'))}{PAD}{line}{PAD}{RESET}"


def banner(pal: dict, title: str) -> str:
    BG, FG = pal["BG"], pal["FG"]
    text = f"━━━ {title} ━━━"
    pad_right = " " * max(0, WIDTH - len(PAD) - len(text))
    return f"{bg_esc(BG)}{fg_esc(FG)}{PAD}{text}{pad_right}{RESET}"


# Each entry is a list of segments, the literal "DIVIDER", or [] for blank line.
def sample_rows():
    return [
        [("● ", "ansi:green"), ("Setting up the theme generator pipeline:",)],
        [],
        [("● ", "ansi:green"), ("Write", "ansi:yellow"),
         ("(colors/gen_aurora_theme.py)",)],
        [("  └ ", "dim"), ("Wrote ",), ("87", "ansi:yellow"),
         (" lines to ",), ("colors/gen_aurora_theme.py", "bold")],
        [("        1  ", "dim"), ("#!/usr/bin/env python3", "dim")],
        [("        2  ", "dim"),
         ('"""Generate the Aurora theme — borealis greens over polar night."""', "dim")],
        [("        3  ", "dim"), ("from ", "ansi:magenta"),
         ("pathlib ", "dim"), ("import ", "ansi:magenta"), ("Path", "dim")],
        [("        4  ", "dim"), ("from ", "ansi:magenta"),
         ("AppKit ", "dim"), ("import ", "ansi:magenta"), ("NSColor", "dim")],
        [("        5  ", "dim")],
        [("        6  ", "dim"), ("BG ", "dim"), ("= ", "dim"),
         ("color", "ansi:blue"), ("(", "dim"),
         ("12", "ansi:yellow"), (", ", "dim"),
         ("18", "ansi:yellow"), (", ", "dim"),
         ("28", "ansi:yellow"), (")  ", "dim"),
         ("# polar night", "ansi:cyan")],
        [("        7  ", "dim"), ("FG ", "dim"), ("= ", "dim"),
         ("color", "ansi:blue"), ("(", "dim"),
         ("164", "ansi:yellow"), (", ", "dim"),
         ("212", "ansi:yellow"), (", ", "dim"),
         ("180", "ansi:yellow"), (")  ", "dim"),
         ("# borealis green", "ansi:cyan")],
        [("    … +80 lines (ctrl+o to expand)", "dim")],
        [],
        [("● ", "ansi:green"),
         ("Run the regenerated theme through the previewer to confirm the palette.",)],
        [],
        [("✻ ", "br:red"), ("Rebuilding theme assets…",),
         (" (2m 14s · ↓ 8.3k tokens · thinking)", "dim")],
        [("  └ ", "dim"), ("✓ ", "ansi:green"),
         ("Parse RGB tuples from each gen_*_theme.py",)],
        [("    ",), ("✓ ", "ansi:green"),
         ("Render sample text with truecolor escapes",)],
        [("    ",), ("▣ ", "ansi:yellow"),
         ("Repoint generators at ", "ansi:yellow"),
         ("themes/", "bold"),
         (" instead of ~/Desktop", "ansi:yellow")],
        [("    ",), ("☐ ", "dim"),
         ("Add a 24-step color gradient strip", "dim")],
        [("    ",), ("☐ ", "dim"),
         ("Wire up keyboard shortcuts for forward/back navigation", "dim")],
        [("    ",), ("☐ ", "dim"),
         ("Write installer that drops profiles into Terminal.app", "dim")],
        [],
        "DIVIDER",
        [(">  ",), (" ", "auto", "cursor"), (" try a prompt…", "dim")],
        "DIVIDER",
        [("▸▸ ", "ansi:cyan"), ("auto mode on",), ("  ·  ", "dim"),
         (" ◇ preview needs your input ", "auto", "br:cyan"),
         ("  ·  ", "dim"), ("↓ to view", "dim"),
         ("  ·  ", "dim"), ("esc to interrupt", "dim"),
         ("  ·  ", "dim"), ("ctrl+t to hide t…", "dim")],
    ]


def swatch_segments(pal: dict):
    """Swatch rows as list-of-segment-lists, shared between preview and screenshots.
    Two ANSI rows (normal + bright) plus a third row for cursor / selection / bold."""
    rows = []
    for prefix in ("ANSI", "BR"):
        segs = []
        for n in ANSI_NAMES:
            if pal.get(f"{prefix}_{n.upper()}") is None:
                continue
            segs.append((f" {n:<8}", "auto", f"{prefix.lower()}:{n}"))
        rows.append(segs)
    extras = []
    if pal.get("CURSOR"):
        extras.append((f" {'cursor':<9}", "auto", "cursor"))
    if pal.get("SELECTION"):
        extras.append((f" {'selection':<9}", "auto", "selection"))
    if pal.get("BOLD"):
        extras.append((f" {'bold':<9}", "bold"))
    rows.append(extras)
    return rows


def render(pal: dict) -> None:
    print()
    title = f'{pal["_name"]}  ·  {pal.get("_mode", "")}'.rstrip(" ·")
    print(banner(pal, title))
    if pal.get("_tagline"):
        print(render_row(pal, [(pal["_tagline"], "dim")]))
    print(render_row(pal, []))
    for row in sample_rows():
        if row == "DIVIDER":
            print(divider(pal))
        else:
            print(render_row(pal, row))
    print(render_row(pal, []))
    for row in swatch_segments(pal):
        print(render_row(pal, row))
    print(render_row(pal, []))
    print()


def main() -> None:
    # Find generators one level deep (colors/<mode>/gen_*_theme.py).
    # Sort: light → dim → dark, alphabetic within each bucket.
    bucket_order = {"light": 0, "dim": 1, "dark": 2}
    files = sorted(
        COLORS_DIR.glob("*/gen_*_theme.py"),
        key=lambda p: (bucket_order.get(p.parent.name, 99), p.name),
    )
    if not files:
        sys.exit(f"No generators found in {COLORS_DIR}")
    palettes = [parse_palette(f) for f in files]
    for i, pal in enumerate(palettes):
        render(pal)
        if i < len(palettes) - 1:
            try:
                input("Press Enter for next theme (Ctrl-C to quit)... ")
            except (KeyboardInterrupt, EOFError):
                print()
                return


if __name__ == "__main__":
    main()

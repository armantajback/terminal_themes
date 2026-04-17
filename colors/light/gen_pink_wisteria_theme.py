#!/usr/bin/env python3
"""Generate a 'Pink Wisteria' macOS Terminal theme — cascading blossoms in dappled sun.

Light-mode palette inspired by a wisteria pergola at peak bloom: petal-tinted
cream background, deep stem-plum text, and accents drawn from the racemes
themselves (rose, blush, deep wisteria) plus the sunlit chartreuse leaves and
brown trellis branches that frame them.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Pink Wisteria — dappled-sun pergola at peak bloom.
# Background: petal-tinted cream, slightly warmer than pure paper.
# Foreground: deep wisteria-stem plum-brown, readable on the cream.
BG            = color(251, 241, 240)   # petal cream
FG            = color(107, 68,  88)    # wisteria stem
BOLD          = color(74,  44,  63)    # deep stem
CURSOR        = color(227, 123, 160)   # wisteria pink
SELECTION     = color(244, 216, 224)   # petal blush

# ANSI — racemes, leaves, branch, dappled sky
ANSI_BLACK    = color(58,  42,  56)    # branch shadow
ANSI_RED      = color(216, 86,  115)   # rose blossom
ANSI_GREEN    = color(155, 184, 90)    # sunlit chartreuse leaf
ANSI_YELLOW   = color(232, 184, 86)    # dappled sun on wood
ANSI_BLUE     = color(138, 168, 198)   # sky between branches
ANSI_MAGENTA  = color(198, 114, 164)   # deep wisteria bloom
ANSI_CYAN     = color(127, 184, 176)   # leaf-shadow sage
ANSI_WHITE    = color(245, 227, 221)   # pale petal wash

BR_BLACK      = color(122, 88,  112)   # dusky lavender stem
BR_RED        = color(240, 133, 160)   # bright pink petal
BR_GREEN      = color(196, 220, 130)   # fresh new leaf
BR_YELLOW     = color(244, 208, 130)   # sun-warmed gold
BR_BLUE       = color(176, 200, 224)   # pale spring sky
BR_MAGENTA    = color(232, 154, 196)   # light wisteria
BR_CYAN       = color(168, 212, 204)   # soft mint leaf
BR_WHITE      = color(255, 248, 244)   # cloud cream

theme = {
    "name": "Pink Wisteria",
    "type": "Window Settings",
    "ProfileCurrentVersion": 2.07,
    "BackgroundColor": BG,
    "TextColor": FG,
    "TextBoldColor": BOLD,
    "CursorColor": CURSOR,
    "SelectionColor": SELECTION,
    "ANSIBlackColor":         ANSI_BLACK,
    "ANSIRedColor":           ANSI_RED,
    "ANSIGreenColor":         ANSI_GREEN,
    "ANSIYellowColor":        ANSI_YELLOW,
    "ANSIBlueColor":          ANSI_BLUE,
    "ANSIMagentaColor":       ANSI_MAGENTA,
    "ANSICyanColor":          ANSI_CYAN,
    "ANSIWhiteColor":         ANSI_WHITE,
    "ANSIBrightBlackColor":   BR_BLACK,
    "ANSIBrightRedColor":     BR_RED,
    "ANSIBrightGreenColor":   BR_GREEN,
    "ANSIBrightYellowColor":  BR_YELLOW,
    "ANSIBrightBlueColor":    BR_BLUE,
    "ANSIBrightMagentaColor": BR_MAGENTA,
    "ANSIBrightCyanColor":    BR_CYAN,
    "ANSIBrightWhiteColor":   BR_WHITE,
    "columnCount": 110,
    "rowCount": 32,
    "useOptionAsMetaKey": True,
    "ShowWindowSettingsNameInTitle": False,
    "ShowActiveProcessInTitle": True,
    "ShowShellCommandInTitle": True,
}

script = Path(__file__).resolve()
out = script.parents[2] / "themes" / script.parent.name / "Pink Wisteria.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")

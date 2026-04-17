#!/usr/bin/env python3
"""Generate a 'Terracotta Tile' macOS Terminal theme — sun-warmed clay in a Mediterranean alley.

Mid-tone (dim) palette, warm-red end of the dim range: clay-rust background
the color of a sunlit roof tile, limewash-cream text, with bougainvillea,
saffron, herb pot, copper patina, and Mediterranean-sky accents — same shaded
courtyard energy as Olive Grove Noon but pulled toward the warm rust side.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Terracotta Tile — sun-warmed clay roof in a Mediterranean alley.
BG            = color(139, 99,  87)    # warm clay
FG            = color(240, 224, 204)   # limewash plaster
BOLD          = color(248, 236, 220)   # bright limewash
CURSOR        = color(244, 176, 112)   # sun gold
SELECTION     = color(92,  58,  48)    # shadow under tile

# ANSI — alley palette: clay, plaster, herb pots, sky between buildings
ANSI_BLACK    = color(63,  40,  32)    # deep terra shadow
ANSI_RED      = color(216, 96,  76)    # bright clay
ANSI_GREEN    = color(144, 168, 100)   # herb pot
ANSI_YELLOW   = color(232, 184, 96)    # saffron / lemon
ANSI_BLUE     = color(116, 148, 180)   # Mediterranean sky
ANSI_MAGENTA  = color(192, 120, 160)   # bougainvillea
ANSI_CYAN     = color(128, 176, 168)   # copper patina
ANSI_WHITE    = color(240, 224, 204)   # limewash

BR_BLACK      = color(156, 112, 104)   # pale clay
BR_RED        = color(240, 128, 112)   # bright terra
BR_GREEN      = color(184, 200, 128)   # bright herb
BR_YELLOW     = color(244, 208, 128)   # sunbright saffron
BR_BLUE       = color(160, 184, 208)   # pale sky
BR_MAGENTA    = color(224, 152, 192)   # bright bougainvillea
BR_CYAN       = color(168, 200, 192)   # pale patina
BR_WHITE      = color(248, 236, 220)   # bright limewash

theme = {
    "name": "Terracotta Tile",
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
out = script.parents[2] / "themes" / script.parent.name / "Terracotta Tile.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")

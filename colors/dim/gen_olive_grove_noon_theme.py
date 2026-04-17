#!/usr/bin/env python3
"""Generate an 'Olive Grove Noon' macOS Terminal theme — silvery sage in Mediterranean midday.

Mid-tone (dim) palette: warm olive-stone shadow background, limewashed-cream
text, with accents from a Mediterranean grove at noon — silvery olive leaves,
terracotta tile, saffron, sea-between-cliffs, wild thyme bloom, and sage. Same
shaded-courtyard feel of looking up from a sunlit alley into the grove beyond.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Olive Grove Noon — dusty olive shadow under a sun-baked sky.
BG            = color(116, 114, 94)    # warm olive-taupe
FG            = color(237, 227, 204)   # limewashed cream
BOLD          = color(248, 240, 220)   # bright limewash
CURSOR        = color(212, 144, 96)    # terracotta jar
SELECTION     = color(74,  72,  56)    # deep olive shadow

# ANSI — Mediterranean grove at noon
ANSI_BLACK    = color(74,  72,  56)    # deep olive shadow
ANSI_RED      = color(200, 112, 96)    # terracotta tile
ANSI_GREEN    = color(156, 176, 112)   # silvery olive leaf
ANSI_YELLOW   = color(216, 176, 96)    # saffron
ANSI_BLUE     = color(120, 156, 180)   # sea between cliffs
ANSI_MAGENTA  = color(176, 128, 160)   # wild thyme bloom
ANSI_CYAN     = color(136, 176, 152)   # sage
ANSI_WHITE    = color(237, 227, 204)   # limewashed wall

BR_BLACK      = color(128, 126, 104)   # pale olive ash
BR_RED        = color(224, 144, 124)   # warm tile
BR_GREEN      = color(188, 208, 136)   # bright leaf
BR_YELLOW     = color(240, 208, 128)   # bright saffron
BR_BLUE       = color(160, 188, 212)   # bright sea
BR_MAGENTA    = color(208, 160, 188)   # wild herb in bloom
BR_CYAN       = color(172, 202, 180)   # bright sage
BR_WHITE      = color(248, 240, 220)   # bright limewash

theme = {
    "name": "Olive Grove Noon",
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
out = script.parents[2] / "themes" / script.parent.name / "Olive Grove Noon.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")

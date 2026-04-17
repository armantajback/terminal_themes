#!/usr/bin/env python3
"""Generate a 'Velvet Garden' macOS Terminal theme — English walled garden at dusk, lantern-lit.

Dark counterpart to Cottage Floral: deep ivy-twilight green for the background,
warm beeswax-candle cream for text, with garden rose, foxglove, delphinium,
and hydrangea accents — the same palette story softened and saturated for
after-hours reading by lantern.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Velvet Garden — walled English garden at dusk, lanterns just lit.
BG            = color(20,  28,  24)    # ivy at twilight
FG            = color(228, 218, 192)   # candlelight cream
BOLD          = color(244, 234, 210)   # bright wax
CURSOR        = color(232, 110, 130)   # garden rose
SELECTION     = color(46,  60,  50)    # moss shadow

# ANSI — the bed at dusk, viewed by lantern
ANSI_BLACK    = color(34,  42,  36)    # yew shadow
ANSI_RED      = color(216, 84,  100)   # garden rose
ANSI_GREEN    = color(132, 184, 124)   # boxwood at dusk
ANSI_YELLOW   = color(232, 188, 92)    # lantern glow
ANSI_BLUE     = color(116, 156, 200)   # delphinium dusk
ANSI_MAGENTA  = color(180, 116, 192)   # foxglove
ANSI_CYAN     = color(120, 184, 184)   # hydrangea twilight
ANSI_WHITE    = color(228, 218, 192)   # magnolia by candlelight

BR_BLACK      = color(96,  110, 100)   # moss stone
BR_RED        = color(248, 138, 152)   # old rose
BR_GREEN      = color(176, 220, 158)   # fresh ivy
BR_YELLOW     = color(248, 218, 132)   # beeswax candle
BR_BLUE       = color(170, 200, 232)   # pale delphinium
BR_MAGENTA    = color(220, 162, 224)   # wisteria moonlit
BR_CYAN       = color(168, 220, 218)   # pale hydrangea
BR_WHITE      = color(252, 244, 220)   # moon-magnolia

theme = {
    "name": "Velvet Garden",
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
out = script.parents[2] / "themes" / script.parent.name / "Velvet Garden.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")

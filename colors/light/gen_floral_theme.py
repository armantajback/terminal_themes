#!/usr/bin/env python3
"""Generate a 'Cottage Floral' macOS Terminal theme — English garden blooms over magnolia cream."""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Cottage / English garden floral palette
# Background: magnolia petal cream with the faintest blush
BG            = color(252, 244, 234)   # magnolia
# Foreground: deep botanical stem green for readability
FG            = color(58,  92,  58)    # stem green
BOLD          = color(36,  66,  40)    # deep ivy
CURSOR        = color(214, 80,  118)   # garden rose
SELECTION     = color(244, 215, 224)   # rose petal

# ANSI — flowers of the cottage garden
ANSI_BLACK    = color(64,  48,  56)    # rich loam
ANSI_RED      = color(196, 64,  92)    # camellia
ANSI_GREEN    = color(86,  138, 78)    # leaf
ANSI_YELLOW   = color(232, 180, 64)    # daffodil
ANSI_BLUE     = color(98,  138, 200)   # forget-me-not
ANSI_MAGENTA  = color(180, 96,  168)   # foxglove
ANSI_CYAN     = color(132, 184, 192)   # hydrangea
ANSI_WHITE    = color(248, 234, 224)   # alyssum

BR_BLACK      = color(124, 102, 110)   # dusk lavender stem
BR_RED        = color(232, 116, 140)   # peony
BR_GREEN      = color(146, 188, 124)   # spring shoot
BR_YELLOW     = color(248, 214, 128)   # buttercup
BR_BLUE       = color(150, 184, 228)   # delphinium
BR_MAGENTA    = color(220, 148, 208)   # sweet pea
BR_CYAN       = color(180, 220, 224)   # bluebell mist
BR_WHITE      = color(255, 250, 244)   # jasmine

theme = {
    "name": "Cottage Floral",
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
out = script.parents[2] / "themes" / script.parent.name / "Cottage Floral.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")

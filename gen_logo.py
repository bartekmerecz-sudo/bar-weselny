#!/usr/bin/env python3
"""Generator identyfikacji wizualnej marki BURSZTYN — mobile bar."""
import os
import cairosvg
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"
OUT = "/home/claude/bursztyn/logo"
os.makedirs(OUT, exist_ok=True)

# ---------- paleta ----------
GRAFIT = "#1A1613"
ZLOTO = "#D9A441"
BURSZTYN = "#C8891F"
KREM = "#E8DCC8"
KREM_TLO = "#F2EBDD"
ZLOTO_CIEMNE = "#8A6A20"

# ---------- typografia ----------
_cache = {}


def load(name):
    if name not in _cache:
        f = TTFont(f"{FONTS}/{name}.ttf", lazy=True)
        _cache[name] = (f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm)
    return _cache[name]


def text_group(text, fontname, size, x, y, fill, tracking=0.0):
    """Zamienia tekst na krzywe. tracking w jednostkach px."""
    font, gs, cmap, upem = load(fontname)
    s = size / upem
    cursor = 0.0
    parts = []
    for ch in text:
        gname = cmap.get(ord(ch))
        if gname is None:
            cursor += upem * 0.3
            continue
        glyph = gs[gname]
        pen = SVGPathPen(gs)
        glyph.draw(pen)
        d = pen.getCommands()
        if d.strip():
            parts.append(f'<path d="{d}" transform="translate({cursor:.2f},0)"/>')
        cursor += glyph.width + (tracking / s)
    width = (cursor - (tracking / s if text else 0)) * s
    body = "".join(parts)
    g = (
        f'<g fill="{fill}" transform="translate({x:.2f},{y:.2f}) '
        f'scale({s:.6f},{-s:.6f})">{body}</g>'
    )
    return g, width


def text_width(text, fontname, size, tracking=0.0):
    return text_group(text, fontname, size, 0, 0, "#000", tracking)[1]


# ---------- znak: kieliszek z bursztynem ----------
def mark(cx, cy, s, stroke, amber=None, sw=2.2):
    """cx,cy = wierzcholek czaszy. s = skala."""
    P = lambda dx, dy: f"{cx + dx * s:.2f} {cy + dy * s:.2f}"
    d = (
        f"M {P(0,0)} L {P(-32,-38)} L {P(32,-38)} L {P(0,0)} "
        f"L {P(0,28)} M {P(-22,28)} L {P(22,28)}"
    )
    out = ""
    if amber:
        out += (
            f'<polygon points="{P(-17.5,-22).replace(" ", ",")} '
            f'{P(17.5,-22).replace(" ", ",")} {P(0,0).replace(" ", ",")}" '
            f'fill="{amber}"/>'
        )
    else:
        # w wersji jednokolorowej poziom plynu jako kreska
        out += (
            f'<line x1="{cx-17.5*s:.2f}" y1="{cy-22*s:.2f}" '
            f'x2="{cx+17.5*s:.2f}" y2="{cy-22*s:.2f}" stroke="{stroke}" '
            f'stroke-width="{sw*s:.2f}" stroke-linecap="round"/>'
        )
    out += (
        f'<path d="{d}" fill="none" stroke="{stroke}" '
        f'stroke-width="{sw*s:.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    return out


def mark_bbox(s):
    """(szerokosc, wysokosc, offset wierzcholka od gory)"""
    return 64 * s, 66 * s, 38 * s


# ---------- kompozycje ----------
SERIF = "CrimsonPro-Regular"
ITAL = "CrimsonPro-Italic"

WORD = "BURSZTYN"
TAG = "mobile bar · Łódź"
TAG_KROTKI = "mobile bar"


def lockup_poziomy(bg, stroke, amber, word_fill, tag_fill, rule_fill, tag=TAG):
    ms = 1.75
    mw, mh, apex_off = mark_bbox(ms)
    pad = 60
    gap = 56
    word_size, word_track = 50, 12.5
    tag_size, tag_track = 20, 2.5

    ww = text_width(WORD, SERIF, word_size, word_track)
    tw = text_width(tag, ITAL, tag_size, tag_track)
    text_w = max(ww, tw, 210)

    W = pad + mw + gap + text_w + pad
    H = pad + mh + pad
    cy = pad + apex_off
    cx = pad + mw / 2
    tx = pad + mw + gap

    baseline_word = pad + 46
    rule_y = baseline_word + 17
    baseline_tag = rule_y + 30

    el = []
    if bg:
        el.append(f'<rect width="{W:.0f}" height="{H:.0f}" fill="{bg}"/>')
    el.append(mark(cx, cy, ms, stroke, amber))
    el.append(text_group(WORD, SERIF, word_size, tx, baseline_word, word_fill, word_track)[0])
    el.append(
        f'<rect x="{tx:.2f}" y="{rule_y:.2f}" width="{max(ww,210)*0.62:.2f}" '
        f'height="1.4" fill="{rule_fill}"/>'
    )
    el.append(text_group(tag, ITAL, tag_size, tx, baseline_tag, tag_fill, tag_track)[0])
    return svg(W, H, el)


def lockup_pionowy(bg, stroke, amber, word_fill, tag_fill, rule_fill):
    ms = 2.0
    mw, mh, apex_off = mark_bbox(ms)
    pad = 60
    word_size, word_track = 34, 9
    tag_size, tag_track = 15, 2

    ww = text_width(WORD, SERIF, word_size, word_track)
    tw = text_width(TAG_KROTKI, ITAL, tag_size, tag_track)
    W = max(mw, ww, tw) + pad * 2
    H = pad + mh + 54 + 34 + 30 + pad

    cx = W / 2
    cy = pad + apex_off
    y_word = pad + mh + 54
    y_rule = y_word + 15
    y_tag = y_rule + 26

    el = []
    if bg:
        el.append(f'<rect width="{W:.0f}" height="{H:.0f}" fill="{bg}"/>')
    el.append(mark(cx, cy, ms, stroke, amber))
    el.append(text_group(WORD, SERIF, word_size, cx - ww / 2, y_word, word_fill, word_track)[0])
    el.append(
        f'<rect x="{cx-ww*0.30:.2f}" y="{y_rule:.2f}" width="{ww*0.60:.2f}" '
        f'height="1.2" fill="{rule_fill}"/>'
    )
    el.append(text_group(TAG_KROTKI, ITAL, tag_size, cx - tw / 2, y_tag, tag_fill, tag_track)[0])
    return svg(W, H, el)


def sygnet(bg, stroke, amber, ring):
    S = 400
    r = 150
    ms = 2.6
    _, mh, apex_off = mark_bbox(ms)
    cx = S / 2
    cy = S / 2 - mh / 2 + apex_off
    el = []
    if bg:
        el.append(f'<rect width="{S}" height="{S}" fill="{bg}"/>')
    el.append(
        f'<circle cx="{cx}" cy="{S/2}" r="{r}" fill="none" '
        f'stroke="{ring}" stroke-width="2.6"/>'
    )
    el.append(mark(cx, cy, ms, stroke, amber))
    return svg(S, S, el)


def znak_solo(stroke, amber, sw=2.2):
    ms = 4.0
    mw, mh, apex_off = mark_bbox(ms)
    pad = 40
    W, H = mw + pad * 2, mh + pad * 2
    el = [mark(W / 2, pad + apex_off, ms, stroke, amber, sw)]
    return svg(W, H, el)


def svg(w, h, elements):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h:.0f}" '
        f'viewBox="0 0 {w:.0f} {h:.0f}">' + "".join(elements) + "</svg>"
    )


# ---------- zapis ----------
def save(name, content, png_width=2400):
    p = f"{OUT}/{name}.svg"
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    cairosvg.svg2png(
        bytestring=content.encode("utf-8"),
        write_to=f"{OUT}/{name}.png",
        output_width=png_width,
    )
    return p


files = [
    ("bursztyn-poziom-ciemne", lockup_poziomy(GRAFIT, ZLOTO, BURSZTYN, KREM, BURSZTYN, BURSZTYN), 2400),
    ("bursztyn-poziom-jasne", lockup_poziomy(KREM_TLO, GRAFIT, BURSZTYN, GRAFIT, ZLOTO_CIEMNE, BURSZTYN), 2400),
    ("bursztyn-poziom-przezroczyste", lockup_poziomy(None, ZLOTO, BURSZTYN, KREM, BURSZTYN, BURSZTYN), 2400),
    ("bursztyn-pion-ciemne", lockup_pionowy(GRAFIT, ZLOTO, BURSZTYN, KREM, BURSZTYN, BURSZTYN), 1600),
    ("bursztyn-pion-jasne", lockup_pionowy(KREM_TLO, GRAFIT, BURSZTYN, GRAFIT, ZLOTO_CIEMNE, BURSZTYN), 1600),
    ("bursztyn-sygnet-ciemne", sygnet(GRAFIT, ZLOTO, BURSZTYN, ZLOTO), 1200),
    ("bursztyn-sygnet-jasne", sygnet(KREM_TLO, GRAFIT, BURSZTYN, ZLOTO_CIEMNE), 1200),
    ("bursztyn-znak-zloty", znak_solo(ZLOTO, BURSZTYN), 1200),
    ("bursztyn-mono-czarny", znak_solo(GRAFIT, None, 2.6), 1200),
    ("bursztyn-mono-kremowy", znak_solo(KREM, None, 2.6), 1200),
]

for name, content, w in files:
    save(name, content, w)
    print(f"  {name}.svg + .png")

print(f"\nGotowe: {len(files)} wersji × 2 formaty = {len(files)*2} plikow")

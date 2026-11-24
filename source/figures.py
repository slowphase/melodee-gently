"""Melodee, Gently: vector figures (prototype).

Panel geometry is ported from Shrub, Gently's figures.py (same FM-1 hardware),
recoloured for the dark purple theme.
"""
import math

# palette (mirrors :root in style.css)
BG = "#14111C"
PANEL = "#1F1A2B"
INK = "#E8E4F0"
MUTED = "#A79FB8"
AMETHYST = "#A78BFA"
VIOLET = "#C084FC"
ORCHID = "#E879F9"
AMBER = "#F5B971"
RULE = "#3A3150"
ENGINE = {"PROPHET": "#6D5BD0", "FM6": "#A78BFA", "CZ-1": "#C4B5FD", "SID": "#D946EF", "DRUM": "#9D4EDD"}

SANS = "Jost"


def t(x, y, s, size=11, fill=INK, weight=500, anchor="middle", ls=0, family=SANS, style=""):
    lsp = f' letter-spacing="{ls}"' if ls else ""
    st = f' font-style="{style}"' if style else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}" font-family="{family}"{lsp}{st}>{s}</text>')


# ---------------------------------------------------------------------------
# FM-1 front panel (geometry from Shrub, Gently)
# ---------------------------------------------------------------------------
OX, OY = 14, 14
KNOBS_L = {"MASTER": (44, 55), "SELECT": (106, 55), "PRESETS": (44, 127), "ALGORITHM": (106, 127)}
KNOBS_R = {"KNOB 1": (416, 49), "KNOB 2": (457, 49), "KNOB 3": (498, 49), "KNOB 4": (539, 49)}
BUTTONS = [["FX", "SCL", "ENV", "LFO", "EDIT", "GLO"], ["HOME", "SAVE", "ARP", "SEQ", "PLAY", "REC"]]
WHITE_N = 16
BLACK_AFTER = [0, 1, 2, 4, 5, 7, 8, 9, 11, 12, 14]


def _white_x(i):
    return 35 + 32.8 * i


def fm1_panel(hl=(), keys_hl=False, nums=None, screen=None):
    """hl: control names to light. nums: {control: step number} badges."""
    hl = set(hl)
    nums = nums or {}
    dimop = .32
    o = []
    W, H = 592, 384
    o.append(f'<rect x="{OX}" y="{OY}" width="564" height="355" rx="16" fill="#241E33" stroke="{RULE}" stroke-width="2"/>')

    def badge(name, x, y):
        if name not in nums:
            return ""
        big = len(nums[name]) > 1
        return (f'<circle cx="{x}" cy="{y}" r="{8.2 if big else 7.2}" fill="{ORCHID}" stroke="{BG}" stroke-width="1.4"/>' +
                t(x, y + 3.2, nums[name], 8.4 if big else 9.4, BG, 700))

    def knob(name, cx, cy, r):
        lit = name in hl
        op = 1 if lit else dimop
        cx, cy = cx + OX, cy + OY
        s = [f'<g opacity="{op}">']
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="{VIOLET if lit else "#5B5170"}" stroke-width="{2.6 if lit else 1.2}"/>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{"#4A3A6E" if lit else "#3A3348"}"/>')
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r + 3}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
        s.append(t(cx, cy - r - 9, name, 8.4 if len(name) < 9 else 7.6, VIOLET if lit else MUTED, 600, ls=.4))
        s.append("</g>")
        s.append(badge(name, cx, cy + r + 8) if name.startswith("KNOB") else badge(name, cx + r + 2, cy + r - 2))
        return "".join(s)

    for n, (x, y) in KNOBS_L.items():
        o.append(knob(n, x, y, 18 if n != "MASTER" else 16))
    for n, (x, y) in KNOBS_R.items():
        o.append(knob(n, x, y, 14))
    # octave buttons
    for i, name in enumerate(["OCT-", "OCT+"]):
        lit = name in hl
        op = 1 if lit else dimop
        x = OX + 22 + i * 56
        o.append(f'<g opacity="{op}"><rect x="{x}" y="{OY + 172}" width="50" height="22" rx="4" fill="{"#7C5BD6" if lit else "#3A3348"}" stroke="{VIOLET if lit else "#5B5170"}" stroke-width="1"/>')
        o.append(t(x + 25, OY + 186.5, name.replace("-", "&#8722;"), 8.6, INK, 600) + "</g>")
        o.append(badge(name, x + 48, OY + 172))
    # screen
    lit = "SCREEN" in hl
    o.append(f'<g opacity="{1 if (lit or screen) else .7}"><rect x="{OX + 152}" y="{OY + 5}" width="232" height="230" rx="10" fill="#0E0B14" stroke="{VIOLET if lit else RULE}" stroke-width="{3 if lit else 1.5}"/>')
    o.append(f'<rect x="{OX + 161}" y="{OY + 13}" width="214" height="214" rx="3" fill="#08060C"/>')
    if screen:
        o.append(f'<g transform="translate({OX + 161},{OY + 13}) scale({214 / 240:.4f})">{screen}</g>')
    else:
        o.append(t(OX + 268, OY + 124, "SCREEN", 10, "#4B4360", 600, ls=2))
    o.append("</g>")
    # button grid
    o.append(f'<rect x="{OX + 397}" y="{OY + 94}" width="162" height="72" rx="6" fill="#2B2440" stroke="{RULE}"/>')
    for r, row in enumerate(BUTTONS):
        for c, name in enumerate(row):
            lit = name in hl
            op = 1 if lit else dimop
            x = OX + 401 + c * 26
            y = OY + 99 + r * 33
            o.append(f'<g opacity="{op}"><rect x="{x}" y="{y}" width="24" height="28" rx="3.5" fill="{"#7C5BD6" if lit else "#3A3348"}" stroke="{VIOLET if lit else "#5B5170"}" stroke-width="1"/>')
            o.append(t(x + 12, y + 17.5, name, 6.4 if len(name) > 3 else 7, INK, 600) + "</g>")
            o.append(badge(name, x + 12, y - 1))
    # keyboard
    op = 1 if keys_hl else .4
    o.append(f'<g opacity="{op}"><rect x="{OX + 9}" y="{OY + 247}" width="546" height="106" rx="10" fill="#2B2440" stroke="{RULE}"/>')
    for i in range(WHITE_N):
        x = OX + _white_x(i) - 13
        o.append(f'<rect x="{x:.1f}" y="{OY + 297}" width="26" height="50" rx="11" fill="{"#8E6FE0" if keys_hl else "#4A4258"}" stroke="#0E0B14" stroke-width=".8"/>')
    for i in BLACK_AFTER:
        x = OX + (_white_x(i) + _white_x(i + 1)) / 2 - 12
        o.append(f'<rect x="{x:.1f}" y="{OY + 251}" width="24" height="42" rx="10" fill="{"#5E43B5" if keys_hl else "#3A3348"}" stroke="#0E0B14" stroke-width=".8"/>')
    o.append("</g>")
    if "KEYS" in nums:
        o.append(badge("KEYS", OX + 540, OY + 252))
    return (f'<svg class="panel" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'font-family="{SANS}">{"".join(o)}</svg>')


# ---------------------------------------------------------------------------
# Cover art: five engine arcs rising from a keyboard horizon, a chord of
# three notes stacked like moons.
# ---------------------------------------------------------------------------
def cover_art():
    W, H = 400, 330
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    o.append('<defs><radialGradient id="glow" cx="50%" cy="85%" r="60%">'
             f'<stop offset="0" stop-color="{VIOLET}" stop-opacity=".35"/>'
             f'<stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient></defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
    cx, cy = 200, 290
    cols = list(ENGINE.values())
    for i, c in enumerate(cols):
        r = 70 + i * 26
        o.append(f'<path d="M{cx - r},{cy} A{r},{r} 0 0 1 {cx + r},{cy}" fill="none" stroke="{c}" '
                 f'stroke-width="7" stroke-linecap="round" opacity="{.95 - i * .08:.2f}"/>')
    # stacked chord: three notes
    for j, (y, rr) in enumerate([(178, 15), (138, 12), (102, 9)]):
        o.append(f'<circle cx="{cx}" cy="{y}" r="{rr}" fill="{[ORCHID, VIOLET, AMETHYST][j]}"/>')
    o.append(f'<line x1="{cx}" y1="{100}" x2="{cx}" y2="{180}" stroke="{INK}" stroke-opacity=".25" stroke-width="1.5" stroke-dasharray="2 5"/>')
    # stars
    import random
    random.seed(7)
    for _ in range(38):
        x, y = random.uniform(10, 390), random.uniform(8, 200)
        if abs(x - cx) < 40 and y > 80:
            continue
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.choice([.8, 1, 1.3, 1.7])}" fill="{INK}" opacity="{random.uniform(.25, .7):.2f}"/>')
    # keyboard horizon
    kx0, kw = 40, 320
    o.append(f'<rect x="{kx0}" y="{cy}" width="{kw}" height="30" rx="4" fill="{PANEL}"/>')
    n = 16
    for i in range(n):
        x = kx0 + 4 + i * (kw - 8) / n
        o.append(f'<rect x="{x:.1f}" y="{cy + 4}" width="{(kw - 8) / n - 3:.1f}" height="22" rx="3" fill="#4A4258"/>')
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------------------
# One key, three notes: what a chord mode does
# ---------------------------------------------------------------------------
def one_key_chord():
    W, H = 520, 170
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{SANS}">']
    # left: one finger, one key
    o.append(f'<rect x="20" y="40" width="120" height="96" rx="12" fill="{PANEL}" stroke="{RULE}"/>')
    o.append(f'<rect x="62" y="62" width="36" height="58" rx="12" fill="#8E6FE0"/>')
    o.append(t(80, 30, "you press one key", 12, MUTED, 500))
    o.append(t(80, 152, "A", 14, INK, 600))
    # arrow
    o.append(f'<path d="M160,88 L232,88" stroke="{VIOLET}" stroke-width="2.5" fill="none"/>')
    o.append(f'<path d="M232,81 L244,88 L232,95 Z" fill="{VIOLET}"/>')
    o.append(t(202, 76, "CHRD", 10.5, VIOLET, 600, ls=1))
    # right: staff-ish stack
    sx = 270
    for k in range(5):
        y = 48 + k * 20
        o.append(f'<line x1="{sx}" y1="{y}" x2="{sx + 220}" y2="{y}" stroke="{RULE}" stroke-width="1.2"/>')
    notes = [(128, "A", "root", ORCHID), (88, "C", "third", VIOLET), (48, "E", "fifth", AMETHYST)]
    for y, n, role, c in notes:
        o.append(f'<ellipse cx="{sx + 80}" cy="{y}" rx="13" ry="9.5" fill="{c}"/>')
        o.append(t(sx + 80, y + 4, n, 10, BG, 700))
        o.append(t(sx + 106, y + 4, role, 11.5, INK, 500, anchor="start"))
    o.append(t(sx + 110, 160, "you hear a chord: A minor", 12, MUTED, 500))
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------------------
# Prophet signal flow strip for the cheat sheet
# ---------------------------------------------------------------------------
def prophet_flow():
    W, H = 540, 92
    c = ENGINE["PROPHET"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{SANS}">']
    boxes = [("OSC A + B", "saw, pulse, tri"), ("MIXER", "+ noise"), ("FILTER", "4-pole, SSI / CURTIS"), ("AMP", "envelope")]
    bw, gap = 104, 34
    for i, (a, b) in enumerate(boxes):
        x = 10 + i * (bw + gap)
        o.append(f'<rect x="{x}" y="14" width="{bw}" height="52" rx="9" fill="{PANEL}" stroke="{c}" stroke-width="1.6"/>')
        o.append(t(x + bw / 2, 37, a, 12, INK, 600, ls=.6))
        o.append(t(x + bw / 2, 54, b, 9.5, MUTED, 400))
        if i < 3:
            ax = x + bw + 4
            o.append(f'<path d="M{ax},40 L{ax + gap - 12},40" stroke="{AMETHYST}" stroke-width="2"/>')
            o.append(f'<path d="M{ax + gap - 12},35 L{ax + gap - 4},40 L{ax + gap - 12},45 Z" fill="{AMETHYST}"/>')
    # filter envelope arrow underneath
    fx = 10 + 2 * (bw + gap) + bw / 2
    o.append(f'<path d="M{fx - 60},86 Q{fx},86 {fx},70" fill="none" stroke="{ORCHID}" stroke-width="1.6" stroke-dasharray="3 3"/>')
    o.append(t(fx - 64, 89, "filter envelope", 9.5, ORCHID, 500, anchor="end"))
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------------------
# Book figures
# ---------------------------------------------------------------------------
def _svg(W, H, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{SANS}">{body}</svg>'


def _arrow(x1, y1, x2, y2, c=VIOLET, w=2):
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 9 * math.cos(ang), y2 - 9 * math.sin(ang)
    p1 = (hx + 5 * math.sin(ang), hy - 5 * math.cos(ang))
    p2 = (hx - 5 * math.sin(ang), hy + 5 * math.cos(ang))
    return (f'<line x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{c}" stroke-width="{w}"/>'
            f'<path d="M{x2},{y2} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z" fill="{c}"/>')


def _box(x, y, w, h, title, sub="", stroke=AMETHYST, fill=PANEL, tc=INK):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
    if sub:
        s += t(x + w / 2, y + h / 2 - 2, title, 12, tc, 600, ls=.5) + t(x + w / 2, y + h / 2 + 13, sub, 9.5, MUTED, 400)
    else:
        s += t(x + w / 2, y + h / 2 + 4, title, 12, tc, 600, ls=.5)
    return s


def nav_fig():
    """OCT+ goes in, OCT- comes back out."""
    o = []
    levels = [("STAGE", "home base"), ("A PAGE", "e.g. CHORD"), ("A SHEET", "hold OCT+"), ("A QUESTION", "yes or no")]
    for i, (a, b) in enumerate(levels):
        x = 20 + i * 128
        o.append(_box(x, 40, 104, 52, a, b, stroke=[AMETHYST, VIOLET, ORCHID, ORCHID][i]))
        if i < 3:
            o.append(_arrow(x + 106, 56, x + 126, 56, VIOLET))
            o.append(_arrow(x + 126, 78, x + 106, 78, MUTED))
    o.append(t(276, 22, "OCT+  goes in, enters, confirms", 12, VIOLET, 600))
    o.append(t(276, 118, "OCT−  backs out, one step at a time", 12, MUTED, 600))
    return _svg(552, 130, "".join(o))


def keyboard(lit=(), x0=10, y0=10, w=520, h=100, labels=None, dimmed=(), mark=None, start="F"):
    """16-white-key FM-1 style keyboard F3..G5. lit: white-key indexes (0..15) to light,
    labels: {white index: text}."""
    o = []
    kw = w / 16
    names = "FGABCDE"
    si = names.index(start)
    for i in range(16):
        x = x0 + i * kw
        on = i in lit
        dim = i in dimmed
        fill = "#8E6FE0" if on else ("#2B2440" if dim else "#4A4258")
        o.append(f'<rect x="{x + 1.5:.1f}" y="{y0}" width="{kw - 3:.1f}" height="{h}" rx="6" fill="{fill}"/>')
        if labels and i in labels:
            o.append(t(x + kw / 2, y0 + h - 10, labels[i], 10.5, BG if on else MUTED, 700))
    # black keys
    for i in range(15):
        n = names[(si + i) % 7]
        if n in "FGACD":
            x = x0 + (i + 1) * kw - kw * .32
            o.append(f'<rect x="{x:.1f}" y="{y0}" width="{kw * .64:.1f}" height="{h * .56:.1f}" rx="5" fill="#0E0B14" stroke="#2B2440"/>')
    return "".join(o)


def scale_fig():
    """A natural minor: the white keys from A happen to be the scale; SNAP moves strays down."""
    o = []
    # white keys F3..G5: F G A B C D E F G A B C D E F G ; A minor = A B C D E F G => all whites
    labels = {i: "FGABCDE"[i % 7] for i in range(16)}
    o.append(keyboard(lit=set(range(16)), labels=labels, x0=16, y0=36, w=520, h=96))
    o.append(t(276, 22, "A natural minor uses only these notes: A B C D E F G", 12, INK, 600))
    o.append(t(276, 160, "With QNT on SNAP, a black key drops to the scale note just below it, so every key stays in the scale.", 11, MUTED, 400))
    return _svg(552, 172, "".join(o))


def voicing_fig():
    o = []
    def stack(x, notes, title, sub):
        o.append(t(x + 60, 20, title, 12.5, VIOLET, 600, ls=1))
        o.append(t(x + 60, 196, sub, 10.5, MUTED, 400))
        for k in range(9):
            y = 40 + k * 16
            o.append(f'<line x1="{x}" y1="{y}" x2="{x + 120}" y2="{y}" stroke="{RULE}" stroke-width="1"/>')
        cols = [ORCHID, VIOLET, AMETHYST]
        for j, (lvl, n) in enumerate(notes):
            y = 168 - lvl * 8
            o.append(f'<ellipse cx="{x + 60}" cy="{y}" rx="12" ry="8" fill="{cols[j]}"/>' + t(x + 60, y + 3.6, n, 9, BG, 700))
    stack(40, [(0, "A"), (2, "C"), (4, "E")], "CLOSE", "notes huddled together")
    stack(210, [(0, "A"), (6, "E"), (9, "C")], "OPEN", "same notes, spread out")
    stack(380, [(2, "C"), (4, "E"), (7, "A")], "INV1", "a different note at the bottom")
    return _svg(552, 208, "".join(o))


def arp_fig():
    o = []
    o.append(t(80, 22, "you hold", 11.5, MUTED, 500))
    for j, (y, n) in enumerate([(120, "A"), (96, "C"), (72, "E")]):
        o.append(f'<ellipse cx="80" cy="{y}" rx="13" ry="9" fill="{[ORCHID, VIOLET, AMETHYST][j]}"/>' + t(80, y + 4, n, 10, BG, 700))
    o.append(_arrow(118, 96, 168, 96))
    o.append(t(143, 84, "ARP UP", 9.5, VIOLET, 600, ls=1))
    o.append(t(360, 22, "you hear, one note at a time (OCT 2)", 11.5, MUTED, 500))
    seq = [(0, "A"), (1, "C"), (2, "E"), (3, "A"), (4, "C"), (5, "E")]
    for i, (lvl, n) in enumerate(seq * 1):
        x = 196 + i * 54
        y = 136 - lvl * 16
        c = [ORCHID, VIOLET, AMETHYST][i % 3]
        o.append(f'<rect x="{x}" y="{y - 9}" width="44" height="18" rx="6" fill="{c}"/>' + t(x + 22, y + 4, n, 10, BG, 700))
    o.append(f'<line x1="196" y1="156" x2="520" y2="156" stroke="{RULE}" stroke-width="1.2"/>')
    o.append(t(358, 172, "time →", 10, MUTED, 400))
    return _svg(552, 182, "".join(o))


def drum_grid_fig():
    lanes = ["KICK", "SNARE", "CLAP", "HATCL", "HATOP", "TOM", "RIM", "BELL"]
    hits = {"KICK": [0, 4, 8, 12], "SNARE": [4, 12], "HATCL": [0, 2, 4, 6, 8, 10, 12, 14]}
    o = []
    x0, y0, cw, ch = 74, 30, 28, 20
    for s in range(16):
        o.append(t(x0 + s * cw + cw / 2, 22, str(s + 1), 9, VIOLET if s % 4 == 0 else MUTED, 600))
    for r, ln in enumerate(lanes):
        y = y0 + r * ch
        o.append(t(66, y + 14, ln, 9.5, INK if ln in hits else MUTED, 600, anchor="end"))
        for s in range(16):
            x = x0 + s * cw
            on = s in hits.get(ln, [])
            fill = "#8E6FE0" if on else ("#2B2440" if s % 4 else "#352C4A")
            o.append(f'<rect x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{ch - 4}" rx="4" fill="{fill}"/>')
    o.append(t(x0 + 8 * cw, y0 + 8 * ch + 22, "One bar of 16 steps. Each white key is one step; the black keys choose the lane.", 10.5, MUTED, 400))
    return _svg(552, 220, "".join(o))


def capture_fig():
    o = []
    x0, w = 30, 480
    bw = w / 4
    for b in range(4):
        x = x0 + b * bw
        o.append(f'<rect x="{x + 3}" y="40" width="{bw - 6}" height="46" rx="8" fill="{PANEL}" stroke="{RULE}"/>')
        o.append(t(x + bw / 2, 30, f"bar {b + 1}", 10.5, MUTED, 500))
        o.append(f'<rect x="{x + 10}" y="50" width="{bw - 26}" height="26" rx="6" fill="{[ORCHID, VIOLET, AMETHYST, "#8E6FE0"][b]}"/>')
        o.append(t(x + 10 + (bw - 26) / 2, 67, f"chord {b + 1}", 10.5, BG, 700))
    hx = x0 + w + 6
    o.append(f'<line x1="{hx}" y1="34" x2="{hx}" y2="96" stroke="{ORCHID}" stroke-width="2.4" stroke-dasharray="4 3"/>')
    o.append(t(hx + 4, 112, "the next \"one\": hold REC", 11, ORCHID, 600, anchor="end"))
    o.append(t(270, 136, "Play one chord per bar. On the next \"one\", hold REC instead of playing chord 1.", 10.5, MUTED, 400))
    return _svg(552, 146, "".join(o))


def motion_fig():
    o = []
    x0, x1, yb, yt = 40, 520, 120, 30
    o.append(f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="{RULE}"/>')
    for b in range(5):
        x = x0 + b * (x1 - x0) / 4
        o.append(f'<line x1="{x:.1f}" y1="{yt - 6}" x2="{x:.1f}" y2="{yb}" stroke="{RULE}" stroke-dasharray="2 4"/>')
        if b < 4:
            o.append(t(x + (x1 - x0) / 8, yb + 16, f"bar {b + 1}", 10, MUTED, 500))
    pts = []
    for i in range(121):
        u = i / 120
        v = .15 + .75 * (math.sin(u * math.pi) ** 1.5)
        pts.append((x0 + u * (x1 - x0), yb - v * (yb - yt)))
    o.append(f'<path d="{"M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{ORCHID}" stroke-width="3" stroke-linecap="round"/>')
    o.append(t(30, yt - 10, "CUTOFF", 10.5, VIOLET, 600, anchor="start", ls=1))
    o.append(t(280, 156, "One slow turn of KNOB 1, recorded. It plays back the same way every loop.", 10.5, MUTED, 400))
    return _svg(552, 166, "".join(o))


def lfo_fig():
    o = []
    x0, x1, ym, a = 40, 520, 70, 34
    pts = []
    for i in range(241):
        u = i / 240
        ph = (u * 3) % 1
        v = 4 * ph - 1 if ph < .5 else 3 - 4 * ph
        pts.append((x0 + u * (x1 - x0), ym - v * a))
    o.append(f'<line x1="{x0}" y1="{ym}" x2="{x1}" y2="{ym}" stroke="{RULE}" stroke-dasharray="2 4"/>')
    o.append(f'<path d="{"M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{AMETHYST}" stroke-width="3"/>')
    o.append(t(x0, 20, "brighter", 10, VIOLET, 600, anchor="start"))
    o.append(t(x0, 122, "darker", 10, MUTED, 600, anchor="start"))
    o.append(t(280, 146, "An LFO is a hand that never gets tired: it keeps turning the knob for you.", 10.5, MUTED, 400))
    return _svg(552, 156, "".join(o))


def fx_flow_fig():
    o = []
    o.append(_box(10, 30, 96, 52, "TRACK", "your sound"))
    o.append(_arrow(108, 56, 128, 56))
    o.append(_box(130, 30, 104, 52, "NOTE FX", "TAIL, ECHO", stroke=VIOLET))
    o.append(_arrow(236, 56, 256, 56))
    o.append(_box(258, 30, 96, 52, "LEVEL", "and PAN"))
    o.append(_arrow(356, 56, 446, 56, MUTED))
    o.append(_box(448, 30, 96, 52, "MASTER", "punch FX", stroke=ORCHID))
    o.append(_arrow(306, 84, 306, 112, ORCHID))
    o.append(t(318, 102, "SEND", 9.5, ORCHID, 600, anchor="start", ls=1))
    o.append(_box(220, 114, 172, 52, "SHARED  A · B · C", "reverb, chorus, drive…", stroke=ORCHID))
    o.append(f'<path d="M394,140 L496,140 L496,90" fill="none" stroke="{ORCHID}" stroke-width="2"/>')
    o.append(f'<path d="M491,98 L496,86 L501,98 Z" fill="{ORCHID}"/>')
    o.append(t(445, 156, "RETURN", 9.5, ORCHID, 600, ls=1))
    return _svg(552, 176, "".join(o))


def song_grid_fig():
    o = []
    secs = ["INTRO", "A", "B", "B", "A", "END"]
    tracks = ["1 PAD", "2 BASS", "3 LEAD", "4 DRUMS"]
    grid = [
        ["P1", "P1", "P1", "P1", "P1", "P1"],
        ["—", "P1", "P1", "P1", "P1", "P1"],
        ["—", "—", "P1", "P1", "—", "—"],
        ["—", "P1", "P2", "P2", "P1", "—"],
    ]
    x0, y0, cw, ch = 100, 34, 72, 30
    for i, s in enumerate(secs):
        o.append(t(x0 + i * cw + cw / 2, 24, s, 10, VIOLET, 600, ls=1))
    for r, tr in enumerate(tracks):
        y = y0 + r * ch
        o.append(t(78, y + 19, tr, 10, INK, 600, anchor="end"))
        for i in range(len(secs)):
            v = grid[r][i]
            x = x0 + i * cw
            if v == "—":
                o.append(f'<rect x="{x + 3}" y="{y + 3}" width="{cw - 6}" height="{ch - 6}" rx="6" fill="none" stroke="{RULE}" stroke-dasharray="3 3"/>')
                o.append(t(x + cw / 2, y + 19, "rest", 9, MUTED, 400))
            else:
                c = [ "#6D5BD0", "#A78BFA", "#D946EF", "#9D4EDD"][r]
                o.append(f'<rect x="{x + 3}" y="{y + 3}" width="{cw - 6}" height="{ch - 6}" rx="6" fill="{c}"/>')
                o.append(t(x + cw / 2, y + 19, v, 10, "#fff", 700))
    o.append(t(310, 172, "Sections run left to right. Each track plays a pattern, or rests.", 10.5, MUTED, 400))
    return _svg(552, 182, "".join(o))


def mpc_fig():
    o = []
    o.append(_box(20, 40, 150, 70, "FM-1", "running Melodee", stroke=VIOLET))
    o.append(_box(382, 40, 150, 70, "MPC SAMPLE", "", stroke=AMETHYST))
    o.append(_arrow(172, 62, 380, 62, ORCHID, 2.4))
    o.append(t(276, 54, "audio out → audio in", 10.5, ORCHID, 600))
    o.append(t(276, 78, "(the reliable way: record what you hear)", 9.5, MUTED, 400))
    o.append(f'<line x1="172" y1="96" x2="380" y2="96" stroke="{AMETHYST}" stroke-width="2" stroke-dasharray="5 4"/>')
    o.append(t(276, 116, "optional USB link: pads, clock (see the try boxes)", 9.5, MUTED, 400))
    return _svg(552, 130, "".join(o))


def engine_strip():
    o = []
    names = list(ENGINE.items())
    w = 104
    for i, (n, c) in enumerate(names):
        x = 6 + i * (w + 6)
        o.append(f'<rect x="{x}" y="6" width="{w}" height="44" rx="9" fill="{c}"/>')
        o.append(t(x + w / 2, 33, n, 13, "#fff" if n not in ("CZ-1", "FM6") else BG, 700, ls=.8))
    return _svg(556, 56, "".join(o))


# ---------------------------------------------------------------------------
# Example screens (v1.1). Deliberately simple: a page title and the four knob
# values, as the manual describes them. Drawn in a 240 x 240 box and marked
# EXAMPLE so nobody mistakes them for screenshots.
# ---------------------------------------------------------------------------
SCR_BG = "#08060C"


def _scr_frame(title, body):
    o = [f'<rect width="240" height="240" fill="{SCR_BG}"/>']
    o.append(t(14, 30, title, 17, INK, 600, anchor="start", ls=1))
    o.append(f'<rect x="168" y="14" width="60" height="18" rx="9" fill="none" stroke="#4B4360"/>')
    o.append(t(198, 27, "EXAMPLE", 8.5, "#7A6F92", 600, ls=1))
    o.append(f'<line x1="14" y1="42" x2="226" y2="42" stroke="{RULE}"/>')
    o.append(body)
    return "".join(o)


def _knob_strip(cols, y=176):
    """cols: [(label, value)] for KNOB 1 to 4. value: text, or a float 0..1 drawn as a bar."""
    o = []
    for i, (lab, val) in enumerate(cols):
        x = 14 + i * 54
        o.append(f'<rect x="{x}" y="{y}" width="50" height="50" rx="7" fill="#1F1A2B"/>')
        o.append(t(x + 25, y + 15, lab, 9, MUTED, 600, ls=.4))
        if isinstance(val, float):
            o.append(f'<rect x="{x + 8}" y="{y + 30}" width="34" height="7" rx="3.5" fill="#3A3150"/>')
            o.append(f'<rect x="{x + 8}" y="{y + 30}" width="{34 * val:.1f}" height="7" rx="3.5" fill="{VIOLET}"/>')
        else:
            o.append(t(x + 25, y + 37, val, 12 if len(val) < 6 else 10, INK, 700))
    return "".join(o)


def scr_knobs(title, cols, mid=""):
    return _scr_frame(title, mid + _knob_strip(cols, 100 if not mid else 176))


def scr_stage():
    rows = [("1", "It's a Prophet", "#F28B82"), ("2", "FM6 SOLID BASS", "#F5B971"),
            ("3", "CZ-1 SYNTH.LEAD 1", "#8EE3C8"), ("4", "808", "#C4B5FD")]
    o = []
    for i, (n, name, c) in enumerate(rows):
        y = 52 + i * 29
        o.append(f'<rect x="14" y="{y}" width="212" height="24" rx="6" fill="#1F1A2B"/>')
        o.append(f'<rect x="14" y="{y}" width="5" height="24" rx="2.5" fill="{c}"/>')
        o.append(t(28, y + 16, n, 10, c, 700, anchor="start"))
        o.append(t(42, y + 16, name, 10.5, INK, 500, anchor="start"))
    body = "".join(o) + _knob_strip([("CUTOFF", .55), ("RES", .2), ("ENV", .4), ("REL", .35)])
    return _scr_frame("STAGE", body)


def scr_grid():
    lanes = ["KICK", "SNARE", "CLAP", "HATCL", "HATOP", "TOM", "RIM", "BELL"]
    hits = {0: [0, 4, 8, 12], 1: [4, 12], 3: [0, 2, 4, 6, 8, 10, 12, 14]}
    o = []
    for r, ln in enumerate(lanes):
        y = 52 + r * 20
        o.append(t(52, y + 12, ln, 8.5, INK if r in hits else MUTED, 600, anchor="end"))
        for s in range(16):
            x = 58 + s * 10.5
            on = s in hits.get(r, [])
            o.append(f'<rect x="{x:.1f}" y="{y + 2}" width="8" height="13" rx="2" fill="{"#C084FC" if on else ("#2B2440" if s % 4 else "#3A3150")}"/>')
    return _scr_frame("NOTES", "".join(o))


def scr_song():
    secs = 6
    grid = [[1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0], [0, 1, 2, 2, 1, 0]]
    cols = ["#6D5BD0", "#A78BFA", "#D946EF", "#9D4EDD"]
    o = []
    for r in range(4):
        y = 60 + r * 30
        o.append(t(22, y + 16, str(r + 1), 10, MUTED, 600))
        for i in range(secs):
            x = 34 + i * 32
            v = grid[r][i]
            if v:
                o.append(f'<rect x="{x}" y="{y}" width="29" height="24" rx="5" fill="{cols[r]}"/>')
                o.append(t(x + 14.5, y + 16, f"P{v}", 9, "#fff", 700))
            else:
                o.append(f'<rect x="{x + .5}" y="{y + .5}" width="28" height="23" rx="5" fill="none" stroke="#3A3150" stroke-dasharray="2 2"/>')
    o.append(f'<rect x="{34 + secs * 32}" y="60" width="10" height="114" rx="3" fill="none" stroke="#4B4360" stroke-dasharray="2 2"/>')
    o.append(t(120, 200, "sections →", 9.5, MUTED, 500))
    return _scr_frame("SONG", "".join(o))

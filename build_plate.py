# -*- coding: utf-8 -*-
"""'The Day' — Wednesday 18 November 2026.

45 verified stories on one 1024x1024 plate: 3 illustrated leads, 12 story cards with
measured headlines, a pinned world map and 30 one-liners in three columns, plus a strip of
the day's numbers. Every text run is measured with PIL before it is placed, so nothing
overflows its box. Pure SVG output: deterministic, no external assets.
"""
import io
from PIL import ImageFont

GEORGIA = "C:/Windows/Fonts/georgia.ttf"
GEORGIA_B = "C:/Windows/Fonts/georgiab.ttf"
ARIAL = "C:/Windows/Fonts/arial.ttf"
ARIAL_B = "C:/Windows/Fonts/arialbd.ttf"

_font_cache = {}


def f(path, size):
    key = (path, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


def wpx(s, path=ARIAL, size=12):
    """Width of a text run in CSS pixels, as the browser would lay it out."""
    return f(path, size).getlength(s)


def wrap_px(s, maxw, path=ARIAL, size=12):
    lines, cur = [], ""
    for word in s.split():
        t = (cur + " " + word).strip()
        if wpx(t, path, size) > maxw and cur:
            lines.append(cur)
            cur = word
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def clip(s, maxw, path=ARIAL, size=12):
    t = s
    while t and wpx(t + "…", path, size) > maxw:
        t = t[:-1]
    return (t + "…") if t != s else s


# ------------------------------------------------------------------ content
LEADS = [
    dict(region="ASIA \u00b7 APEC SUMMIT", color="#6d3fb5",
         title="Xi greets Trump on the tarmac; Putin joins them in Shenzhen",
         blurb="Crowds welcome Air Force One in Shenzhen. The three leaders meet for the "
               "first time on Thursday \u2014 and Putin's nuclear briefcase is spotted in the room.",
         ill="summit", stat="APEC"),
    dict(region="MIDDLE EAST \u00b7 IRAN WAR", color="#b3402e",
         title="America strikes Qeshm Island; Iran answers Kuwait and Bahrain",
         blurb="Kuwait says it repelled its first Iranian attack in two months, and Bahrain "
               "says it was hit after the US air strike on the Iranian island.",
         ill="gulf", stat="QESHM"),
    dict(region="CULTURE \u00b7 LAUNCH", color="#c86a28",
         title="GTA VI lands and critics call it a masterpiece",
         blurb="PlayStation suffers widespread network problems hours before release, and the "
               "studio says the game was made with working conditions to match.",
         ill="gta", stat="GTA VI"),
]

NUMBERS = [
    ("26", "years of measles-free\nstatus gone in the US"),
    ("\u00a3443", "expected yearly rise in a\ntypical UK energy bill"),
    ("3.6%", "UK inflation in the year\nto October"),
    ("1.8M", "hens to be culled after\nbird flu in Florida"),
    ("16bn", "miles from Earth: Voyager 1,\n49 years after launch"),
    ("27 yrs", "the sentence for the\nIran-backed Trump plot"),
]

CARDS = [
    ("MIDDLE EAST", "ISRAEL-PALESTINE", "#b3402e", "Israel opens a rare ground operation in Gaza",
     "Tanks advance west of the Yellow Line; Gazans flee their shelters.", "tank"),
    ("MIDDLE EAST", "ISRAEL-PALESTINE", "#b3402e", "Settler kills a Palestinian grandmother",
     "Killed in the occupied West Bank near Jericho, where Israel's army beat a journalist.", "olive"),
    ("EUROPE", "UKRAINE", "#1a66c2", "Russian strikes on Odesa kill four, injure 13",
     "The port city is hit again as the front line moves inland.", "flame"),
    ("EUROPE", "UKRAINE", "#1a66c2", "Video shows the moment part of the Crimea bridge fell",
     "BBC Verify analyses the final seconds before the span came down.", "bridge"),
    ("US", "POLITICS", "#6d3fb5", "Democrats nominate Jeffries for Speaker",
     "On a path to becoming the first Black speaker of the House.", "capitol"),
    ("US", "POLITICS", "#6d3fb5", "Democrats win the Alaska Senate race",
     "Peltola's confirmation caps the rout; the Senate is 56-44.", "ballot"),
    ("GLOBAL", "MEDICINE", "#0d8a4f", "E coli toxin a leading suspect in bowel cancer",
     "Scientists tell Commons colibactin in early life may drive cancer under 50.", "dna"),
    ("GLOBAL", "MEDICINE", "#0d8a4f", "WHO sounds alarm over antibiotic resistance",
     "Common bacteria are now resistant to front-line and last-resort drugs.", "pill"),
    ("GLOBAL", "SCIENCE", "#1a66c2", "Voyager 1 passes one light-day from Earth",
     "A record 16 billion miles after 49 years \u2014 and it still beams data back.", "probe"),
    ("AMERICAS", "WEATHER", "#1a66c2", "Torrential rain floods South Florida",
     "Whole neighbourhoods stay under water; schools, roads and hospitals hit.", "rain"),
    ("AMERICAS", "AGRICULTURE", "#0d8a4f", "Largest US egg producer to cull 1.8m birds",
     "Avian influenza at a Florida site: 2.7% of the Cal-Maine flock.", "egg"),
    ("GLOBAL", "AI", "#c86a28", "Java flaw found \u2014 and senators turn to the outages",
     "A startup used AI to find it; lawmakers now quiz the White House AI chief.", "chip"),
]

ONELINERS = [
    # (city, lon, lat, country, text)
    ("The Hague", 4.30, 52.07, "Netherlands", "the ICJ rules that Myanmar committed genocide of the Rohingya"),
    ("The Hague", 4.30, 52.07, "Netherlands", "fears grow that a Nobel-winning judge faces sanctions after the ruling"),
    ("Aden", 45.03, 12.79, "Yemen", "the Houthis may besiege Aden rather than storm it"),
    ("Sanaa", 44.21, 15.35, "Yemen", "UNICEF says dozens more children were killed as hostilities escalate"),
    ("Washington", -77.04, 38.90, "US", "a Pakistani man gets 27 years for an Iran-backed plot to kill Trump"),
    ("Washington", -77.04, 38.90, "US", "Rubio says there is no evidence the tech outages are a systemic attack"),
    ("Washington", -77.04, 38.90, "US", "a Senate committee rejects Trump's nominee to lead the NSF"),
    ("Kharkiv", 49.99, 49.99, "Ukraine", "an underground war in an old Soviet gas pipeline: \u201cthe drones don't fly here\u201d"),
    ("Kyiv", 30.52, 50.45, "Ukraine", "the bridge came down after a Ukrainian drone and missile strike"),
    ("Odesa", 30.73, 46.48, "Ukraine", "Russian strikes kill four and injure thirteen in the port city"),
    ("Ottawa", -75.70, 45.42, "Canada", "Carney calls Putin's downplaying of sanctions \u201ca lie\u201d"),
    ("Brussels", 4.35, 50.85, "Belgium", "five EU states make plans to deport asylum seekers to Rwanda"),
    ("Brussels", 4.35, 50.85, "Belgium", "Europe plans to catch the next computer chip wave"),
    ("London", -0.13, 51.51, "UK", "a leak shows what is inside the 72-paragraph UK-EU reset draft"),
    ("London", -0.13, 51.51, "UK", "a \u00a310m study will test the social media ban's effect on young minds"),
    ("Cairo", 31.24, 30.04, "Egypt", "leaked papers say the EU sugarcoated figures to release \u20ac2.5bn"),
    ("Beirut", 35.50, 33.89, "Lebanon", "the World Bank says the reconstruction is making slow progress"),
    ("Jerusalem", 35.21, 31.77, "Israel", "Israel delays West Bank settlement contracts after UK sanctions"),
    ("Gaza", 34.46, 31.50, "Palestine", "tanks push past the Yellow Line as thousands flee their shelters"),
    ("Shenzhen", 114.06, 22.54, "China", "inside the race to put humanoid robot helpers in our homes"),
    ("Seoul", 126.98, 37.57, "South Korea", "an AI cheating scandal upends the national university exams"),
    ("Manila", 120.98, 14.60, "Philippines", "Trump meets Marcos and calls him a \u201clongtime friend\u201d"),
    ("Tokyo", 139.69, 35.69, "Japan", "the US-Japan potato war is about to reach boiling point"),
    ("Canberra", 149.13, -35.28, "Australia", "Albanese defies critics for the APEC summit photo with Putin"),
    ("Canberra", 149.13, -35.28, "Australia", "the business council is more fossil-aligned than its own members"),
    ("Alice Springs", 133.90, -23.70, "Australia", "\u201cphantom forests\u201d in the arid outback were sold as carbon credits"),
    ("Suva", 178.44, -18.13, "Fiji", "the Maldives open talks with an Indian firm over wave energy"),
    ("Miami", -80.19, 25.76, "US", "torrential rain leaves whole neighbourhoods under water"),
    ("Cincinnati", -84.51, 39.10, "US", "Fiona the hippo is fed and cared for after swallowing a hat"),
    ("Derry", -7.32, 55.00, "N Ireland", "a 2,000-year-old bog woman was beheaded, the coroner finds"),
    ("Berlin", 13.40, 52.52, "Germany", "children play beneath a square's ever-watchful Kollwitz statue"),
    ("Limoges", 1.26, 45.85, "France", "rebuilding starts at the city hall one month after the fire"),
    ("Madrid", -3.70, 40.42, "Spain", "who to watch as Spain votes on 29 November"),
    ("Los Angeles", -118.24, 34.05, "US", "LeBron James sues a betting app over using his nickname"),
    ("Santa Clara", -121.96, 37.35, "US", "Nvidia says it won't reinstate Huang after soaring sales"),
]


MAP_W, MAP_H = 282, 196
MAP_LON0, MAP_LON1 = -180.0, 180.0
MAP_LAT0, MAP_LAT1 = 78.0, -58.0


def proj(lon, lat, ox, oy, w=MAP_W, h=MAP_H):
    x = ox + (lon - MAP_LON0) / (MAP_LON1 - MAP_LON0) * w
    y = oy + (MAP_LAT0 - lat) / (MAP_LAT0 - MAP_LAT1) * h
    return x, y


CONTINENTS = [
    # North America
    [(-168, 66), (-156, 71), (-130, 70), (-110, 73), (-85, 70), (-62, 58), (-55, 47),
     (-66, 44), (-74, 38), (-76, 26), (-84, 30), (-81, 25), (-90, 29), (-97, 26),
     (-105, 20), (-110, 28), (-114, 33), (-124, 40), (-124, 48), (-135, 55), (-150, 60)],
    # Greenland
    [(-45, 60), (-25, 70), (-22, 78), (-45, 80), (-60, 76), (-58, 66)],
    # South America
    [(-78, 9), (-62, 11), (-50, 2), (-35, -6), (-38, -20), (-46, -28), (-54, -38),
     (-62, -52), (-70, -55), (-74, -44), (-72, -20), (-76, -6), (-80, 2)],
    # Europe
    [(-9, 38), (-9, 44), (-4, 48), (2, 51), (8, 54), (5, 58), (18, 60), (30, 61),
     (40, 56), (40, 46), (30, 41), (20, 40), (12, 38), (4, 43)],
    # Africa
    [(-17, 15), (-14, 22), (-8, 32), (2, 37), (11, 34), (25, 32), (34, 28), (43, 12),
     (51, 11), (45, -4), (40, -16), (32, -30), (25, -34), (16, -34), (10, -22),
     (2, -6), (-8, 4), (-15, 11)],
    # Asia (mainland + Siberia)
    [(30, 70), (45, 72), (70, 74), (95, 76), (125, 73), (160, 70), (178, 65),
     (170, 60), (155, 55), (143, 52), (135, 42), (129, 35), (122, 30), (108, 21),
     (100, 10), (98, 17), (88, 22), (80, 8), (72, 20), (68, 24), (58, 25), (50, 30),
     (43, 12), (35, 30), (32, 42)],
    # India
    [(68, 24), (74, 33), (88, 27), (80, 8), (72, 15)],
    # Japan + Korea
    [(129, 32), (133, 34), (137, 37), (141, 41), (145, 44), (142, 45), (140, 38),
     (136, 35), (131, 33)],
    # Indonesia / Philippines
    [(95, 6), (106, -6), (115, -8), (125, -9), (135, -4), (140, -8), (130, -9),
     (120, -9), (110, -7), (100, 0)],
    [(119, 6), (123, 18), (126, 6), (121, 2)],
    # Australia
    [(113, -21), (114, -33), (124, -35), (138, -35), (150, -37), (153, -28),
     (145, -15), (130, -12), (119, -20)],
    # New Zealand
    [(172, -34), (178, -38), (174, -41), (167, -46), (170, -38)],
]

PINS_UNUSED = [(58, 38), (86, 78), (86, 104), (186, 32), (210, 64), (228, 42), (242, 60),
        (258, 36), (282, 54), (296, 46), (254, 98), (116, 102)]

ICONS = {
    "tank": '<rect x="4" y="12" width="18" height="7" rx="2" fill="#fff"/><rect x="8" y="8" width="11" height="5" rx="1" fill="#fff"/><path d="M19 12h6" stroke="#fff" stroke-width="2.4"/>',
    "olive": '<path d="M13 4c4 3 4 9 0 16-4-7-4-13 0-16z" fill="#fff"/><path d="M13 7v12" stroke="#0d8a4f" stroke-width="1.2"/>',
    "flame": '<path d="M13 3c4 6 6 8 6 12a6 6 0 0 1-12 0c0-4 2-6 6-12z" fill="#fff"/>',
    "bridge": '<path d="M3 17h20M6 17v-5M12 17V8M18 17v-5" stroke="#fff" stroke-width="2" fill="none"/><path d="M3 12h6M12 8h6" stroke="#fff" stroke-width="2"/>',
    "capitol": '<path d="M13 4l10 6H3z" fill="#fff"/><rect x="5" y="11" width="16" height="3" fill="#fff"/><path d="M7 15v6M12 15v6M17 15v6M4 22h18" stroke="#fff" stroke-width="2"/>',
    "ballot": '<rect x="5" y="4" width="16" height="18" rx="2" fill="#fff"/><path d="M9 11l3 3 6-6" fill="none" stroke="#6d3fb5" stroke-width="2.2"/>',
    "dna": '<path d="M8 3c0 6 10 6 10 12M18 3c0 6-10 6-10 12" fill="none" stroke="#fff" stroke-width="2"/><path d="M8 8h10M8 13h10M9 18h6" stroke="#fff" stroke-width="1.4"/>',
    "pill": '<rect x="4" y="10" width="18" height="7" rx="3.5" fill="#fff" transform="rotate(-30 13 13)"/><path d="M13 2v4M13 20v4" stroke="#fff" stroke-width="2"/>',
    "probe": '<circle cx="13" cy="9" r="4" fill="#fff"/><path d="M13 13v9M9 22h8" stroke="#fff" stroke-width="2"/><path d="M11 5a9 9 0 0 0-6 6" stroke="#fff" stroke-width="1.4" fill="none"/>',
    "rain": '<path d="M7 11a4 4 0 0 1 4-4 5 5 0 0 1 9 2 3.5 3.5 0 0 1-1 7H8a3.5 3.5 0 0 1-1-5z" fill="#fff"/><path d="M10 19l-1 3M14 19l-1 3M18 19l-1 3" stroke="#fff" stroke-width="2"/>',
    "egg": '<ellipse cx="13" cy="13" rx="6" ry="8" fill="#fff"/><circle cx="13" cy="13" r="2" fill="#c9a227"/>',
    "chip": '<rect x="7" y="7" width="12" height="12" rx="2" fill="#fff"/><path d="M10 3v4M16 3v4M10 19v4M16 19v4M3 10h4M3 16h4M19 10h4M19 16h4" stroke="#fff" stroke-width="1.8"/>',
}

# ------------------------------------------------------------------ layout
W = H = 1024
M = 42
CW = W - 2 * M          # 940
LEAD_W = (CW - 2 * 13) // 3    # 304
CARD_COLS = 4
CARD_W = (CW - 3 * 10) // 4    # 227
PAPER = "#f7f2e6"
INK = "#1b1712"
DIM = "#4a4234"
FAINT = "#6b6152"
RED = "#b3402e"


COUNT_STORIES = len(LEADS) + len(CARDS) + len(ONELINERS)
COUNT_PLACES = len(ONELINERS)
COUNT_COUNTRIES = len(set(o[3] for o in ONELINERS))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, size, weight=400, fill=INK, anchor="start", serif=True, spacing=None):
    path = "Georgia, serif" if serif else "Arial, Helvetica, sans-serif"
    sp = ' letter-spacing="%s"' % spacing if spacing else ""
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" fill="%s" '
            'text-anchor="%s"%s>%s</text>') % (x, y, path, size, weight, fill, anchor, sp, esc(s))


def sw(s, size, serif=True):
    return wpx(s, GEORGIA if serif else ARIAL, size)


def lead_ill(kind, ix, iy, w):
    """A drawn scene, 128 tall, w wide."""
    o = []

    def add(s):
        o.append(s)

    def band(txt, sub, bg, fg, subfg):
        add('<rect x="%d" y="%d" width="%d" height="15" fill="%s"/>' % (ix, iy, w, bg))
        add(T(ix + 8, iy + 11, txt, 9.5, 700, fg, serif=False, spacing="1.1"))
        add('<rect x="%d" y="%d" width="%d" height="16" fill="%s"/>' % (ix, iy + 112, w, bg))
        add(T(ix + 8, iy + 124, sub, 8.4, 700, subfg, serif=False, spacing="0.9"))

    if kind == "summit":
        add('<rect x="%d" y="%d" width="%d" height="128" fill="url(#sunset)"/>' % (ix, iy, w))
        add('<circle cx="%d" cy="%d" r="20" fill="#f7c9a0" opacity="0.7"/>' % (ix + 52, iy + 42))
        # helicopter
        hx, hy = ix + w - 62, iy + 32
        add('<rect x="%d" y="%d" width="22" height="5" rx="2" fill="#8e86ad"/>' % (hx, hy))
        add('<rect x="%d" y="%d" width="3" height="8" fill="#8e86ad"/>' % (hx + 3, hy + 5))
        add('<rect x="%d" y="%d" width="12" height="5" rx="2" fill="#8e86ad"/>' % (hx + 7, hy + 12))
        add('<path d="M%d %d h26" stroke="#a79ec4" stroke-width="1.6"/>' % (hx + 10, hy - 3))
        # skyline with windows
        for k in range(10):
            bx = ix + 4 + k * (w - 8) // 10
            bh = 20 + (k * 17) % 40
            add('<rect x="%d" y="%d" width="17" height="%d" fill="#b9aede" opacity="0.8"/>' % (bx, iy + 92 - bh, bh))
            for r in range(2):
                for c in range(2):
                    if (r * 3 + c + k) % 3 == 0:
                        add('<rect x="%d" y="%d" width="4" height="4" fill="#fff" opacity="0.55"/>' % (bx + 4 + c * 7, iy + 96 - bh + r * 10))
        # tarmac
        add('<rect x="%d" y="%d" width="%d" height="20" fill="#7d7596"/>' % (ix, iy + 92, w))
        add('<path d="M%d %d h26" stroke="#e8d47a" stroke-width="1.6" stroke-dasharray="10 8"/>' % (ix + 8, iy + 102))
        # three leaders + flags
        for k, (col, flag) in enumerate((("#2f5f9e", "#2f5f9e"), ("#c0392b", "#c0392b"), ("#c86a28", "#c86a28"))):
            fx = ix + 30 + k * 34
            add('<circle cx="%d" cy="%d" r="6.4" fill="#3a3550"/>' % (fx, iy + 66))
            add('<path d="M%d %d q13 4 13 13 l0 6 q-13 4 -13 -6 z" fill="#332f47"/>' % (fx - 6, iy + 71))
            add('<rect x="%d" y="%d" width="3" height="16" fill="#2b2840"/>' % (fx + 9, iy + 74))
            add('<rect x="%d" y="%d" width="13" height="9" fill="%s"/>' % (fx + 12, iy + 66, flag))
            add('<path d="M%d %d q6 3 1 8" stroke="#332f47" stroke-width="2.4" fill="none"/>' % (fx + 5, iy + 74))
        # press line
        for k in range(9):
            px = ix + 8 + k * 16
            add('<rect x="%d" y="%d" width="5" height="4" rx="1" fill="#5d567a"/>' % (px, iy + 80))
            add('<rect x="%d" y="%d" width="1.6" height="12" fill="#5d567a"/>' % (px + 2, iy + 84))
        # robots
        for k in range(2):
            rx = ix + w - 40 + k * 19
            add('<rect x="%d" y="%d" width="9" height="15" rx="3" fill="#aab3cc"/>' % (rx, iy + 76))
            add('<circle cx="%d" cy="%d" r="5" fill="#dbe1ef"/>' % (rx + 4, iy + 72))
            add('<path d="M%d %d l-6 -6 M%d %d l6 -6" stroke="#aab3cc" stroke-width="2"/>' % (rx + 1, iy + 80, rx + 8, iy + 80))
        band("BEIJING \u00b7 TARMAC GREETING", "SHENZHEN \u00b7 21 LEADERS \u00b7 EUROPE ABSENT", "#6d3fb5", "#ffffff", "#efeaf8")
    elif kind == "gulf":
        add('<rect x="%d" y="%d" width="%d" height="128" fill="#241f33"/>' % (ix, iy, w))
        for k in range(26):
            sx = ix + 6 + (k * 37) % (w - 12)
            sy = iy + 22 + (k * 23) % 40
            add('<circle cx="%d" cy="%d" r="0.9" fill="#cfc7e6" opacity="0.75"/>' % (sx, sy))
        add('<circle cx="%d" cy="%d" r="13" fill="#f6e7c4"/>' % (ix + w - 38, iy + 30))
        add('<circle cx="%d" cy="%d" r="13" fill="#241f33"/>' % (ix + w - 44, iy + 27))
        # jets
        for k in range(2):
            jx = ix + 24 + k * 76
            jy = iy + 26 + (k * 14) % 10
            add('<path d="M%d %d l13 3 l-13 3 l-4 -3 z" fill="#8f86b4"/>' % (jx, jy))
            add('<path d="M%d %d h-26" stroke="#8f86b4" stroke-width="1" opacity="0.6"/>' % (jx, jy + 3))
        # sea
        add('<rect x="%d" y="%d" width="%d" height="56" fill="#332c4a"/>' % (ix, iy + 62, w))
        for k in range(7):
            add('<path d="M%d %d q10 -3 20 0 t20 0" stroke="#4b4268" stroke-width="1.2" fill="none"/>' % (ix + 4, iy + 70 + k * 7, ))
        # island + radar dome
        add('<path d="M%d %d q24 -9 44 0 l7 11 q-29 7 -57 0 z" fill="#1f1a2b"/>' % (ix + 52, iy + 56))
        add('<path d="M%d %d a14 10 0 0 1 28 0 z" fill="#4b4268"/>' % (ix + 60, iy + 56))
        add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#8f86b4" stroke-width="1.4"/>' % (ix + 74, iy + 56, ix + 74, iy + 44))
        # oil flare
        add('<path d="M%d %d q4 -14 0 -20 q-4 6 0 20z" fill="#ff9a52"/>' % (ix + 96, iy + 58))
        add('<circle cx="%d" cy="%d" r="7" fill="#ffcb7a" opacity="0.85"/>' % (ix + 96, iy + 48))
        # missile arcs
        for sx, sy, ex, ey in ((ix + 56, iy + 50, ix + 16, iy + 22), (ix + 70, iy + 54, ix + 140, iy + 26)):
            add('<path d="M%d %d Q%d %d %d %d" fill="none" stroke="#e0603a" stroke-width="2" stroke-dasharray="6 4"/>' % (sx, sy, (sx + ex) // 2, sy - 24, ex, ey))
            add('<circle cx="%d" cy="%d" r="3.2" fill="#ffd0a8"/>' % (ex, ey))
        add('<path d="M%d %d l0 -14 l4 6 l5 2 l-5 3 z" fill="#ffd98f"/>' % (ix + 196, iy + 52))
        # tankers on the water
        for k in range(3):
            tx = ix + 16 + k * 30
            ty = iy + 96 + (k % 2) * 8
            add('<rect x="%d" y="%d" width="18" height="5" rx="2" fill="#6f668f"/>' % (tx, ty))
            add('<rect x="%d" y="%d" width="6" height="4" fill="#8b81ab"/>' % (tx + 11, ty - 4))
            add('<path d="M%d %d h-14" stroke="#5b5379" stroke-width="1"/>' % (tx + 4, ty + 5))
        band("QESHM \u00b7 US STRIKE \u00b7 HORMUZ", "KUWAIT REPELS \u00b7 BAHRAIN HIT AGAIN", "#b3402e", "#ffffff", "#f7d9cd")
    else:
        add('<rect x="%d" y="%d" width="%d" height="128" fill="#241f2e"/>' % (ix, iy, w))
        add('<circle cx="%d" cy="%d" r="27" fill="#ff5f8f"/>' % (ix + w // 2, iy + 58))
        for k in range(4):
            add('<rect x="%d" y="%d" width="%d" height="3" fill="#241f2e"/>' % (ix + w // 2 - 27, iy + 46 + k * 8, 54))
        for k, bh in enumerate((44, 66, 32, 58, 38, 26)):
            bx = ix + 8 + k * 44
            if bx + 30 > ix + w:
                break
            add('<rect x="%d" y="%d" width="30" height="%d" fill="#111620"/>' % (bx, iy + 100 - bh, bh))
            for r in range(4):
                for c in range(3):
                    if (r + c * 2 + k) % 3 == 0:
                        add('<rect x="%d" y="%d" width="5" height="6" fill="%s"/>' % (bx + 5 + c * 9, iy + 102 - bh + r * 11,
                                                                                     ("#ffd166", "#4cc9f0", "#ff5f8f")[(k + r) % 3]))
        add('<rect x="%d" y="%d" width="10" height="26" fill="#ff5f8f" opacity="0.85"/>' % (ix + 24, iy + 74))
        add('<rect x="%d" y="%d" width="8" height="18" fill="#4cc9f0" opacity="0.8"/>' % (ix + 40, iy + 82))
        # palms
        for k in range(3):
            px = ix + w - 76 + k * 24
            add('<path d="M%d %d q-3 -12 1 -20" stroke="#0d1018" stroke-width="2.4" fill="none"/>' % (px, iy + 100, ))
            for a in (-40, -15, 10, 35):
                add('<path d="M%d %d q%d -6 %d -3" stroke="#0d1018" stroke-width="2" fill="none"/>' % (px, iy + 80, 12 if a > 0 else -12, 20 if a > 0 else -18))
        # boulevard + car
        add('<rect x="%d" y="%d" width="%d" height="14" fill="#171a24"/>' % (ix, iy + 100, w))
        add('<path d="M%d %d h40" stroke="#ffd166" stroke-width="1.4" stroke-dasharray="8 7"/>' % (ix + 8, iy + 107))
        add('<path d="M%d %d l16 -7 l20 0 l6 7 z" fill="#e8e2d6"/>' % (ix + w - 96, iy + 100))
        add('<circle cx="%d" cy="%d" r="3" fill="#ffd166"/>' % (ix + w - 92, iy + 100))
        add('<path d="M%d %d h26" stroke="#ffe9b0" stroke-width="1.6" opacity="0.8"/>' % (ix + w - 72, iy + 101))
        band("VICE CITY \u00b7 LAUNCH NIGHT", "\u201cA MASTERPIECE\u201d \u00b7 SERVERS FELL HOURS BEFORE", "#c86a28", "#ffffff", "#ffe9c9")
    return o


def svg():
    o = []
    A = o.append
    A('<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">')
    A('<defs><linearGradient id="sunset" x1="0" y1="0" x2="0" y2="1">'
      '<stop offset="0" stop-color="#f6ddc4"/><stop offset="1" stop-color="#e6dff3"/></linearGradient></defs>')
    A('<rect width="1024" height="1024" fill="%s"/>' % PAPER)
    A('<rect x="0" y="0" width="1024" height="9" fill="%s"/>' % INK)

    # masthead
    A(T(M, 44, "THE DAY", 14, 700, RED, serif=False, spacing="2.6"))
    A(T(W - M, 44, "%d STORIES \u00b7 %d COUNTRIES \u00b7 ALL FROM WEDNESDAY" % (COUNT_STORIES, COUNT_COUNTRIES), 12.5, 700, FAINT, "end", serif=False, spacing="1.5"))
    A(T(W / 2, 112, "Wednesday 18 November 2026", 58, 700, INK, "middle"))
    A('<line x1="%d" y1="132" x2="%d" y2="132" stroke="%s" stroke-width="3"/>' % (M, W - M, INK))
    A('<line x1="%d" y1="138" x2="%d" y2="138" stroke="%s" stroke-width="1"/>' % (M, W - M, INK))

    # leads
    y0 = 152
    for i, L in enumerate(LEADS):
        x = M + i * (LEAD_W + 13)
        A('<rect x="%d" y="%d" width="%d" height="274" fill="#fdfbf4" stroke="#e2dac6"/>' % (x, y0, LEAD_W))
        for ln in lead_ill(L["ill"], x + 10, y0 + 10, LEAD_W - 20):
            A(ln)
        ky = y0 + 156
        A('<circle cx="%d" cy="%d" r="6.5" fill="%s"/>' % (x + 16, ky - 4, L["color"]))
        A(T(x + 27, ky, L["region"], 10.5, 700, L["color"], serif=False, spacing="1.2"))
        tl = wrap_px(L["title"], LEAD_W - 24, GEORGIA_B, 18)
        for j, ln in enumerate(tl[:3]):
            A(T(x + 12, ky + 24 + j * 22, ln, 18, 700))
        by = ky + 24 + 22 * len(tl[:3]) + 2
        for j, ln in enumerate(wrap_px(L["blurb"], LEAD_W - 24, ARIAL, 11.5)[:4]):
            A(T(x + 12, by + j * 14.5, ln, 11.5, 400, DIM, serif=False))

    # numbers strip
    ny = y0 + 296
    A('<rect x="%d" y="%d" width="%d" height="56" fill="#efe8d6"/>' % (M, ny, CW))
    colw = CW // 6
    for i, (num, lbl) in enumerate(NUMBERS):
        nx = M + i * colw
        if i:
            A('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#d8cfb6"/>' % (nx, ny + 8, nx, ny + 40))
        A(T(nx + 14, ny + 23, num, 18.5, 700, RED, serif=False))
        for j, ln in enumerate(lbl.split("\n")):
            A(T(nx + 14, ny + 35 + j * 10, ln, 9.2, 400, DIM, serif=False))

    # cards
    cy = ny + 64
    CARD_H = 76
    for i, (region, topic, color, title, blurb, icon) in enumerate(CARDS):
        r, c = divmod(i, CARD_COLS)
        x = M + c * (CARD_W + 10)
        y = cy + r * (CARD_H + 8)
        A('<rect x="%d" y="%d" width="%d" height="%d" fill="#fdfbf4" stroke="#e2dac6"/>' % (x, y, CARD_W, CARD_H))
        A('<rect x="%d" y="%d" width="3" height="%d" fill="%s"/>' % (x, y, CARD_H, color))
        A('<rect x="%d" y="%d" width="22" height="22" rx="6" fill="%s"/>' % (x + 10, y + 10, color))
        A('<g transform="translate(%d %d)">%s</g>' % (x + 10, y + 10, ICONS.get(icon, "")))
        A(T(x + 38, y + 18, region + " \u00b7 " + topic, 8.4, 700, color, serif=False, spacing="0.8"))
        tl = wrap_px(title, CARD_W - 48, ARIAL_B, 11.6)[:2]
        for j, ln in enumerate(tl):
            A(T(x + 38, y + 29 + j * 12.4, ln, 11.3, 700, INK, serif=False))
        bl = wrap_px(blurb, CARD_W - 20, ARIAL, 9.4)[:2]
        for j, ln in enumerate(bl):
            A(T(x + 10, y + 54 + j * 10.8, ln, 9.3, 400, DIM, serif=False))

    # map + one-liners
    my = cy + 3 * (CARD_H + 8) + 6
    mh = H - my - 50
    mw = MAP_W
    A('<rect x="%d" y="%d" width="%d" height="%d" fill="#e4eddf"/>' % (M, my, mw, mh))
    A('<rect x="%d" y="%d" width="%d" height="19" fill="%s"/>' % (M, my, mw, INK))
    A('<text x="%d" y="%d" font-family="Arial" font-size="8.6" font-weight="700" fill="%s" letter-spacing="1.3">WHERE IT HAPPENED</text>' % (M + 9, my + 13, PAPER))
    A('<text x="%d" y="%d" font-family="Arial" font-size="7.8" font-weight="700" fill="%s" text-anchor="end">%d PLACES · PINS MATCH THE LIST</text>' % (M + mw - 8, my + 13, "#bdb3a0", len(ONELINERS)))
    for poly in CONTINENTS:
        pts = " ".join("%.1f,%.1f" % proj(lo, la, M, my + 19, mw, mh - 19) for lo, la in poly)
        A('<polygon points="%s" fill="#cfc0a2" stroke="#b9a888" stroke-width="0.7"/>' % pts)
    # place the pins, then pull crowded ones apart with leader lines
    spots = []
    for i, (city, lon, lat, country, txt) in enumerate(ONELINERS):
        px, py = proj(lon, lat, M, my + 19, mw, mh - 19)
        spots.append([px, py, px, py])
    for _ in range(60):
        moved = False
        for a in range(len(spots)):
            for b in range(a + 1, len(spots)):
                dx = spots[b][2] - spots[a][2]
                dy = spots[b][3] - spots[a][3]
                d = (dx * dx + dy * dy) ** 0.5
                if d < 15.0:
                    if d < 0.01:
                        dx, dy, d = 1.0, 0.0, 1.0
                    push = (15.0 - d) / 2.0 + 0.4
                    ux, uy = dx / d, dy / d
                    spots[a][2] -= ux * push
                    spots[a][3] -= uy * push
                    spots[b][2] += ux * push
                    spots[b][3] += uy * push
                    moved = True
        for sp in spots:
            sp[2] = min(max(sp[2], M + 9), M + mw - 10)
            sp[3] = min(max(sp[3], my + 26), my + mh - 8)
        if not moved:
            break
    for i, sp in enumerate(spots):
        px, py, dx, dy = sp
        if abs(dx - px) > 0.4 or abs(dy - py) > 0.4:
            A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.8"/>' % (px, py, dx, dy, "#4a4234"))
            A('<circle cx="%.1f" cy="%.1f" r="1.3" fill="%s"/>' % (px, py, "#4a4234"))
        A('<circle cx="%.1f" cy="%.1f" r="6.6" fill="%s"/>' % (dx, dy, INK))
        A('<circle cx="%.1f" cy="%.1f" r="6.6" fill="none" stroke="%s" stroke-width="1.1"/>' % (dx, dy, PAPER))
        A('<text x="%.1f" y="%.1f" font-family="Arial" font-size="7.8" font-weight="700" fill="%s" text-anchor="middle">%d</text>' % (dx, dy + 2.7, PAPER, i + 1))

    ox = M + mw + 14
    ow = W - M - ox
    A(T(ox, my + 12, "ALSO ON WEDNESDAY 18 NOVEMBER", 10, 700, RED, serif=False, spacing="1.1"))
    cols = 2
    colw = ow // cols
    per = (len(ONELINERS) + cols - 1) // cols
    rowh = (mh - 22) / per
    for i, (place, lon, lat, country, rest) in enumerate(ONELINERS):
        c, r = divmod(i, per)
        x = ox + c * colw
        y = my + 25 + r * rowh
        A(T(x, y, "%d" % (i + 1), 8, 700, RED, "end", serif=False))
        A(T(x + 12, y, place + ":", 9.2, 700, INK, serif=False))
        px = x + 14 + sw(place + ":", 9.2, serif=False)
        avail = (colw - (px - x) - 10) * 0.93
        A(T(px, y, clip(rest, avail, ARIAL, 9.2), 9.2, 400, DIM, serif=False))

    # footer
    fy = H - 50
    A('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#cdc2a9"/>' % (M, fy, W - M, fy))
    A(T(M, fy + 13, "SOURCES: BBC, AL JAZEERA, THE GUARDIAN, NPR, DW, UN NEWS, FRANCE 24, ABC \u00b7 18 NOVEMBER 2026", 10, 400, FAINT, serif=False, spacing="0.6"))
    A(T(M, fy + 26, "EVERY STORY HAPPENED OR WAS FIRST REPORTED THAT DAY \u00b7 CONTESTED CLAIMS ARE MARKED AS CLAIMS \u00b7 %d PLOTTED PLACES" % COUNT_PLACES, 10, 700, FAINT, serif=False, spacing="0.6"))
    A('</svg>')
    return "\n".join(o)


html = ('<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
        '@page{size:1024px 1024px;margin:0}'
        'html,body{margin:0;padding:0;width:1024px;height:1024px;overflow:hidden;background:' + PAPER + '}'
        '</style></head><body>' + svg() + '</body></html>')
io.open("news18_final.html", "w", encoding="utf-8").write(html)
print("written", len(html))

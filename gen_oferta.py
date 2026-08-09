#!/usr/bin/env python3
"""Oferta PDF — BURSZTYN mobile bar."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

import os

HERE = os.path.dirname(os.path.abspath(__file__))

F = os.environ.get("FONTS", "/mnt/skills/examples/canvas-design/canvas-fonts")
LOGO = os.path.join(HERE, "assets")
OUT = os.path.join(HERE, "oferta", "BURSZTYN-oferta-2027.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

for n, f in [
    ("Serif", "CrimsonPro-Regular"), ("SerifIt", "CrimsonPro-Italic"),
    ("SerifBd", "CrimsonPro-Bold"), ("Sans", "Outfit-Regular"), ("SansBd", "Outfit-Bold"),
]:
    pdfmetrics.registerFont(TTFont(n, f"{F}/{f}.ttf"))

W, H = A4
M = 56
GRAFIT = (0.102, 0.086, 0.075)
ZLOTO = (0.851, 0.643, 0.255)
BURSZ = (0.784, 0.537, 0.122)
KREM = (0.910, 0.863, 0.784)
KREM_TLO = (0.949, 0.922, 0.867)
ZLOTO_C = (0.541, 0.416, 0.125)
SZARY = (0.42, 0.38, 0.33)

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("BURSZTYN — mobile bar · oferta 2027")
c.setAuthor("BURSZTYN mobile bar")


def bg(col):
    c.setFillColorRGB(*col)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def tracked(txt, x, y, font, size, col, track=0.0, center=False):
    c.setFont(font, size)
    c.setFillColorRGB(*col)
    total = sum(pdfmetrics.stringWidth(ch, font, size) + track for ch in txt) - track
    if center:
        x -= total / 2
    for ch in txt:
        c.drawString(x, y, ch)
        x += pdfmetrics.stringWidth(ch, font, size) + track
    return total


def wrap(txt, font, size, maxw):
    c.setFont(font, size)
    words, lines, cur = txt.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if pdfmetrics.stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def para(txt, x, y, font, size, col, maxw, lead):
    c.setFillColorRGB(*col)
    for ln in wrap(txt, font, size, maxw):
        c.setFont(font, size)
        c.drawString(x, y, ln)
        y -= lead
    return y


def label(num, txt, x, y):
    tracked(num, x, y, "Sans", 8.5, BURSZ, 1.6)
    tracked(txt.upper(), x + 26, y, "Sans", 8.5, SZARY, 1.6)
    c.setStrokeColorRGB(*BURSZ)
    c.setLineWidth(0.7)
    c.line(x, y - 9, x + 34, y - 9)


def rule(x, y, w_, col=BURSZ, lw=0.8):
    c.setStrokeColorRGB(*col)
    c.setLineWidth(lw)
    c.line(x, y, x + w_, y)


# ================= STRONA 1 — OKŁADKA =================
bg(GRAFIT)
logo = ImageReader(f"{LOGO}/bursztyn-pion-ciemne.png")
lw_, lh_ = logo.getSize()
disp_w = 210
disp_h = disp_w * lh_ / lw_
c.drawImage(logo, (W - disp_w) / 2, H - 300, disp_w, disp_h, mask="auto")

tracked("MOBILNY BAR KOKTAJLOWY", W / 2, 372, "Sans", 9, ZLOTO, 3.4, center=True)

c.setFont("Serif", 42)
c.setFillColorRGB(*KREM)
c.drawCentredString(W / 2, 318, "Oferta na sezon")
c.setFont("SerifIt", 42)
c.setFillColorRGB(*ZLOTO)
c.drawCentredString(W / 2, 268, "2027")

rule(W / 2 - 44, 232, 88, ZLOTO, 0.9)

c.setFont("Serif", 13)
c.setFillColorRGB(0.60, 0.55, 0.47)
c.drawCentredString(W / 2, 200, "Wesela · przyjęcia · wydarzenia firmowe")
c.drawCentredString(W / 2, 180, "Łódź i województwo łódzkie")

tracked("PRZYJMUJEMY TRZY REZERWACJE W KWARTALE", W / 2, 96, "Sans", 7.5, (0.42, 0.37, 0.30), 2.6, center=True)
c.showPage()

# ================= STRONA 2 — IDEA =================
bg(KREM_TLO)
label("01", "Idea", M, H - M - 10)

c.setFont("Serif", 33)
c.setFillColorRGB(*GRAFIT)
c.drawString(M, H - M - 66, "Bar, który przyjeżdża")
c.setFont("SerifIt", 33)
c.setFillColorRGB(*ZLOTO_C)
c.drawString(M, H - M - 106, "do Was.")

y = H - M - 156
y = para(
    "Rozkładamy pełnoprawny bar koktajlowy w Waszej sali, plenerze albo na dziedzińcu — "
    "z oświetleniem, szkłem i barmanem, który przez całą noc robi drinki na miejscu. "
    "Nie stawiamy stołu z butelkami. Prowadzimy bar.",
    M, y, "Serif", 12.5, (0.24, 0.21, 0.18), W - 2 * M - 150, 19,
)

y -= 26
c.setFont("SerifIt", 15)
c.setFillColorRGB(*ZLOTO_C)
c.drawString(M, y, "Alkohol kupujecie Wy. Resztą zajmujemy się my.")
y -= 22
y = para(
    "Przygotowujemy dla Was imienną listę zakupową — konkretne butelki i ilości dopasowane "
    "do liczby gości i wybranej karty. Kupujecie je sami, w dowolnym miejscu i po swojej cenie. "
    "Dzięki temu płacicie za alkohol tyle, ile kosztuje w sklepie, a nie z marżą baru.",
    M, y, "Serif", 12.5, (0.24, 0.21, 0.18), W - 2 * M - 150, 19,
)

y -= 46
rule(M, y, W - 2 * M)
y -= 34

col_w = (W - 2 * M - 40) / 2
tracked("W CENIE USŁUGI", M, y, "Sans", 8.5, BURSZ, 1.8)
tracked("PO STRONIE SALI", M + col_w + 40, y, "Sans", 8.5, SZARY, 1.8)
y -= 24

lewo = [
    "Mobilny bar z oświetleniem",
    "Barman lub dwóch, zależnie od pakietu",
    "Szkło koktajlowe i pełny sprzęt",
    "Soki, syropy, toniki, owoce, zioła",
    "Lód na całą noc",
    "Karta drinków w Waszej oprawie",
    "Indywidualna lista zakupowa alkoholu",
    "Konsultacja karty przed weselem",
    "Dojazd do 50 km od Łodzi",
]
prawo = [
    "Alkohol (wg naszej listy)",
    "Dostęp do prądu",
    "Dostęp do wody",
    "Miejsce na bar (ok. 3 × 2 m)",
]

yl = y
for it in lewo:
    c.setFillColorRGB(*BURSZ)
    c.circle(M + 3, yl + 3.4, 1.7, fill=1, stroke=0)
    c.setFont("Serif", 11.5)
    c.setFillColorRGB(0.24, 0.21, 0.18)
    c.drawString(M + 14, yl, it)
    yl -= 20

yr = y
for it in prawo:
    c.setStrokeColorRGB(*SZARY)
    c.setLineWidth(0.9)
    c.circle(M + col_w + 43, yr + 3.4, 1.9, fill=0, stroke=1)
    c.setFont("Serif", 11.5)
    c.setFillColorRGB(0.40, 0.36, 0.31)
    c.drawString(M + col_w + 54, yr, it)
    yr -= 20

c.setFont("SerifIt", 10.5)
c.setFillColorRGB(*SZARY)
c.drawString(M + col_w + 40, yr - 12, "Alkohol pozostaje Waszą własnością")
c.drawString(M + col_w + 40, yr - 28, "przez cały czas trwania przyjęcia.")

tracked("BURSZTYN · MOBILE BAR", M, 44, "Sans", 7.5, (0.62, 0.57, 0.49), 2.2)
c.drawRightString(W - M, 44, "")
tracked("2", W - M - 6, 44, "Sans", 7.5, (0.62, 0.57, 0.49), 0)
c.showPage()

# ================= STRONA 3 — PAKIETY =================
bg(KREM_TLO)
label("02", "Pakiety", M, H - M - 10)

c.setFont("Serif", 33)
c.setFillColorRGB(*GRAFIT)
c.drawString(M, H - M - 66, "Trzy warianty")

pakiety = [
    ("KAMERALNY", "do 60 gości", "2 900 zł", [
        "1 barman", "6 godzin pracy", "4 drinki w karcie",
        "Szkło lub eco-naczynia", "Wszystkie dodatki i lód",
    ]),
    ("PEŁNY", "do 120 gości", "4 300 zł", [
        "2 barmanów", "8 godzin pracy", "6 drinków w karcie",
        "Szkło koktajlowe", "Wszystkie dodatki i lód",
        "Oświetlenie dekoracyjne baru",
    ]),
    ("AUTORSKI", "do 120 gości", "5 400 zł", [
        "2 barmanów", "8 godzin pracy", "Karta tworzona od zera",
        "Drink Pary Młodej z Waszą historią", "Degustacja karty przed weselem",
        "Drukowane karty na stoły", "Szkło premium",
    ]),
]

y0 = H - M - 118
card_h = 196
for i, (nazwa, kogo, cena, punkty) in enumerate(pakiety):
    top = y0 - i * (card_h + 18)
    wyroz = i == 1
    if wyroz:
        c.setFillColorRGB(*GRAFIT)
        c.rect(M, top - card_h, W - 2 * M, card_h, fill=1, stroke=0)
        tc, sc, ac = KREM, (0.62, 0.57, 0.49), ZLOTO
    else:
        c.setStrokeColorRGB(0.80, 0.75, 0.66)
        c.setLineWidth(0.9)
        c.rect(M, top - card_h, W - 2 * M, card_h, fill=0, stroke=1)
        tc, sc, ac = GRAFIT, SZARY, ZLOTO_C

    px = M + 30
    tracked(nazwa, px, top - 40, "Sans", 10, ac, 2.6)
    c.setFont("SerifIt", 12)
    c.setFillColorRGB(*sc)
    c.drawString(px, top - 60, kogo)

    c.setFont("Serif", 30)
    c.setFillColorRGB(*ac)
    c.drawRightString(W - M - 30, top - 48, cena)
    c.setFont("SerifIt", 10)
    c.setFillColorRGB(*sc)
    c.drawRightString(W - M - 30, top - 66, "bez alkoholu")

    yy = top - 92
    for p in punkty:
        c.setFillColorRGB(*ac)
        c.circle(px + 2, yy + 3.2, 1.5, fill=1, stroke=0)
        c.setFont("Serif", 11)
        c.setFillColorRGB(*tc)
        c.drawString(px + 12, yy, p)
        yy -= 17

c.setFont("SerifIt", 10.5)
c.setFillColorRGB(*SZARY)
c.drawString(M, 76, "Każda kolejna godzina: 350 zł. Dojazd powyżej 50 km od Łodzi: 2 zł za kilometr.")
c.drawString(M, 60, "Rezerwację potwierdza zadatek w wysokości 30% wartości pakietu.")

tracked("BURSZTYN · MOBILE BAR", M, 36, "Sans", 7.5, (0.62, 0.57, 0.49), 2.2)
tracked("3", W - M - 6, 36, "Sans", 7.5, (0.62, 0.57, 0.49), 0)
c.showPage()

# ================= STRONA 4 — KARTA I PROCES =================
bg(KREM_TLO)
label("03", "Karta", M, H - M - 10)

c.setFont("Serif", 33)
c.setFillColorRGB(*GRAFIT)
c.drawString(M, H - M - 66, "Przykładowa karta")
c.setFont("SerifIt", 12.5)
c.setFillColorRGB(*SZARY)
c.drawString(M, H - M - 90, "Układamy ją razem z Wami. To punkt wyjścia, nie zamknięta lista.")

karta = [
    ("21:00", "Aperitif", "gin · prosecco · grejpfrut · tymianek"),
    ("23:00", "Sour", "whisky · cytryna · miód · aquafaba"),
    ("00:00", "Północ", "rum · espresso · gorzka czekolada"),
    ("02:00", "Powrót na parkiet", "wódka · ogórek · mięta · limonka"),
    ("—", "Bezsenność", "bez alkoholu · cytrus · rozmaryn · tonik"),
    ("—", "Drink Pary Młodej", "komponowany indywidualnie"),
]

y = H - M - 134
for godz, nazwa, opis in karta:
    c.setFont("Sans", 9)
    c.setFillColorRGB(*BURSZ)
    c.drawString(M, y, godz)
    c.setFont("Serif", 14)
    c.setFillColorRGB(*GRAFIT)
    c.drawString(M + 58, y, nazwa)
    c.setFont("SerifIt", 11)
    c.setFillColorRGB(*SZARY)
    c.drawRightString(W - M, y, opis)
    y -= 12
    rule(M, y, W - 2 * M, (0.84, 0.79, 0.71), 0.5)
    y -= 26

y -= 12
label("04", "Jak to działa", M, y)
y -= 40

kroki = [
    ("Rozmowa", "Poznajemy Wasze wesele: liczbę gości, salę, godziny, styl."),
    ("Karta", "Proponujemy zestaw drinków i dopasowujemy go do Waszych upodobań."),
    ("Rezerwacja", "Umowa i zadatek 30%. Termin jest Wasz."),
    ("Lista zakupowa", "Na miesiąc przed weselem dostajecie dokładny spis alkoholu."),
    ("Wesele", "Przyjeżdżamy 2 godziny wcześniej, rozkładamy bar, pracujemy do końca."),
]
for i, (t, o) in enumerate(kroki, 1):
    c.setFont("Sans", 8.5)
    c.setFillColorRGB(*BURSZ)
    c.drawString(M, y, f"0{i}")
    c.setFont("SerifBd", 12)
    c.setFillColorRGB(*GRAFIT)
    c.drawString(M + 26, y, t)
    c.setFont("Serif", 11)
    c.setFillColorRGB(0.32, 0.29, 0.25)
    c.drawString(M + 118, y, o)
    y -= 22

# stopka kontaktowa
c.setFillColorRGB(*GRAFIT)
c.rect(0, 0, W, 128, fill=1, stroke=0)
sygn = ImageReader(f"{LOGO}/bursztyn-znak-zloty.png")
c.drawImage(sygn, M, 30, 46, 46, mask="auto")

tracked("POROZMAWIAJMY", M + 68, 88, "Sans", 8.5, ZLOTO, 2.4)
c.setFont("Serif", 13)
c.setFillColorRGB(*KREM)
# telefonu celowo nie publikujemy — kontakt mailem i przez Instagram
c.drawString(M + 68, 64, "@barweselnybursztyn")
c.drawString(M + 68, 44, "kontaktbursztyn.barweselny@gmail.com")

c.setFont("SerifIt", 10)
c.setFillColorRGB(0.55, 0.50, 0.43)
c.drawRightString(W - M, 64, "Łódź i województwo łódzkie")
c.drawRightString(W - M, 44, "Trzy rezerwacje w kwartale")

c.showPage()
c.save()
print(f"Zapisano: {OUT}")

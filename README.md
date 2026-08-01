# BURSZTYN — mobile bar

Strona wizytówka mobilnego baru koktajlowego. Łódź i województwo łódzkie.

Kontekst biznesowy, marka i zasady edycji: **[CLAUDE.md](CLAUDE.md)**
Co zrobić, żeby ruszyć: **[START.md](START.md)**

---

## Zawartość

```
index.html                          strona — jeden plik, bez zależności
CLAUDE.md                           kontekst projektu (czytany przez Claude Code)
START.md                            co zrobić, żeby ruszyć — checklista
SPRZET.md                           lista sprzętu z budżetem
OGLOSZENIA.md                       gotowe teksty na OLX i grupy weselne
assets/                             logo: 10 wersji × SVG + PNG
assets/JAK-UZYWAC.txt               który plik logo kiedy
oferta/BURSZTYN-oferta-2027.pdf     oferta dla par młodych
grafiki/olx-*.png                   3 grafiki na ogłoszenia, 1200 × 900
grafiki/karty-zrodlo.html           źródło grafik — edytuj i wyrenderuj ponownie
grafiki/FILOZOFIA-WIZUALNA.md       język wizualny marki
gen_logo.py                         generator plików logo   → assets/
gen_oferta.py                       generator oferty PDF    → oferta/
```

## Podgląd lokalny

Otwórz `index.html` w przeglądarce. Nic nie trzeba instalować.

Albo z serwerem:

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## Publikacja — GitHub Pages

1. Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)**
4. Save

Strona pojawi się pod `https://bartekmerecz-sudo.github.io/bar-weselny/`
w ciągu kilku minut.

W `CNAME` jest domena `bursztyn.barweselny.pl`. Żeby zadziałała, w DNS
domeny musi być rekord `CNAME` z `bursztyn` na `bartekmerecz-sudo.github.io`.
Po propagacji zaznacz **Enforce HTTPS** w ustawieniach Pages.

## Regeneracja plików

```bash
pip install cairosvg fonttools reportlab
python3 gen_logo.py      # → assets/
python3 gen_oferta.py    # → oferta/BURSZTYN-oferta-2027.pdf
```

Skrypty wymagają fontów Crimson Pro i Outfit. Ścieżkę do katalogu z fontami
ustawia zmienna środowiskowa `FONTS`:

```bash
FONTS=~/fonty python3 gen_logo.py
```

`gen_oferta.py` czyta logo z `assets/`, więc uruchamiaj go po `gen_logo.py`.

---

## Zanim opublikujesz

W `index.html` i w ofercie są **zastępcze dane kontaktowe**.
Szukaj `DANE ZASTĘPCZE`. Podmień mail, telefon i nazwę konta na Instagramie.

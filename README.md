# BURSZTYN — mobile bar

Strona wizytówka mobilnego baru koktajlowego. Łódź i województwo łódzkie.

Kontekst biznesowy, marka i zasady edycji: **[CLAUDE.md](CLAUDE.md)**

---

## Zawartość

```
index.html          strona — jeden plik, bez zależności
CLAUDE.md           kontekst projektu (czytany przez Claude Code)
assets/             logo: 10 wersji × SVG + PNG, instrukcja użycia
oferta/             oferta PDF dla par młodych
gen_logo.py         generator plików logo
gen_oferta.py       generator oferty PDF
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

## Regeneracja plików

```bash
pip install cairosvg fonttools reportlab
python3 gen_logo.py      # → logo/
python3 gen_oferta.py    # → PDF oferty
```

Skrypty wymagają fontów Crimson Pro i Outfit — ścieżkę ustawia stała
`FONTS` na górze każdego pliku.

---

## Zanim opublikujesz

W `index.html` i w ofercie są **zastępcze dane kontaktowe**.
Szukaj `DANE ZASTĘPCZE`. Podmień mail, telefon i nazwę konta na Instagramie.

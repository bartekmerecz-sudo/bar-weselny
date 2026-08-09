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
SPRZET.md                           sprzęt: ceny, priorytety, kalkulacja marży
SPRZET-LISTA.md                     wypiska do odhaczania: zakupy, pakowanie, zwijanie
OGLOSZENIA.md                       gotowe teksty na OLX, Google, mail do sal
SALE.md                             sale weselne: skąd wziąć listę, o co pytać, tabela
FACEBOOK.md                         profil firmowy, posty, grupy, odpowiedzi
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
w ciągu kilku minut. Ten adres jest teraz wpisany wszędzie: w `index.html`
(`canonical`, `og:image`, dane strukturalne) i w tekstach ogłoszeń.

## Domena własna — jak ją włączyć

Plik `CNAME` został **usunięty celowo**. Domena `bursztyn.barweselny.pl`
rozwiązuje się na `185.253.212.22`, a GitHub Pages stoi na
`185.199.108–111.153`. Sam plik `CNAME` bez wpisu w DNS psuje oba adresy
naraz: `github.io` przekierowuje na domenę własną, a ta prowadzi w inne
miejsce. Ogłoszenia z takim linkiem byłyby martwe.

Kolejność włączania jest ważna — **najpierw DNS, potem plik**:

**1. W panelu DNS domeny `barweselny.pl` dodaj rekord:**

```
typ: CNAME    nazwa: bursztyn    wartość: bartekmerecz-sudo.github.io
```

W panelu `barweselny.pl` jest **wildcard `*`** — dowolna subdomena rozwiązuje
się na `185.253.212.22`. Dwie konsekwencje:

- **Na plus:** nie musisz nic usuwać. Rekord dla konkretnej nazwy `bursztyn`
  jest bardziej szczegółowy niż `*` i wygrywa. Usuwaj tylko wtedy, gdy panel
  pokazuje **osobny** rekord A dla `bursztyn` — CNAME nie może współistnieć
  z rekordem A dla tej samej nazwy.
- **Groźne:** wildcard sprawia, że `bursztyn.barweselny.pl` **rozwiązuje się
  zawsze**, także przed dodaniem CNAME-a. Samo „adres odpowiada" nie jest
  więc żadnym dowodem. Sprawdzaj **na jaki adres IP**, nie „czy w ogóle".

**2. Sprawdź, czy propagacja zadziałała** (może potrwać do 24 h):

```bash
getent hosts bursztyn.barweselny.pl
```

| Wynik | Znaczenie |
|-------|-----------|
| `185.199.108.153` lub `.109` / `.110` / `.111` | gotowe, przechodź do kroku 3 |
| `185.253.212.22` | **jeszcze nie** — to wildcard, CNAME nie zadziałał lub nie zdążył |

Jeśli przełączysz adresy przy `185.253.212.22`, strona i wszystkie linki
w ogłoszeniach przestaną działać, a DNS nie zgłosi żadnego błędu — domena
będzie prowadzić na Twój drugi hosting.

**3. Dopiero gdy adresy się zgadzają — przywróć plik i podmień adresy:**

```bash
echo "bursztyn.barweselny.pl" > CNAME
grep -rl "bartekmerecz-sudo.github.io/bar-weselny" \
  index.html FACEBOOK.md OGLOSZENIA.md \
  | xargs sed -i 's|bartekmerecz-sudo\.github\.io/bar-weselny|bursztyn.barweselny.pl|g'
```

**4. Zaznacz Enforce HTTPS** w Settings → Pages.

Powrót do wersji na `github.io` to ta sama komenda z odwróconymi stronami
plus `rm CNAME`.

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

## Dane kontaktowe

```
kontaktbursztyn.barweselny@gmail.com
@barweselnybursztyn
```

**Telefon nie jest publikowany celowo** — kontakt idzie mailem i przez Instagram.
W stopce `index.html` jest zakomentowany link `tel:`, gotowy do odkomentowania,
jeśli decyzja się zmieni.

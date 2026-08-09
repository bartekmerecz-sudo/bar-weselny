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
GDZIE-KUPIC.md                      trzy wyjazdy po sprzęt, sklepy i linki
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

## Domena własna — do wykupienia

**Adres produkcyjny to dziś `bartekmerecz-sudo.github.io/bar-weselny`**
i jest wpisany wszędzie: w `index.html` (`canonical`, `og:image`, dane
strukturalne) oraz w tekstach ogłoszeń w `FACEBOOK.md` i `OGLOSZENIA.md`.

### Czego tu wcześniej nie było, a jest ważne

Projekt od początku zakładał adres `bursztyn.barweselny.pl` — plik `CNAME`
zawierał tę wartość, a zaślepka maila to było `kontakt@bursztynbar.pl`.
Sprawdzone w sierpniu 2026: **`barweselny.pl` nie należy do nas.** Domena
jest zaparkowana na AfterMarket.pl (`ns1/ns2.aftermarket.pl`, MX na
`blackhole.aftermarket.pl`, wildcard na adres parkingowy `185.253.212.22`)
i na koncie widnieje „Brak zarejestrowanych domen".

Dlatego plik `CNAME` został usunięty i nie należy go przywracać z tą wartością.

### Kandydatka: `bursztynbar.pl`

Sprawdzona przez zapytanie o rekordy NS — brak delegacji, czyli
**prawdopodobnie wolna**. To sygnał, nie dowód: pewność daje tylko wyszukiwarka
rejestratora albo WHOIS w [dns.pl](https://www.dns.pl/).

Zajęta jest `barbursztyn.pl` (`ns1.ibc.pl`). Bez delegacji, czyli też
prawdopodobnie wolne: `bursztyn-bar.pl`, `bursztynbar.com.pl`,
`bursztynkoktajle.pl`, `barweselnybursztyn.pl`.

Koszt rejestracji `.pl` to zwykle 10–80 zł za pierwszy rok i 60–120 zł
za kolejne.

### Po wykupieniu — kolejność ma znaczenie

**Najpierw DNS, potem plik `CNAME`.** Odwrotnie zabijesz oba adresy naraz:
`github.io` zacznie przekierowywać na domenę, która jeszcze nie prowadzi
do GitHuba.

**1. W panelu rejestratora ustaw rekordy.** Dla domeny głównej to **cztery
rekordy A** (nie CNAME — CNAME dla domeny głównej jest niedopuszczalny):

```
@  A  185.199.108.153
@  A  185.199.109.153
@  A  185.199.110.153
@  A  185.199.111.153
```

Dodatkowo dla `www`, jeśli chcesz, żeby działało: `www CNAME bartekmerecz-sudo.github.io`

> **Najpierw usuń parkingowy rekord A.** AfterMarket po rejestracji sam
> wstawia do strefy rekord `@ A 185.253.212.22` — swój parking. Sprawdzone
> na `bursztynbar.pl` zaraz po zakupie: delegacja poszła na `ns1/ns2.aftermarket.pl`,
> a `@` wskazywał na parking.
>
> Ten rekord trzeba **usunąć**, nie tylko dodać cztery nowe obok. Pięć
> rekordów A dla tej samej nazwy to round robin — przeglądarka losuje jeden
> z pięciu adresów, więc strona działałaby w czterech przypadkach na pięć,
> a w piątym pokazywała parking. Taki błąd jest wredny, bo wygląda
> na „czasem nie działa", nie na błąd konfiguracji.
>
> Jeśli domena ma włączoną stronę parkingową albo sprzedażową, wyłącz ją
> najpierw — inaczej panel może wstawić rekord ponownie.

**2. Sprawdź propagację** (do 24 h):

```bash
getent hosts bursztynbar.pl
```

| Wynik | Znaczenie |
|-------|-----------|
| `185.199.108–111.153` | gotowe, przechodź do kroku 3 |
| cokolwiek innego albo brak | jeszcze nie |

**3. Dopiero wtedy przywróć plik i podmień adresy w 14 miejscach:**

```bash
echo "bursztynbar.pl" > CNAME
grep -rl "bartekmerecz-sudo.github.io/bar-weselny" \
  index.html FACEBOOK.md OGLOSZENIA.md \
  | xargs sed -i 's|bartekmerecz-sudo\.github\.io/bar-weselny|bursztynbar.pl|g'
```

Komenda jest sprawdzona na kopii plików — przełącza wszystkie wystąpienia,
a adresy absolutne wychodzą jako `https://bursztynbar.pl/`, bez zostawionego
`/bar-weselny/`. Powrót to ta sama komenda z odwróconymi stronami plus `rm CNAME`.

**4. Settings → Pages → Custom domain** → wpisz domenę → Save →
zaznacz **Enforce HTTPS**, gdy przycisk się odblokuje.

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

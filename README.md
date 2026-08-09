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

## Domena własna — jak ją włączyć

Plik `CNAME` został **usunięty celowo**. Domena `bursztyn.barweselny.pl`
rozwiązuje się na `185.253.212.22`, a GitHub Pages stoi na
`185.199.108–111.153`. Sam plik `CNAME` bez wpisu w DNS psuje oba adresy
naraz: `github.io` przekierowuje na domenę własną, a ta prowadzi w inne
miejsce. Ogłoszenia z takim linkiem byłyby martwe.

Kolejność włączania jest ważna — **najpierw DNS, potem plik**:

**Gdzie jest panel.** Domena stoi na serwerach nazw `ns1.aftermarket.pl`
i `ns2.aftermarket.pl`, czyli strefą DNS zarządza **AfterMarket.pl** —
tam się logujesz i tam dodajesz rekord.
Instrukcja producenta: [Jak dodać rekord A, MX, TXT albo CNAME do domeny](https://www.aftermarket.pl/pomoc/pl/domeny/dns/jak_dodac_rekord_a_mx_txt_albo_cname_do_domeny.htm)

**0. Najpierw sprawdź, czy domena jest na Twoim koncie.** Stan strefy
wygląda na parking, nie na działającą konfigurację:

```
NS  → ns1.aftermarket.pl, ns2.aftermarket.pl
MX  → blackhole.aftermarket.pl      (poczta nigdzie nie trafia)
*   → 185.253.212.22                (adres parkingowy AfterMarketu)
```

AfterMarket jest też giełdą domen, więc taki zestaw rekordów mają zarówno
domeny kupione i nieskonfigurowane, jak i **domeny wystawione na sprzedaż**.
Jeśli `barweselny.pl` nie ma na liście Twoich domen po zalogowaniu, nie da
się dodać rekordu i trzeba wybrać inną drogę.

**1. W panelu AfterMarketu dodaj rekord:**

| Pole w panelu | Wartość |
|---|---|
| Typ | `CNAME` |
| Nazwa hosta | `bursztyn` |
| Wartość / cel | `bartekmerecz-sudo.github.io` |
| TTL | domyślny |

Rekord dodajesz przyciskiem **„Dodaj wpis DNS ręcznie"** albo **„Dodaj nowy
wpis DNS"**, zależnie od tego, czy strefa ma już jakieś rekordy.

Dwa ograniczenia AfterMarketu, oba nas nie blokują:
CNAME **można ustawić tylko dla subdomeny**, nie dla domeny głównej — a my
kierujemy subdomenę `bursztyn`, więc jest dobrze. Drugie: CNAME nie może
istnieć obok rekordu **A dla tej samej nazwy** — jeśli panel pokaże osobny
rekord A dla `bursztyn`, usuń go najpierw. Wildcard `*` zostaw.

Jeśli domena ma włączony parking albo stronę sprzedażową, wyłącz je —
inaczej panel może nadpisywać Twoje rekordy.

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
będzie prowadzić na parking AfterMarketu.

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

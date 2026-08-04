# BURSZTYN — mobile bar

Kontekst projektu dla Claude Code. Przeczytaj przed wprowadzaniem zmian.

---

## Czym to jest

Strona wizytówka mobilnego baru koktajlowego obsługującego wesela i przyjęcia
w Łodzi i województwie łódzkim. Firma dopiero startuje — nie ma jeszcze
klientów ani zdjęć z realizacji.

**Jedyne zadanie strony:** doprowadzić parę młodą do wysłania zapytania
o termin na sezon 2027.

Właściciel pracuje na etacie w IT, barmanem był wcześniej (3 lata),
ma kurs barmański I stopnia. Firma jest działalnością dodatkową,
prowadzoną w weekendy.

---

## Ograniczenia, które kształtują treść

### Model alkoholowy — nie zmieniaj tego przekazu

Klient kupuje alkohol sam. Firma świadczy **wyłącznie usługę barmańską**
(sprzęt, obsługa, składniki bezalkoholowe, lód, szkło).

To nie jest wybór marketingowy, tylko prawny. Sprzedaż alkoholu wymagałaby
zezwolenia (ustawa o wychowaniu w trzeźwości, art. 18); sprzedaż bez zezwolenia
podlega karze z art. 43. Dodatkowo działalność nierejestrowana wyklucza
działalność wymagającą zezwoleń.

**Nigdy nie pisz na stronie, że firma sprzedaje, dostarcza albo zapewnia alkohol.**
Poprawne sformułowania: "alkohol kupujecie Wy", "przygotowujemy listę zakupową",
"alkohol pozostaje Waszą własnością".

### Limit przychodu — stąd komunikat o trzech rezerwacjach

Działalność nierejestrowana, limit 10 813,50 zł przychodu na kwartał (2026).
Przy cenach pakietów daje to maksymalnie 2–3 zlecenia kwartalnie.

Komunikat "trzy rezerwacje w kwartale" jest prawdziwy i jednocześnie
buduje pozycjonowanie premium. Zostaw go.

### Brak zdjęć

Sesja stylizowana jeszcze się nie odbyła. Strona jest zaprojektowana tak,
żeby działać bez fotografii — typografia i kolor niosą całość.

**Nie dodawaj zdjęć stockowych.** Fałszywe zdjęcia z wesel, których nie było,
to problem wiarygodności, nie estetyki. Miejsca na przyszłe zdjęcia są
oznaczone komentarzem `<!-- MIEJSCE NA ZDJĘCIE -->`.

---

## Identyfikacja wizualna

### Paleta

| Nazwa     | Hex       | Zastosowanie                          |
|-----------|-----------|---------------------------------------|
| Grafit    | `#1A1613` | tło główne, tekst na jasnym           |
| Grafit ciemny | `#12100E` | tło strony (głębsze niż logo)     |
| Złoto     | `#D9A441` | kontur znaku, akcenty na ciemnym      |
| Bursztyn  | `#C8891F` | wypełnienie kieliszka, kreski         |
| Krem      | `#E8DCC8` | tekst na ciemnym tle                  |
| Krem tło  | `#F2EBDD` | jasne sekcje (nigdy czysta biel)      |
| Stonowany | `#8A7B62` | teksty drugorzędne                    |

Czysta biel jest zakazana — przy złocie wygląda tanio.

### Typografia

- **Crimson Pro** — nagłówki, logotyp, treść (szeryfowy)
- **Outfit** — etykiety, podpisy, elementy techniczne (bezszeryfowy)

Oba darmowe, Google Fonts, pełna obsługa polskich znaków.
Etykiety zawsze wersalikami z dużym światłem międzyliterowym.

### Znak

Kieliszek rysowany jedną linią (monoline) z bursztynowym wypełnieniem
do poziomu 1/3 czaszy. Wypełnienie łączy nazwę ze znakiem — bez niego
to dowolny bar. W wersji jednokolorowej poziom płynu to kreska, nie plama.

Pliki w `assets/`. Wersja pozioma do nagłówków, sygnet do awatarów,
mono do haftu i pieczątek.

---

## Oferta

| Pakiet     | Goście | Cena     | Zakres                                    |
|------------|--------|----------|-------------------------------------------|
| Kameralny  | do 60  | 2 900 zł | 1 barman, 6 h, 4 drinki                   |
| Pełny      | do 120 | 4 300 zł | 2 barmanów, 8 h, 6 drinków, oświetlenie   |
| Autorski   | do 120 | 5 400 zł | karta od zera, degustacja, drink pary     |

Ceny **bez alkoholu** — zawsze to zaznaczaj przy cenie.
Dodatkowa godzina 350 zł. Dojazd powyżej 50 km od Łodzi: 2 zł/km.
Zadatek 30% potwierdza rezerwację.

### Karta jako oś nocy

Drinki są indeksowane godzinami (21:00 aperitif → 02:00 powrót na parkiet).
To sygnaturowy element strony — kolejność niesie realną informację,
nie jest dekoracją. Nie zamieniaj na zwykłą listę.

---

## Stan projektu

### Zrobione
- [x] Nazwa, znak, paleta, typografia
- [x] Pliki logo (10 wersji, SVG + PNG)
- [x] Oferta PDF dla par młodych
- [x] Strona — `index.html`
- [x] Dane kontaktowe na stronie i w ofercie PDF (mail + Instagram, bez telefonu)

### Do zrobienia
- [ ] Sesja stylizowana z fotografem → pierwsze zdjęcia
- [ ] Instagram @barweselnybursztyn (konto firmowe)
- [ ] Wzór umowy z zadatkiem
- [ ] Szablon listy zakupowej alkoholu
- [ ] Książeczka sanepidowska
- [ ] Ubezpieczenie OC (sprawdzić wyłączenia alkoholowe w OWU)

### Dane kontaktowe — aktualne

W `index.html` są prawdziwe dane. Nie zastępuj ich zaślepkami:

```
kontaktbursztyn.barweselny@gmail.com
@barweselnybursztyn        → instagram.com/barweselnybursztyn
```

**Telefonu nie publikujemy celowo.** Kontakt idzie mailem i przez Instagram —
zapytanie na piśmie od razu zawiera datę, liczbę gości i miejsce, więc
odpowiedź może być konkretna. Nie dodawaj numeru na stronę bez wyraźnej prośby.

W stopce `index.html` został zakomentowany link `tel:` gotowy do odkomentowania,
jeśli decyzja się zmieni. Zostaw ten komentarz na miejscu.

Te same dane są w stopce oferty PDF (`gen_oferta.py`, sekcja „POROZMAWIAJMY").
Zmieniasz jedno — zmień oba i przegeneruj PDF.

---

## Techniczne

Jeden plik `index.html`, bez frameworków, bez build stepu.
Fonty z Google Fonts CDN. Znak wbudowany jako SVG inline.

Hosting: GitHub Pages (Settings → Pages → Deploy from branch → main).

### Zasady przy zmianach

- Nie dodawaj zależności ani narzędzi budowania. Ma zostać jednoplikowe.
- Zachowaj `prefers-reduced-motion` — animacja nalewania musi dać się wyłączyć.
- Zachowaj widoczny focus na klawiaturze.
- Testuj na szerokości 360 px — większość par ogląda na telefonie.
- Kontrast tekstu minimum 4.5:1.

### Ton tekstów

Zwracaj się per "Wy" do pary młodej. Krótkie zdania. Bez marketingowego
napuszenia, bez wykrzykników, bez "wyjątkowy" i "niezapomniany".
Konkret zamiast obietnicy: "przyjeżdżamy 2 godziny wcześniej" zamiast
"zadbamy o każdy szczegół".

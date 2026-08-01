# START — co zrobić, żeby ruszyć

Stan na 1 sierpnia 2026. Cel: mieć pierwsze zapytania na sezon 2027.

---

## Najważniejsze: kalendarz nie czeka

Pary rezerwują usługi weselne **12–18 miesięcy przed terminem**. Wesela 2027
odbędą się głównie w czerwcu–wrześniu 2027. To znaczy, że decyzje o wyborze
baru zapadają **jesienią 2026 i zimą 2026/27**.

Masz około **dwóch–trzech miesięcy**, żeby być widocznym, zanim ruszy główna fala.
Targi ślubne w Łodzi to styczeń–luty — jeśli chcesz tam być ze zdjęciami,
sesja musi się odbyć do października.

```
sie 2026   dane kontaktowe, strona online, Instagram, OLX     ← jesteś tutaj
wrz 2026   sprzęt, próbne przyjęcie u znajomych
paź 2026   SESJA STYLIZOWANA — pierwsze zdjęcia
lis–gru    grupy weselne, Wizytówka Google, pierwsze zapytania
sty–lut    targi ślubne, szczyt rezerwacji
mar–maj    domykanie terminów, degustacje
cze–wrz    sezon 2027
```

---

## Krok 1 — Dane kontaktowe (dziś, 1–2 h)

Bez tego strona jest atrapą. W `index.html` i w PDF-ie są zaślepki.

- [ ] **Numer telefonu.** Osobna karta prepaid albo eSIM na firmę. Nie mieszaj
      z prywatnym — będziesz odbierał w pracy.
- [ ] **Mail.** Domena `bursztyn.barweselny.pl` jest już w `CNAME`.
      Jeśli masz do niej dostęp, ustaw `kontakt@`. Jeśli nie — Gmail
      `bursztyn.bar@gmail.com` na start wystarczy, tylko konsekwentnie.
- [ ] **Instagram `@bursztyn.bar`** — konto firmowe. Awatar:
      `assets/bursztyn-sygnet-ciemne.png`.
- [ ] Podmień wszystkie trzy w `index.html` (szukaj `DANE ZASTĘPCZE`)
      i przegeneruj PDF: `python3 gen_oferta.py`.
- [ ] Włącz GitHub Pages (Settings → Pages → main → / root).

**Nie publikuj strony przed podmianą.** Martwy telefon na stronie kosztuje
więcej niż brak strony.

## Krok 2 — Zdjęcia (wrzesień–październik)

To jest twoje wąskie gardło, nie sprzęt i nie strona. Żadna para nie zarezerwuje
baru, którego nie widziała. Strona jest zaprojektowana tak, żeby działać bez
zdjęć, ale bez nich konwersja będzie niska.

Najtańsza droga to **barter**: fotograf ślubny startujący w 2026 potrzebuje
portfolio dokładnie tak jak ty. Szukaj w grupach „sesje stylizowane łódzkie",
„fotografia ślubna Łódź — współpraca". Typowa ekipa do sesji: fotograf,
florysta, cukiernik, wypożyczalnia dekoracji, para modeli. Każdy wnosi swoje,
nikt nie płaci.

Co musisz mieć na zdjęciach:
- bar rozłożony, wieczorem, z oświetleniem (kadr szeroki — to zdjęcie z hero)
- ręce nad shakerem, ruch, rozlewanie
- trzy–cztery drinki z karty, każdy osobno, na ciemnym tle
- ty za barem — para kupuje człowieka, nie mebel
- detal: lód, skórka cytrusa, szkło pod światło

Do czasu sesji używaj grafik z `assets/` — logo i typografia niosą markę.
**Nie wstawiaj stocków.** Zdjęcie z wesela, którego nie było, to problem
wiarygodności, nie estetyki.

## Krok 3 — Sprzęt i próba (wrzesień)

Lista z cenami i priorytetami: **[SPRZET.md](SPRZET.md)**.

Zanim wydasz pełny budżet, zrób **jedno przyjęcie testowe** — urodziny
u znajomych, 30 osób, po kosztach. Dowiesz się rzeczy, których nie da się
przewidzieć: ile realnie schodzi lodu, jak długo rozkładasz bar, czy dajesz
radę sam przy 60 osobach, co się tłucze w transporcie.

## Krok 4 — Formalności

- [ ] **Orzeczenie lekarskie do celów sanitarno-epidemiologicznych**
      (potocznie „książeczka sanepidowska"). Badanie + wpis, ok. 100–150 zł.
      Musi mieć każdy, kto pracuje za barem — także drugi barman.
- [ ] **Zadzwoń do PSSE w Łodzi** i zapytaj wprost: czy mobilny bar koktajlowy
      przy działalności nierejestrowanej wymaga zatwierdzenia zakładu.
      Odpowiedź bywa różna w różnych powiatach — chcesz to wiedzieć przed
      pierwszym weselem, nie w jego trakcie. Zapytaj też o wymóg trzech
      pojemników na mycie szkła i o dostęp do wody bieżącej.
- [ ] **OC z rozszerzeniem na organizację imprez.** Czytaj wyłączenia w OWU —
      wiele polis wyłącza szkody powstałe „w związku ze spożyciem alkoholu",
      co przy weselu wycina połowę sensu polisy. Pytaj o to na piśmie.
- [ ] **Wzór umowy z zadatkiem.** Musi zawierać: termin i godziny, adres,
      liczbę gości, pakiet, kwotę i termin zadatku, zasady odwołania po obu
      stronach, zapis że alkohol zapewnia i pozostaje właścicielem Zamawiający.
      Zadatek (art. 394 k.c.) działa w obie strony — przy twojej rezygnacji
      oddajesz podwójnie. To celowe, buduje zaufanie, ale musisz to rozumieć.
- [ ] **Ewidencja sprzedaży** — przy działalności nierejestrowanej wystarczy
      uproszczona, prowadzona na bieżąco. Zwykły arkusz: data, kwota, narastająco.
- [ ] **Polityka prywatności na stronie**, jeśli zbierasz dane z formularza.
      Teraz jest tylko `mailto:`, więc temat jest mały, ale wróci przy umowach.

## Krok 5 — Dystrybucja (od października)

Gotowe teksty: **[OGLOSZENIA.md](OGLOSZENIA.md)**.

Kolejność ma znaczenie — od najtańszego do najdroższego:

1. **Wizytówka Google (Profil Firmy)** — darmowa, daje wyniki w „bar mobilny Łódź".
   Wymaga adresu lub obszaru działania; wybierz obszar, nie adres domowy.
2. **OLX** — kategoria Usługi → Ślub i wesele. Trzy ogłoszenia, patrz OGLOSZENIA.md.
3. **Grupy na Facebooku** — „Wesele 2027", „Panny Młode łódzkie", giełdy terminów.
   Większość ma wyznaczony dzień na ogłoszenia. Złam to raz i wylatujesz.
4. **Instagram** — nie sprzedaje bezpośrednio, ale każda para sprawdzi profil
   przed napisaniem. Pusty profil = brak zapytania. Minimum 9 postów przed
   uruchomieniem reklamy gdziekolwiek.
5. **Sale weselne** — najlepsze źródło. Sala poleca cię parze, bo ty nie
   konkurujesz z jej barem (nie sprzedajesz alkoholu). Obdzwoń 15 sal
   w promieniu 50 km, zapytaj o zasady wnoszenia własnego alkoholu i o to,
   czy przyjmują zewnętrznych barmanów. Przy okazji dowiesz się, które sale
   mają wyłączność — to informacja, której potrzebujesz i tak.
6. **Targi ślubne** (styczeń–luty) — stoisko 800–2 500 zł. Idź dopiero
   ze zdjęciami i wydrukowaną ofertą.

---

## Do przemyślenia, zanim podpiszesz pierwszą umowę

### Limit przychodu zderzy się z sezonem

Limit działalności nierejestrowanej to 10 813,50 zł przychodu na kwartał.
Zestaw to z cennikiem:

| Kombinacja w kwartale        | Przychód  | Mieści się? |
|------------------------------|-----------|-------------|
| 3 × Kameralny                | 8 700 zł  | tak         |
| 2 × Pełny                    | 8 600 zł  | tak         |
| 1 × Autorski + 1 × Pełny     | 9 700 zł  | tak         |
| 2 × Autorski                 | 10 800 zł | tak, o 13 zł|
| 2 × Pełny + 1 × Kameralny    | 11 500 zł | **nie**     |
| 3 × Pełny                    | 12 900 zł | **nie**     |

Realnie to **dwa wesela w kwartale**, nie trzy — trzy tylko w najtańszym
wariancie. Dodatkowe godziny i dojazdy powyżej 50 km też wliczają się
do przychodu i zjadają zapas.

Problem jest ostrzejszy, niż wygląda: **80% wesel wypada w III kwartale**.
Limit obetnie cię dokładnie wtedy, kiedy jest praca, a I i IV kwartał
zostaną niewykorzystane.

Trzy wyjścia:
- **Rozłóż terminy.** Bierz maj i wrzesień, nie tylko lipiec–sierpień.
- **Sprzedawaj poza sezonem.** Urodziny, przyjęcia firmowe, sylwester —
  wypełniają I i IV kwartał, gdzie limit stoi pusty. Dlatego w OGLOSZENIA.md
  jest osobne ogłoszenie pod imprezy niewesełne.
- **Zarejestruj działalność przed sezonem 2027.** Ulga na start (6 miesięcy
  bez składek społecznych), potem preferencyjny ZUS przez 24 miesiące.
  Przy 8–10 weselach rocznie to prawdopodobnie i tak nieuniknione.

**Sprawdź u księgowego jedną rzecz:** czy zadatek wpłacony w listopadzie 2026
za wesele w lipcu 2027 liczy się do limitu IV kwartału 2026, czy III kwartału
2027. Od tej odpowiedzi zależy, ile wesel zmieścisz w szczycie sezonu.
Przepisy o limicie mówią o przychodzie należnym, a PIT dla działalności
nierejestrowanej rozlicza się kasowo — to nie jest to samo i warto mieć
to na piśmie, zanim przyjmiesz trzy zadatki naraz.

### Drugi barman to nie drobiazg

Pakiety Pełny i Autorski zakładają dwie osoby. Przy działalności
nierejestrowanej nie zatrudnisz nikogo bez stania się płatnikiem składek.
Najczystsze rozwiązanie: druga osoba wystawia ci rachunek — z własnej
działalności nierejestrowanej albo z firmy. Ustal to i sprawdź jego
orzeczenie sanitarne, zanim sprzedasz pakiet dla 120 osób.

### Policz marżę, zanim uwierzysz w cennik

Rozliczenie jednego wesela w pakiecie Pełny (120 gości) jest w
[SPRZET.md](SPRZET.md#ile-realnie-zostaje). W skrócie: z 4 300 zł zostaje
około 1 800 zł przed podatkiem. To uczciwa stawka za weekend, ale nie
jest to 4 300 zł.

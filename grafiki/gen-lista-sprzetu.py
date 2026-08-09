import pathlib, html, re

FONTS = pathlib.Path("fonts.css").read_text()

# (kategoria, [(nazwa, ilosc, koszt_dolny, flaga)])
ETAP1 = [
 ("Bar", [
   ("Bar ze skrzynek + blat sosnowy", "1 kpl", 600, "wariant tani — bar składany to 1 500–3 500 zł"),
   ("Stół pomocniczy składany 120 cm", "1 szt", 150, ""),
 ]),
 ("Narzędzia — jedno stanowisko", [
   ("Shaker bostoński, dwie blaszki", "2 kpl", 120, ""),
   ("Sitko Hawthorne ×2 + drobne ×1", "3 szt", 80, ""),
   ("Jigger 25/50 ml", "2 szt", 60, ""),
   ("Łyżka barmańska", "2 szt", 50, ""),
   ("Muddler", "1 szt", 30, ""),
   ("Wyciskarka do cytrusów, prasa ręczna", "1 szt", 150, ""),
   ("Deska, nóż, obieraczka do skórki", "1 kpl", 100, ""),
   ("Dozowniki do butelek", "10 szt", 40, ""),
   ("Butelki na syropy 500 ml z dozownikiem", "6 szt", 90, ""),
   ("Mata barmańska antypoślizgowa", "1 szt", 40, ""),
   ("Ścierki lniane", "6 szt", 90, "zużyjesz więcej, niż myślisz"),
 ]),
 ("Lód i chłodzenie", [
   ("Skrzynia termiczna 60–70 l", "2 szt", 400, "NIE OSZCZĘDZAJ"),
   ("Wiadro barmańskie na lód roboczy", "2 szt", 100, ""),
   ("Szufelka do lodu", "2 szt", 60, "nigdy szklanką — szkło w lodzie kończy wesele"),
 ]),
 ("Prąd i światło", [
   ("Przedłużacz bębnowy 25 m, 3 × 1,5 mm²", "1 szt", 120, "NIE OSZCZĘDZAJ"),
   ("Przedłużacz zapasowy 10 m", "1 szt", 50, ""),
   ("Rozgałęziacz z bezpiecznikiem", "2 szt", 60, ""),
   ("Latarka czołowa", "2 szt", 80, "pakujesz się po ciemku"),
   ("Girlanda LED ciepła, IP44", "1 szt", 150, ""),
 ]),
 ("Woda i higiena", [
   ("Pojemnik na wodę czystą 25 l z kranikiem", "1 szt", 100, "bez tego nie zrobisz pleneru"),
   ("Kanister na ścieki 25 l", "1 szt", 80, ""),
   ("Trzy pojemniki do mycia szkła", "1 kpl", 120, "wymóg sanitarny"),
   ("Płyn do dezynfekcji rąk z dozownikiem", "1 szt", 40, ""),
   ("Rękawiczki jednorazowe, ręczniki papierowe", "zapas", 60, ""),
   ("Kosz na odpady + worki", "2 szt", 60, ""),
   ("Apteczka", "1 szt", 60, ""),
 ]),
 ("Transport", [
   ("Skrzynie transportowe 60 l z pokrywą", "4 szt", 320, ""),
   ("Wózek transportowy składany, 100+ kg", "1 szt", 150, ""),
   ("Pasy mocujące", "4 szt", 60, ""),
 ]),
 ("Ubiór", [
   ("Fartuch barmański z haftem", "2 szt", 200, ""),
   ("Koszule robocze, grafitowe", "3 szt", 250, ""),
 ]),
 ("Formalności", [
   ("Orzeczenie do celów sanitarno-epidemiologicznych", "1", 150, "musi mieć każdy za barem"),
   ("OC z rozszerzeniem na organizację imprez", "rok", 450, "czytaj wyłączenia alkoholowe w OWU"),
 ]),
]

ETAP2 = [
 ("Drugie stanowisko i szkło", [
   ("Drugi moduł baru", "1 szt", 1200, ""),
   ("Drugie stanowisko narzędziowe", "1 kpl", 800, ""),
   ("Listwa na butelki (speed rail)", "2 szt", 300, ""),
   ("Pojemniki GN na garnisze z pokrywkami", "6 szt", 100, ""),
   ("Szklanki rocks / old fashioned 300 ml", "80 szt", 500, ""),
   ("Szklanki highball / collins 350 ml", "80 szt", 500, ""),
   ("Kosze zmywarkowe 25-polowe na szkło", "8 szt", 500, "NIE OSZCZĘDZAJ"),
   ("Worek Lewisa + tłuczek do lodu", "1 kpl", 80, ""),
   ("Taśma LED pod blat, bateryjna", "1 szt", 80, ""),
   ("Kufer wyściełany na narzędzia", "1 szt", 200, ""),
 ]),
]

def rows(groups, prefix):
    out, n = [], 0
    for kat, items in groups:
        out.append('<h3 class="kat">%s</h3>' % html.escape(kat))
        out.append('<ul class="lista">')
        for nazwa, ilosc, koszt, flaga in items:
            n += 1
            idd = "%s-%d" % (prefix, n)
            krytyczne = flaga == "NIE OSZCZĘDZAJ"
            nota = ""
            if flaga and not krytyczne:
                nota = '<span class="nota">%s</span>' % html.escape(flaga)
            znak = '<span class="flaga">nie oszczędzaj</span>' if krytyczne else ""
            out.append(
              '<li><input type="checkbox" id="%s" data-koszt="%d"><label for="%s">'
              '<span class="nazwa">%s%s%s</span>'
              '<span class="ilosc">%s</span><span class="cena">%s zł</span>'
              '</label></li>' % (idd, koszt, idd, html.escape(nazwa), znak, nota,
                                 html.escape(ilosc), f"{koszt:,}".replace(",", " ")))
        out.append("</ul>")
    return "\n".join(out), sum(k for _, its in groups for _, _, k, _ in its)

def sp(n):
    return f"{n:,}".replace(",", "\u00a0")

r1, s1 = rows(ETAP1, "a")
r2, s2 = rows(ETAP2, "b")
f1, f2, tot = sp(s1), sp(s2), sp(s1 + s2)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --tlo:#F2EBDD; --karta:#FBF7EE; --linia:#DCCFB4;
  --ink:#241F1A; --przygaszony:#6B6152;
  --akcent:#7A5C18; --bursztyn:#B87A15; --zaznaczone:#EFE3C9;
  --serif:'Crimson',Georgia,serif; --sans:'Outfit',system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --tlo:#12100E; --karta:#1A1613; --linia:#33291C;
    --ink:#E8DCC8; --przygaszony:#9C8D72;
    --akcent:#D9A441; --bursztyn:#C8891F; --zaznaczone:#221B12;
  }
}
:root[data-theme="dark"]{
  --tlo:#12100E; --karta:#1A1613; --linia:#33291C;
  --ink:#E8DCC8; --przygaszony:#9C8D72;
  --akcent:#D9A441; --bursztyn:#C8891F; --zaznaczone:#221B12;
}
body{background:var(--tlo);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.5;-webkit-text-size-adjust:100%;
  padding:0 0 56px}
.wrap{max-width:640px;margin:0 auto;padding:0 18px}

header{padding:34px 0 20px;text-align:center}
.znak{width:46px;height:auto;display:block;margin:0 auto 16px}
h1{font-family:var(--serif);font-weight:400;font-size:clamp(1.6rem,6vw,2.1rem);
  letter-spacing:.02em;line-height:1.15;text-wrap:balance}
.pod{font-size:.84rem;color:var(--przygaszony);margin-top:8px}

.pasek{position:sticky;top:0;z-index:5;background:var(--tlo);
  border-bottom:1px solid var(--linia);padding:12px 0}
.pasek .in{max-width:640px;margin:0 auto;padding:0 18px;
  display:flex;align-items:baseline;gap:14px}
.licznik{font-family:var(--sans);font-size:.72rem;font-weight:600;
  letter-spacing:.14em;text-transform:uppercase;color:var(--przygaszony)}
.suma{margin-left:auto;font-family:var(--serif);font-size:1.32rem;
  font-variant-numeric:tabular-nums;color:var(--ink)}
.suma b{font-weight:400;color:var(--akcent)}
.szyna{height:3px;background:var(--linia);margin-top:10px;overflow:hidden}
.szyna i{display:block;height:100%;width:0;background:var(--bursztyn);
  transition:width .3s ease}

h2{font-family:var(--serif);font-weight:400;font-size:1.5rem;
  margin:38px 0 4px;display:flex;align-items:baseline;gap:10px}
h2 em{font-style:normal;font-family:var(--sans);font-size:.66rem;font-weight:600;
  letter-spacing:.16em;text-transform:uppercase;color:var(--akcent)}
.etap-opis{font-size:.9rem;color:var(--przygaszony);margin-bottom:6px}
.kat{font-family:var(--sans);font-size:.68rem;font-weight:600;
  letter-spacing:.18em;text-transform:uppercase;color:var(--akcent);
  margin:26px 0 8px}

.lista{list-style:none;background:var(--karta);border:1px solid var(--linia)}
.lista li+li{border-top:1px solid var(--linia)}
.lista input{position:absolute;opacity:0;width:0;height:0}
.lista label{display:grid;grid-template-columns:26px 1fr auto auto;
  gap:4px 12px;align-items:baseline;
  padding:14px 14px;min-height:52px;cursor:pointer}
.lista label::before{content:"";grid-row:1/span 2;align-self:center;
  width:19px;height:19px;border:1.5px solid var(--akcent);
  display:block}
.lista input:checked+label{background:var(--zaznaczone)}
.lista input:checked+label::before{background:var(--bursztyn);
  border-color:var(--bursztyn)}
.lista input:checked+label .nazwa{text-decoration:line-through;
  text-decoration-color:var(--przygaszony);color:var(--przygaszony)}
.lista input:focus-visible+label{outline:2px solid var(--akcent);outline-offset:-2px}
.nazwa{font-size:.95rem}
.ilosc{font-family:var(--sans);font-size:.74rem;color:var(--przygaszony);
  white-space:nowrap;font-variant-numeric:tabular-nums}
.cena{font-family:var(--sans);font-size:.86rem;font-variant-numeric:tabular-nums;
  white-space:nowrap;min-width:66px;text-align:right}
.nota{display:block;grid-column:2/-1;font-size:.78rem;
  color:var(--przygaszony);font-style:italic;margin-top:3px}
.flaga{display:inline-block;font-family:var(--sans);font-size:.6rem;font-weight:600;
  letter-spacing:.12em;text-transform:uppercase;
  color:var(--tlo);background:var(--bursztyn);padding:2px 7px;margin-left:8px;
  vertical-align:middle}

.razem{display:flex;align-items:baseline;gap:10px;
  padding:16px 14px;border:1px solid var(--linia);border-top:none;
  background:var(--karta);font-family:var(--sans);font-size:.72rem;
  font-weight:600;letter-spacing:.14em;text-transform:uppercase;
  color:var(--przygaszony)}
.razem span{margin-left:auto;font-family:var(--serif);font-size:1.3rem;
  font-weight:400;letter-spacing:0;text-transform:none;color:var(--ink);
  font-variant-numeric:tabular-nums}

.info{border-left:2px solid var(--bursztyn);padding:2px 0 2px 14px;
  margin:22px 0;font-size:.9rem;color:var(--przygaszony)}
.info strong{color:var(--ink);font-weight:600}
footer{margin-top:40px;padding-top:20px;border-top:1px solid var(--linia);
  font-size:.8rem;color:var(--przygaszony);text-align:center;line-height:1.7}
.reset{background:none;border:1px solid var(--linia);color:var(--przygaszony);
  font-family:var(--sans);font-size:.68rem;font-weight:600;letter-spacing:.14em;
  text-transform:uppercase;padding:9px 16px;margin-top:14px;cursor:pointer}
.reset:hover{border-color:var(--akcent);color:var(--akcent)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

HTML = f"""<title>BURSZTYN — sprzęt do kupienia</title>
<style>
{FONTS}
{CSS}
</style>

<div class="wrap">
<header>
  <svg class="znak" viewBox="0 0 80 84" role="img" aria-label="BURSZTYN">
    <polygon fill="#C8891F" points="22.5,20 57.5,20 40,42"/>
    <path fill="none" stroke="#D9A441" stroke-width="2.6" stroke-linecap="round"
      stroke-linejoin="round" d="M40 42 L8 4 L72 4 L40 42 L40 70 M18 70 L62 70"/>
  </svg>
  <h1>Sprzęt do kupienia</h1>
  <p class="pod">Odhaczaj w sklepie. Zaznaczenia zapisują się w tej przeglądarce.</p>
</header>
</div>

<div class="pasek">
  <div class="in">
    <span class="licznik"><b id="ile">0</b> z <span id="wszystkie">0</span> pozycji</span>
    <span class="suma"><b id="wydane">0</b> / {tot} zł</span>
  </div>
  <div class="szyna"><i id="szyna"></i></div>
</div>

<div class="wrap">

<h2>Etap 1 <em>pierwsze wesele do 60 osób</em></h2>
<p class="etap-opis">Za to zrobisz pakiet Kameralny. Zwraca się na drugim zleceniu.</p>
{r1}
<div class="razem">Etap 1 razem <span>{f1} zł</span></div>

<h2>Etap 2 <em>dokup po pierwszym pakiecie Pełnym</em></h2>
<p class="etap-opis">Nie kupuj tego na zapas. Dopiero gdy sprzedasz wesele na 120 osób.</p>
{r2}
<div class="razem">Etap 2 razem <span>{f2} zł</span></div>

<p class="info"><strong>Kwoty to dolne widełki.</strong> Górne przedziały,
kalkulacja marży i uzasadnienia są w <strong>SPRZET.md</strong> w repo.
Wszystko z tej listy kupisz taniej z drugiej ręki — szczególnie skrzynie,
szkło i bar.</p>

<p class="info"><strong>Coupe 200 ml wypożyczaj</strong>, dopóki nie sprawdzisz,
czy karta ich naprawdę potrzebuje. Wypożyczalnia to około 1 zł za sztukę.</p>

<p class="info"><strong>Trzy rzeczy, które kupisz drugi raz,</strong> jeśli pierwszy
raz wybierzesz najtaniej: przedłużacz bębnowy, kosze na szkło i skrzynia
termiczna. Oznaczone na liście.</p>

<footer>
  BURSZTYN — mobilny bar koktajlowy<br>
  Kolejność zakupów: narzędzia i szkło → bar → oświetlenie → transport i higiena
  <br><button class="reset" id="reset" type="button">Odznacz wszystko</button>
</footer>
</div>

<script>
(function(){{
  var pola = Array.prototype.slice.call(document.querySelectorAll('.lista input'));
  var elIle = document.getElementById('ile');
  var elWyd = document.getElementById('wydane');
  var elSzyna = document.getElementById('szyna');
  document.getElementById('wszystkie').textContent = pola.length;
  var KLUCZ = 'bursztyn-sprzet-v1';

  function zapisz(){{
    try {{
      localStorage.setItem(KLUCZ, JSON.stringify(
        pola.filter(function(p){{ return p.checked; }}).map(function(p){{ return p.id; }})));
    }} catch(e){{}}
  }}
  function wczytaj(){{
    try {{
      var z = JSON.parse(localStorage.getItem(KLUCZ) || '[]');
      pola.forEach(function(p){{ if (z.indexOf(p.id) > -1) p.checked = true; }});
    }} catch(e){{}}
  }}
  function fmt(n){{ return n.toString().replace(/\\B(?=(\\d{{3}})+(?!\\d))/g, ' '); }}
  function odswiez(){{
    var n = 0, zl = 0;
    pola.forEach(function(p){{
      if (p.checked) {{ n++; zl += parseInt(p.dataset.koszt, 10); }}
    }});
    elIle.textContent = n;
    elWyd.textContent = fmt(zl);
    elSzyna.style.width = (pola.length ? (n / pola.length * 100) : 0) + '%';
  }}

  wczytaj();
  odswiez();
  pola.forEach(function(p){{
    p.addEventListener('change', function(){{ zapisz(); odswiez(); }});
  }});
  document.getElementById('reset').addEventListener('click', function(){{
    pola.forEach(function(p){{ p.checked = false; }});
    zapisz(); odswiez();
  }});
}})();
</script>
"""
# encje nie sa dekodowane w <script> i <style>, wiec sprawdzamy,
# ze tam nie ma znakow poza ASCII, i dopiero wtedy escapujemy calosc
for blok in re.findall(r"<(script|style)[^>]*>(.*?)</\\1>", HTML, re.S):
    tresc = blok[1]
    assert tresc.isascii(), "znak poza ASCII w <%s> — encje tam nie zadzialaja" % blok[0]
ASCII = HTML.encode("ascii", "xmlcharrefreplace").decode("ascii")
pathlib.Path("sprzet.html").write_text(ASCII, encoding="ascii")
print("etap1:", s1, "zl | etap2:", s2, "zl | razem:", s1+s2)
print("plik:", pathlib.Path("sprzet.html").stat().st_size, "bajtow")

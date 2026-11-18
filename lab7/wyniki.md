## Zadanie 1

Błąd w app.py w wierszu 21 to klucz sklejany z tekstem zapytania.

| Wejście (klucz) | Liczba wierszy |
|---|---|
| `1234` | 1 |
| `'` | 0 (błąd OperationalError: unrecognized token) |
| `' OR '1'='1` | 4 |
| `' UNION SELECT name, sql FROM sqlite_master WHERE type='table' --` | 2 |
| `' UNION SELECT login, rola\|\|' '\|\|email FROM konta --` | 2 |

Zapytanie po wstawieniu danych dla ataku OR (z trybu diagnostycznego):

`SELECT wlasciciel, sekret FROM sekrety WHERE klucz = '' OR '1'='1'`

Baza ma dwie tabele: `sekrety(klucz, wlasciciel, sekret)` i `konta(login, rola, email)`. Druga tabela to `konta`, a jej zawartość odczytana atakiem UNION to: `admin administrator admin@lab7.example` oraz `anna uzytkownik anna@lab7.example`.

Dane wejściowe zmieniły strukturę zapytania, bo apostrof zamknął napis z kluczem, a dopisana składnia (OR, UNION, komentarz --) stała się częścią wykonywanego polecenia SQL.

## Zadanie 2

Fragment kodu z parametrem:

```python
zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
wiersze = db.execute(zapytanie, (klucz,)).fetchall()
```

Szczegóły wyjątku trafiają teraz do logu serwera (`app.logger.exception`), a użytkownik dostaje ogólny komunikat.

| Wejście (klucz) | Wierszy przed | Wierszy po |
|---|---|---|
| `1234` | 1 | 1 |
| `'` | błąd | 0 |
| `' OR '1'='1` | 4 | 0 |
| `' UNION SELECT name, sql FROM sqlite_master WHERE type='table' --` | 2 | 0 |
| `' UNION SELECT login, rola\|\|' '\|\|email FROM konta --` | 2 | 0 |
| `d'Artagnan` | błąd | 1 |

Wartość parametru nie może zmienić struktury zapytania, bo treść SQL jest kompilowana przed podstawieniem wartości, a wartość przekazana osobno jest traktowana wyłącznie jako dane, łącznie z apostrofem. Parametr nie może zastąpić nazwy tabeli ani kolumny, bo te należą do struktury zapytania, a nie do danych.

## Zadanie 3

Błąd w app.py w wierszu 37 to `eval(wyrazenie)` wykonuje dowolny kod Pythona.

Wyrażenia z kroku 2 (wyniki skrócone):

- `__import__('os').listdir('/etc')` zwróciło listę katalogu /etc (network, passwd, shadow, os-release, hosts i inne)
- `open('/etc/os-release').read()` zwróciło zawartość pliku: NAME="Alpine Linux"
- `__import__('os').getuid()` zwróciło UID procesu: 1000

UID procesu aplikacji: 1000 (zwykły użytkownik, nie root).

Obliczanie zastąpiono własnym parserem (liczba, operator, liczba; regex `re.fullmatch`, limit 100 znaków, bez eval/exec/compile).

| Wejście | Kod HTTP | Wynik po poprawce |
|---|---|---|
| `2+3` | 200 | 5.0 |
| `7 / 2` | 200 | 3.5 |
| `-1.5*4` | 200 | -6.0 |
| `1/0` | 400 | dzielenie przez zero |
| `__import__('os').listdir('/etc')` | 400 | odrzucone |
| `open('/etc/os-release').read()` | 400 | odrzucone |
| `__import__('os').getuid()` | 400 | odrzucone |
| puste pole `?wyrazenie=` | 400 | odrzucone |

Dodatkowo `/kalkulator` bez parametru zwraca 200 i sam formularz.

Lista dozwolonych operacji jest lepsza od blokowania słów jak import, bo przepuszcza tylko jawnie wybrane działania arytmetyczne, a blokowanie słów zawsze da się obejść innym zapisem (np. __import__, open, dostęp przez inny obiekt), bo technicznie rzecz biorąc niebezpiecznych wejść jest nieskończenie wiele.

## Zadanie 1

| Adres | Przed | Po |
|---|---|---|
| /materialy/ | 200, lista plików | 403 |
| /materialy/notatka.txt | 200 | 200 |
| /wewnetrzne/ | 200, lista plików | 403 |
| /wewnetrzne/plan.txt | 200 | 403 |

Wpis z logu:
AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/plan.txt

Options -Indexes wyłącza tylko listę plików, więc plik o znanym adresie nadal jest dostępny, a Require all denied blokuje dostęp do całego katalogu i każdego pliku w nim.

## Zadanie 2

| Próba | Kod |
|---|---|
| /panel/raport.txt bez logowania | 401 |
| /panel/raport.txt, błędne hasło | 401 |
| /panel/raport.txt, poprawne hasło | 200 |
| / bez logowania | 200 |

WWW-Authenticate bez logowania: Basic realm="Laboratorium 5"

Basic przesyła login i hasło zakodowane tylko w base64, które każdy podsłuchujący może odkodować, dlatego hasło w transmisji chroni dopiero HTTPS.

## Zadanie 3

UID procesu CGI: 2, GID: 2 (daemon)

| Plik | Właściciel | Grupa | Prawa | Odczyt przez CGI |
|---|---|---|---|---|
| /lab-data/ogolny.txt | 0 (root) | 2 (daemon) | 640 | treść odczytana |
| /lab-data/poufny.txt | 0 (root) | 2 (daemon) | 600 | odmowa odczytu |

| Żądanie /cgi-bin/uprawnienia.cgi | Kod | UID/GID i odczyty |
|---|---|---|
| przed Basic | 200 | 2/2, ogolny odczytany, poufny odmowa |
| po Basic, bez logowania | 401 | skrypt nie uruchomiony |
| po Basic, poprawne hasło | 200 | bez zmian |

Proces należy do grupy 2, więc czyta ogolny.txt dzięki prawu odczytu dla grupy, a poufny.txt może czytać tylko root.

Użytkownik student istnieje tylko w bazie htpasswd i nie jest kontem systemowym, a skrypt CGI po zalogowaniu nadal działa jako daemon, a nie root, więc logowanie do serwera WWW nie zmienia praw procesu do plików.

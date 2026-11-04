# Laboratorium 5

Pliki własne:
- konfiguracja/dostep.conf - reguły dostępu
- cgi-bin/uprawnienia.cgi - skrypt CGI w Pythonie 3

Baza haseł auth/uzytkownicy nie jest w repozytorium.

Uruchomienie:
docker compose up -d --build web
Strona: http://127.0.0.1:8080/

Utworzenie konta testowego:
docker compose run --rm --no-deps narzedzia -cB /auth/uzytkownicy student

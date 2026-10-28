## Zadanie 1

| Plik | Status |
|---|---|
| dokumenty/budzet.csv | BŁĄD |
| dokumenty/dane.bin | OK |
| dokumenty/harmonogram.txt | BRAK |
| dokumenty/kontakt.txt | OK |
| dokumenty/regulamin.txt | OK |

Skróty SHA-256 tekstów "Ala ma kota." i "Ola ma kota." różnią się na 131 z 256 bitów.

Sumę kontrolną zapisaną obok pliku atakujący może po prostu przeliczyć po podmianie pliku, dlatego trzeba użyć podpisu cyfrowego albo HMAC z tajnym kluczem.

## Zadanie 2

| Test | Wynik |
|---|---|
| anna, Kasztan-2026 | prawda |
| anna, kasztan-2026 | fałsz |
| piotr, Żółw na łące | prawda |
| kasia, Kasztan-2026 | fałsz |

Konta test1 i test2 (to samo hasło) mają różne sole i różne skróty. Weryfikacja obu kont zwraca prawdę.

Sól powoduje, że takie same hasła mają różne skróty, więc nie da się użyć gotowych tablic skrótów ani łamać wielu kont jednocześnie, a liczba iteracji spowalnia sprawdzanie każdego kandydata na hasło.

## Zadanie 3

Znaleziona para: v_oryginał = 7282, v_zmieniony = 1761, h24 = aac6b9.

Liczba wariantów zmienionego dokumentu z h24 równym h24 oryginału (9a8fd6): 0.

Dowolną parę wybieramy spośród 8192 * 8192 = 2^26 kombinacji, co daje średnio 2^26 / 2^24 = 4 kolizje, natomiast przy ustalonym skrócie każdy wariant trafia z prawdopodobieństwem tylko 1/2^24, więc 8192 prób zwykle nie wystarcza.

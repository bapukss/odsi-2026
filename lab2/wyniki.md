# Laboratorium 2 - Kryptografia historyczna

## Zadanie 1 - Cezar

Ranking pięciu najlepszych przesunięć (ocena to udział bajtów 32-126 oraz 9, 10, 13):

| Lp. | k   | Ocena  | Początek odszyfrowania |
|------|-----|--------|------------------------|
| 1    | 230 | 1.0000 | `Wkh#Qljkw#Ihuu`       |
| 2    | 233 | 1.0000 | `The Night Ferry`      |
| 3    | 228 | 0.9948 | `Ymj%Snlmy%Kjww`       |
| 4    | 229 | 0.9948 | `Xli$Rmklx$Jivv`       |
| 5    | 231 | 0.9948 | `Vjg"Pkijv"Hgtt`       |

Wybrane przesunięcie: **k = 233**. Przesunięcia 230 i 233 mają taką samą ocenę 1.0, ale tylko k = 233 daje angielski tekst (The Night Ferry). Dla k = 230 tekst jest wciąż przesunięty o 3 (`Wkh` zamiast `The`), a znaki końca wiersza zamieniły się na `\r`, które również liczą się jako dozwolone, stąd remis.

Entropia histogramu nie rozstrzyga wyboru, ponieważ przesunięcie o k modulo 256 jest permutacją wartości bajtów. Zmienia ono tylko to, której wartości odpowiada dana częstość, a nie same częstości, więc entropia jest identyczna dla wszystkich 256 kandydatów.

## Zadanie 2 - Vigenère

| Test                                                  | Wynik |
|-------------------------------------------------------|-------|
| odszyfrowanie `vigenere.bin` zgodne ze źródłem bajt po bajcie | True  |
| puste dane                                            | True  |
| dane z bajtami 0 i 255                   | True  |

Szyfrowanie `BRAMABRAMABRAMA`:

| Klucz   | Fragment 1   | Fragment 2   | Fragment 3   |
|---------|--------------|--------------|--------------|
| `SZYFR` | `95ac9a9393` | `95ac9a9393` | `95ac9a9393` |
| `KOD`   | `8da1859890` | `869d90918c` | `91968c9c85` |

Powtarzany fragment `BRAMA` ma 5 bajtów, tyle samo co klucz `SZYFR`, więc każde jego wystąpienie zaczyna się w tym samym miejscu klucza i jest szyfrowane identycznie. Przy kluczu `KOD` (3 bajty) kolejne wystąpienia trafiają na inne przesunięcie klucza, więc fragmenty kryptogramu się różnią. Atakujący widzi powtórzenia w kryptogramie, a odległość między nimi zdradza wielokrotność długości klucza.

## Zadanie 3 - RC4

Klucz: **`tat`**

| Poz. | Klucz | Entropia pierwszych 512 B |
|------|-------|---------------------------|
| 1    | `tat` | 4.3910                    |
| 2    | `neg` | 7.4304                    |
| 3    | `mcn` | 7.4512                    |
| 4    | `oxo` | 7.4536                    |
| 5    | `tnx` | 7.4592                    |

- Liczba prób: 17 576 (26³)
- Czas przeszukiwania: 2.35 s
- Entropia całego kryptogramu: 7.9271 bit/bajt
- Entropia całego odszyfrowania: 4.3259 bit/bajt

| Test                                                  | Wynik |
|-------------------------------------------------------|-------|
| dwukrotne RC4 z tym samym kluczem odtwarza wejście    | True  |
| ponowne szyfrowanie `rc4.txt` zgodne z kryptogramem   | True  |
| sensowność tekstu: The Clockmaker's Apprentice      | tak   |

RC4 szyfruje przez XOR ze strumieniem klucza, a XOR z tym samym strumieniem jest operacją odwrotną do siebie. Dlatego ponowne szyfrowanie odtworzy kryptogram dla dowolnego klucza, także błędnego, i potwierdza jedynie spójność implementacji. Ranking entropii mógłby zawieść, gdyby tekst jawny sam miał wysoką entropię (dane skompresowane, zaszyfrowane lub losowe), gdyby próbka była zbyt krótka albo gdyby błędny klucz przypadkiem dał niższą entropię niż poprawny.

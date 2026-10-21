**Zadanie 1**  
ECB: równe bloki 1, 2, 3, 4. CBC: brak równych bloków.  
Po odszyfrowaniu: ECB zgodne z wejściem oraz CBC zgodne z wejściem.  
ECB szyfruje każdy blok niezależnie, więc równe bloki jawne dają równe bloki kryptogramu, a w CBC każdy blok jest przed szyfrowaniem łączony XOR z poprzednim kryptogramem (pierwszy z IV).

**Zadanie 2**  
Puste dane: zgodne, kryptogram 16 B.  
16 B: zgodne, kryptogram 32 B.  
wiadomosc.txt (247 B): zgodne, kryptogram 256 B.  
Dwa szyfrowania z nową solą i IV: kryptogramy różne.  
Sól zmienia klucz wyprowadzany z hasła, a IV zmienia kryptogram przy tym samym kluczu.

**Zadanie 3**  
Top 5: `m` 4.4536, `b` 7.9472, `x` 7.9490, `o` 7.9493, `2` 7.9502  
Znak klucza: `m`  
Pierwszy wiersz: Record 000. The archive contains laboratory notes about symmetric encryption and careful handling of binary files.  
Kluczy jest 36, bo klucz zależy tylko od jednego znaku z 36-znakowego zbioru. Ranking może zawieść dla danych skompresowanych, bo ich entropia jest bliska 8 bitów na bajt, jak przy błędnym kluczu.

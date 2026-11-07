# ctrlX pilot: ST + Python

Prosty test, czy na sterowniku ctrlX da się połączyć program w ST z kodem w Pythonie. Zrobiony na wirtualnym sterowniku ctrlX COREvirtual, bez kupowania licencji.

## Co to robi

Program w ST (ctrlX PLC Engineering) liczy co sekundę i zapisuje wynik w zmiennej `counter`. Skrypt w Pythonie na komputerze loguje się do sterownika przez REST API i odczytuje tę zmienną.

## Co jest w folderze

- `pilot_python.project`: projekt PLC (reszta plików `pilot_python.*` i `LastLoaded.*` to pliki pomocnicze generowane przez PLC Engineering)
- `odczyt_counter.py`: skrypt w Pythonie, który odczytuje `counter`
- `PLC PLC-2.6.5.app`: plik aplikacji PLC do zainstalowania na sterowniku wirtualnym

## Wymagania

- ctrlX WORKS 2.6.x z ctrlX COREvirtual i ctrlX PLC Engineering
- Python 3 z biblioteką `requests` (`python -m pip install requests`)

## Jak uruchomić

1. Uruchom ctrlX COREvirtual w ctrlX WORKS (po 4 godzinach wyłącza się sam).
2. W panelu sterownika (https://192.168.1.1) w Settings, Apps zainstaluj aplikację PLC z pliku `PLC PLC-2.6.5.app`.
3. Otwórz projekt w ctrlX PLC Engineering, w Symbol Configuration zaznacz tylko `counter`.
4. Wykonaj: Online, Reset origin, Build, Clean all, Build, Login, pobierz program, Start.
5. W terminalu uruchom: `python odczyt_counter.py`

Skrypt powinien wypisać kilka kolejnych wartości `counter`, rosnących o 1 na sekundę. Adres sterownika, login i hasło są na górze skryptu.

## Znane problemy

- Zaznaczenie w Symbol Configuration zmiennej `tick` (blok TON) powodowało alarm "License invalid" i wyjątek PLC. Po zaznaczeniu samego `counter` problem znikał. Przyczyny nie ustalono.
- Wirtualny sterownik nie ma czasu rzeczywistego, więc zdarzają się powtórzone odczyty tej samej wartości.

## Co sprawdzono, a czego nie

Sprawdzono:
- ST na ctrlX COREvirtual
- odczyt zmiennej PLC z Pythona przez sieć

Nie sprawdzono:
- zapisu z Pythona do zmiennej PLC
- własnej aplikacji Python lub C++ uruchomionej na samym sterowniku (snap)
- działania na prawdziwym sterowniku ctrlX CORE X3, w tym licencji
- pracy wielu użytkowników naraz

Adresy REST w skrypcie pochodzą z mojej wiedzy i zadziałały w wersji 2.6.5 aplikacji PLC. Przy innych wersjach mogą wymagać poprawki.

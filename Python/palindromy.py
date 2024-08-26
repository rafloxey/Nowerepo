# 1. Pobierz liczbę od użytkownika
liczba = input("Podaj liczbę: ")

# 2. Sprawdź, czy liczba jest palindromem
if liczba == liczba[::-1]:
    print(f"Liczba {liczba} jest palindromem.")
else:
    print(f"Liczba {liczba} nie jest palindromem.")

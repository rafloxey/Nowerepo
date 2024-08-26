def oblicz_procent(liczba, procent): 
    wynik_procentowy = (liczba * procent) / 100
    return wynik_procentowy



liczba = int(input("Podaj liczbę: "))
procent = float(input("Podaj procent: "))

if liczba < 0:
    print("Liczba nie może być ujemna.")
    exit()

if procent < 0 or procent > 100:
    print("Procent nie może być mniejszy od 0 i większy od 100.")
    exit()

wynik = oblicz_procent(liczba, procent)
print(f"Wynik procentowy: {wynik}")
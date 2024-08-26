# 1. Odczytaj liczbę n od użytkownika
n = int(input("Podaj liczbę n: "))

# 2. Iteruj po liczbach od 1 do n
for i in range(1, n + 1):
    # 3. Oblicz kwadrat liczby i
    kwadrat = i * i
    # 4. Wyświetl wynik
    print(f"Kwadrat liczby {i} to {kwadrat}")

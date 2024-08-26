import matplotlib.pyplot as plt

def sito_eratostenesa(limit):
    # Tworzymy listę, gdzie indeksy odpowiadają liczbom, a wartości True oznaczają, że liczba jest pierwsza
    sito = [True] * (limit + 1)
    sito[0] = sito[1] = False  # 0 i 1 nie są liczbami pierwszymi

    # Przechodzimy przez listę i oznaczamy wielokrotności liczb jako False (nie są pierwsze)
    for i in range(2, int(limit ** 0.5) + 1):
        if sito[i]:
            for j in range(i * i, limit + 1, i):
                sito[j] = False

    # Zbieramy wszystkie liczby pierwsze
    liczby_pierwsze = [i for i, is_prime in enumerate(sito) if is_prime]
    return liczby_pierwsze

def zapisz_do_pliku(liczby_pierwsze, filename="liczby_pierwsze.txt"):
    with open(filename, "w") as file:
        for liczba in liczby_pierwsze:
            file.write(f"{liczba}\n")
    print(f"Wyniki zapisano do pliku: {filename}")

def wizualizacja_liczb_pierwszych(liczby_pierwsze, limit):
    plt.figure(figsize=(10, 6))
    plt.plot(liczby_pierwsze, 'ro', markersize=4)
    plt.title(f"Rozkład liczb pierwszych mniejszych niż {limit}")
    plt.xlabel("Indeks liczby pierwszej")
    plt.ylabel("Liczba pierwsza")
    plt.grid(True)
    plt.show()

def liczby_pierwsze_w_zakresie(limit):
    liczby_pierwsze = sito_eratostenesa(limit)
    print(f"Liczby pierwsze mniejsze niż {limit}:")
    print(liczby_pierwsze)

    # Wyświetlenie statystyk
    print(f"\nLiczba znalezionych liczb pierwszych: {len(liczby_pierwsze)}")
    print(f"Suma liczb pierwszych: {sum(liczby_pierwsze)}")

    # Zapis wyników do pliku
    zapisz_do_pliku(liczby_pierwsze)

    # Wizualizacja rozkładu liczb pierwszych
    wizualizacja_liczb_pierwszych(liczby_pierwsze, limit)

# Poproszenie użytkownika o podanie liczby
limit = int(input("Podaj liczbę: "))
liczby_pierwsze_w_zakresie(limit)
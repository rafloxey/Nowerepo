# Liczba podana przez użytkownika
n = int(input("Napisz jak wysoka ma być piramida: "))

# Pętla generująca piramidę
for i in range(n):
    # Drukowanie spacji
    print(" " * (n - i - 1), end="")
    # Drukowanie gwiazdek
    print("*" * (2 * i + 1))

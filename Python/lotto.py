from random import sample

moje_liczby = {8, 12, 22, 48, 7, 33}
lotto_liczby = range(1, 50)
counter = 0 
wylosowane_liczby = set()

while wylosowane_liczby != moje_liczby:
    wylosowane_liczby = set(sample(lotto_liczby, 6))
    counter += 1
    if counter % 1000000 == 0:  # Co milion iteracji
        print(f"Iteracja: {counter}, wylosowane: {wylosowane_liczby}")

print(f"Liczba prób: {counter}")

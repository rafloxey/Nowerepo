def zlicz_samogloski(tekst):
    count = 0
    for litera in tekst:
        if litera in samogloski:
            count += 1
    return count



user_tekst = input("Podaj jakiś tekst: ")
samogloski = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
wynik = zlicz_samogloski(user_tekst)
print("Liczba samogłosek w tekście:", wynik)
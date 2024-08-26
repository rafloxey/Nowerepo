def silnia(user_int):
    silnia_wynik = 1
    for i in range(1, user_int + 1):
        silnia_wynik *= i
        
    return silnia_wynik
    



user_int = int(input("Podaj liczbę naturalną: "))

if user_int < 0:
    print("Liczba nie może być ujemna.")
    exit()
if user_int == 0:
    print("Liczba musi być większa od 0. ")
    exit()
    
wynik = silnia(user_int)
print("Silnia liczby", user_int, "to:", wynik)
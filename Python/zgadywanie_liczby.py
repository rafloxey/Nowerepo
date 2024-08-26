import random

user_int = 0
wylosowana_liczba = random.randint(1, 21)
no_of_attempts = 0

while wylosowana_liczba != user_int:
    user_int = int(input("Zgadnij liczbę  od 1 do 20:  "))
    no_of_attempts += 1
    if user_int < wylosowana_liczba:
        print("Podana liczba jest za mała.")
        
    elif user_int > wylosowana_liczba:
        print("Podana liczba jest za duża.")

        
    else:
        print("Brawo! Zgadłeś liczbę w ", no_of_attempts, " próbach.")
        break
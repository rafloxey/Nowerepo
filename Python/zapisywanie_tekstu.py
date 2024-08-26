plik = "user_text.txt"
user_text = input("Podaj jakiś tekst: ")
plik = open(plik, "a")
plik.write(user_text + "\n")
plik.close()

plik_odczyt = open('user_text.txt', 'r')
plik_odczyt.close()
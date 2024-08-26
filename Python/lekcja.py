# # Poproś użytkownika o wpisanie tekstu
# tekst = input("Wpisz tekst: ")

# # Podziel tekst na słowa
# słowa = tekst.split()

# # Utwórz pusty słownik na przechowywanie liczby wystąpień słów
# licznik_słów = {}

# # Przeiteruj przez słowa i zliczaj wystąpienia
# for słowo in słowa:
#     if słowo in licznik_słów:
#         licznik_słów[słowo] += 1
#     else:
#         licznik_słów[słowo] = 1

# # Wyświetl zawartość słownika
# for słowo, liczba in licznik_słów.items():
#     print(f"{słowo}: {liczba}")

countries_information = {}
countries_information['Polska'] = ('Warszawa', 38)
countries_information['Niemcy'] = ('Berlin', 83)
countries_information['Francja'] = ('Paryz', 57)

def print_country_information(country):
    print('Kraj - ' + country)
    print('Stolica: ' + countries_information[country][0])
    print('Liczba mieszkańców : '+ str(countries_information[country][1]) + ' milionów')


print_country_information('Niemcy')
print()
print_country_information('Polska')
print()
print_country_information('Francja')
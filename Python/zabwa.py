hasło = input("Podaj hasło: ")
lista = []

def litery_w_hasle(hasło):
    lista = []
    for litera in hasło:
        if litera not in lista:
            lista.append(litera)
    return lista

# Wywołanie funkcji i przypisanie wyniku do listy
lista = litery_w_hasle(hasło)
print(lista)
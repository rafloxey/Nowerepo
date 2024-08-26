def liczba_slow(user_tekst):
    slowa = user_tekst.split()
    lista_slow.append(slowa)
    print("Liczba słów w podanym tekście:", len(slowa))

def liczba_zdan(user_tekst):
    zdania = user_tekst.split(".")
    lista_zdan.append(zdania)
    print("Liczba zdań w podanym tekście:", len(zdania))

def srednia_dlugosc_slowa(lista_slow):
    suma_dlugosci = 0
    liczba_slow = 0
    for slowa in lista_slow:
        liczba_slow += len(slowa)
        for slowo in slowa:
            suma_dlugosci += len(slowo)

    if liczba_slow > 0:
        srednia_dlugosc = suma_dlugosci / liczba_slow
    else:
        srednia_dlugosc = 0
    
    return srednia_dlugosc

# Przykład użycia funkcji
user_tekst = input("Podaj tekst: ")
lista_slow = []
lista_zdan = []

liczba_slow(user_tekst)
liczba_zdan(user_tekst)
srednia_dlugosc = srednia_dlugosc_slowa(lista_slow)
print("Średnia długość słowa w podanym tekście:", srednia_dlugosc)
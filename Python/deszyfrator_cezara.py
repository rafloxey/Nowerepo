def deszyfruj_cezara(szyfrogram, k):
    odszyfrowany_tekst = ""

    for znak in szyfrogram:
        # Sprawdź, czy znak jest literą
        if znak.isalpha():
            # Sprawdź, czy litera jest wielka
            if znak.isupper():
                # Przesuń w lewo o k miejsc w alfabecie
                indeks = (ord(znak) - ord('A') - k) % 26 + ord('A')
                odszyfrowany_tekst += chr(indeks)
            else:
                # Przesuń w lewo o k miejsc w alfabecie dla małych liter
                indeks = (ord(znak) - ord('a') - k) % 26 + ord('a')
                odszyfrowany_tekst += chr(indeks)
        else:
            # Jeśli znak nie jest literą, dodaj go bez zmian
            odszyfrowany_tekst += znak

    return odszyfrowany_tekst

# Pobranie danych od użytkownika
szyfrogram = input("Podaj zaszyfrowany tekst: ")
k = int(input("Podaj klucz (liczba miejsc przesunięcia): "))

# Deszyfrowanie i wyświetlanie wyniku
odszyfrowany_tekst = deszyfruj_cezara(szyfrogram, k)
print("Odszyfrowany tekst:", odszyfrowany_tekst)

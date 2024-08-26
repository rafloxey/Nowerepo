def szyfr_cezara(tekst, k):
    zaszyfrowany_tekst = ""

    for znak in tekst:
        # Sprawdzanie, czy znak jest literą
        if znak.isalpha():
            # Ustal, czy znak jest wielką, czy małą literą
            ascii_offset = ord('A') if znak.isupper() else ord('a')
            
            # Przesunięcie znaku o k miejsc w alfabecie
            zaszyfrowany_znak = chr((ord(znak) - ascii_offset + k) % 26 + ascii_offset)
            zaszyfrowany_tekst += zaszyfrowany_znak
        else:
            # Jeśli znak nie jest literą, dodaj go do wyniku bez zmian
            zaszyfrowany_tekst += znak

    return zaszyfrowany_tekst

# Pobranie danych od użytkownika
tekst = input("Podaj tekst do zaszyfrowania: ")
k = int(input("Podaj przesunięcie (k): "))

# Zaszyfrowanie tekstu
zaszyfrowany = szyfr_cezara(tekst, k)

# Wyświetlenie zaszyfrowanego tekstu
print("Zaszyfrowany tekst:", zaszyfrowany)

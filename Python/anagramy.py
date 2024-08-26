def czy_anagram(zdanie1, zdanie2):
    # Usunięcie spacji i przekształcenie na małe litery
    zdanie1 = zdanie1.replace(" ", "").lower()
    zdanie2 = zdanie2.replace(" ", "").lower()
    
    # Sprawdzenie, czy posortowane litery w obu zdaniach są takie same
    if sorted(zdanie1) == sorted(zdanie2):
        print("Podane zdania są anagramami.")
    else:
        print("Podane zdania nie są anagramami.")

# Pobranie danych od użytkownika
zdanie1 = input("Podaj pierwsze zdanie: ")
zdanie2 = input("Podaj drugie zdanie: ")

czy_anagram(zdanie1, zdanie2)


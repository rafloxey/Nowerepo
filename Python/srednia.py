ocena1 = input("Podaj ocenę 1: ")
ocena2 = input("Podaj ocenę 2: ")
ocena3 = input("Podaj ocenę 3: ")

def srednia_ocen(ocena1, ocena2, ocena3):
    if ocena1.isdigit() and ocena2.isdigit() and ocena3.isdigit():
        srednia = (int(ocena1) + int(ocena2) + int(ocena3)) / 3
        return srednia
    else:
        return "Błędne dane. Wpisz liczby."
    
srednia_ocen = srednia_ocen(ocena1, ocena2, ocena3)
print(round(srednia_ocen, 2))
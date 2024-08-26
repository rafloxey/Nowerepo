print("Witaj w kalkulatorze wynagrodzenia")
stawka = int(input("Podaj swoją stawkę w [zł]: "))
godziny = int(input("Podaj ilość przepracowanych godzin: "))

wynagrodzenie_brutto = stawka * godziny

def wynagrodzenie_netto(wynagrodzenie_brutto):
    netto = wynagrodzenie_brutto * 0.85
    return netto

wynagrodzenie_netto = wynagrodzenie_netto(wynagrodzenie_brutto)
panstwo_ukadlo = wynagrodzenie_brutto - wynagrodzenie_netto

print(f"Twoje wynagrodzenie brutto to: {wynagrodzenie_brutto} zł, łączne przepracowane godziny to: {godziny} ")
print(f"Twoje wynagrodzenie netto to: {wynagrodzenie_netto} zł ")
print(f"Panstwo ukradło: {panstwo_ukadlo} zł")
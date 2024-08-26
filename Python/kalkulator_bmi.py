
def pobierz_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Proszę podać poprawną liczbę.")

print("Witaj w kalkulatorze BMI ")
print("Aby obliczyć swoje BMI, podaj wzrost i wagę." )

wzrost = pobierz_float("Podaj swój wzrost w centymetrach: ")
waga = pobierz_float("Podaj swoją wagę w kilogramach: ")

wzrost_m = wzrost / 100

def bmi(wzrost_m, waga):
    bmi_wynik = waga / wzrost_m ** 2
    return bmi_wynik

bmi_wynik = bmi(wzrost_m, waga)
print("Twoje BMI to: ", round(bmi_wynik, 2))
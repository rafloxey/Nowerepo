plik_odczyt = open('user_text.txt', 'rt')
l = 1
for linia in plik_odczyt:
    print(f"linia {l}: {linia}")
    l += 1

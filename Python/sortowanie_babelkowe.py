elements = [7, 3, 1, 2, 5, 8, 12, 4, 16, 9, 13, 10, 11, 6]
size = len(elements)

print("Before sorting:", elements)
counter = 0
for i in range(size):
    
    has_swapped = False  # Ustawienie flagi na False przed rozpoczęciem iteracji
    for j in range(0, size-i-1):
        if elements[j] > elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]
            has_swapped = True  # Jeśli nastąpiła zamiana, ustawiamy flagę na True
            print(elements)
            counter += 1  # Zwiększamy licznik zamian
    if not has_swapped:
        break  # Jeśli w tej iteracji nie było zamiany, kończymy sortowanie

print("After sorting:", elements)
print(counter)
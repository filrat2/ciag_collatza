# -*- coding: utf-8 -*-

# user input
while True:
    try:
        liczba = int(input("Wprowadź liczbę całkowitą z zakresu od 1 do 100: "))
    except ValueError:
        print("Wprowadzony atrybut nie jest liczbą całkowitą.")
        continue
    else:
        break

# first conditions - only integers from 1 to 100
if 1 <= liczba <= 100:
    print(liczba)
else:
    print("Wprowadzono liczbę całkowitą, która nie należy do zakresu 1-100."
          " Działanie programu przerwane.")
    exit()

# define objects (variables)
user_input = liczba
lista = []

if liczba == 1:
    lista.append(liczba)

# while loop with conditions
while liczba != 1:
    if liczba % 2 == 0:  # liczba parzysta
        liczba = int(liczba / 2)
        print(liczba)
        lista.append(liczba)
    else:
        liczba = 3 * liczba + 1
        print(liczba)
        lista.append(liczba)

# summary
print(f"Ciąg Collatza dla liczby {user_input} wymaga {len(lista)} kroków"
      f" z maksymalną osiągniętą wartością {int(max(lista))}.")

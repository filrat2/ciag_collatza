# -*- coding: utf-8 -*-

# user input
liczba = int(input("Wprowadź liczbę całkowitą z zakresu od 1 do 100: "))

# first condition - only numbers from 1 to 100
if liczba < 1 or liczba > 100:
    print("Wprowadzono liczbę całkowitą, która nie należy do zakresu 1-100."
          " Działanie programu przerwane.")
    exit()

if liczba >= 1 and liczba <= 100:
    print(liczba)

# define objects (variables)
user_input = liczba
lista = []

if liczba == 1:
    lista.append(liczba)

# while loop with conditions
while liczba != 1:
    if liczba % 2 == 0:  # liczba parzysta
        liczba = (liczba / 2)
        print(int(liczba))
        lista.append(liczba)
    else:
        liczba = ((3 * liczba) + 1)
        print(int(liczba))
        lista.append(liczba)

# summary
print(f"Ciąg Collatza dla liczby {user_input} wymaga {len(lista)} kroków"
      f" z maksymalną osiągniętą wartością {int(max(lista))}.")

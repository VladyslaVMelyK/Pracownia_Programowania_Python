#random -- Generowanie liczb pseudolosowych. Moduł implementuje generatory liczb pseudolosowych o różnych rozkładach. Umożliwia wybór losowej liczby całkowitej z zadanego zakresu jak również losowego elementu z podanej sekwencji przy założeniu równomiernego rozkładu prawdopodobieństwa
import random
#potrzebujemy funkcji randint(a, b) z modułu random. Zwróci nam ona liczbę całkowitą z zakresu <a; b>.
c_dice = random.randint(1, 6)
user_input = int(input('Enter number from 1 to 6: '))
if user_input < 1 or user_input > 6:
    print("You've picked wrond number, restart program and choose number from 1 to 6.")
elif user_input == c_dice:
    print('True.2')
else:
    print(f'False. \nThe number was {comp_dice}!')
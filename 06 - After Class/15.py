file_name = 'colours.txt'

colours = ['red', 'blue', 'white', 'black']

with open(file_name, 'r') as file:
    for colours in file:
        print(colours, end= ' ')
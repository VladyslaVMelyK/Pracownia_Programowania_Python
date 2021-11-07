s = input('Enter the name of university where you study : ')
array = []
for letter in s:
    array.extend(letter)
print(' '.join(array))
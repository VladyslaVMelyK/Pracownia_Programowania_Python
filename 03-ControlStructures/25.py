a = int(input('Enter first variable :'))
b = int(input('Enter the second variable :'))

print('*' * b)
for i in range(a - 2):
    print('*', ' ' * (b - 4), '*')
print('*' * b)
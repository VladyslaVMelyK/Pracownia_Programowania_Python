def compare(array1, array2):
    if len(array1) == len(array2):
        for index in range(len(array1)):
            if not array1[index] == array2[index]:
        return True
    else:
        return False

array1 = ["water","book","sky"]
array2 = ["water","book","sky"]
print(f'Array 1 : {arrayA1}')
print(f'Array 2 : {arrayA2}')
comparisonA = compare(arrayA1, arrayA2)
print(f'Array are the same? {comparisonA}')
print()

arrayB1 = [True, False]
arrayB2 = [True, False, True]



    
    
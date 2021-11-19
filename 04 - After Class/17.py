def count(l, t):
    counter = 0
    for symbol in text:
        if symbol.lower() == 1:
            counter += 1        
        
        return counter
    
letter = input()
text = input()
    
print(count(letter, text))
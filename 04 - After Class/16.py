def month(n):
    if (n>=1) & (n<=12):
        return ['january', 'february', 'marth', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] [n-1]
    else:
        return 'bad months number!'
print (month(9))
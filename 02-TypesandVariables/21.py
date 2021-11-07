#Aby móc korzystać z modułów i bibliotek należy je najpierw zaimportować. Do tego celu służy słowo kluczowe import . Cały system importowania jest bardzo złożonym procesem i prawdopodobnie nie zagłębialiście się jak dokładnie działa. Importować można moduły, pakiety, funkcję i klasy. Lepiej zrozumiemy to na poniższej aplikacji.
import random

a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)

sum_of_digits = a + b + c

print(f'Result: {a}, {b}, {c}. Sum of digits: {sum_of_digits}')
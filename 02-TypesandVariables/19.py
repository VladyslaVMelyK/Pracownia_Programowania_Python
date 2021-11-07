# Python Program to find the area of triangleusing Heron's formula.
a = float(input("Enter first side : "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area =(s * (s-a) * (s-b) * (s-c))**0.5
#result
print('Area of the triangle for the sides : %0.2f' %area)
#%0.2f - ile cyfr po przecinku , dla mnie na pamiątke :)
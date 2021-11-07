cm=int(input("Enter the height in centimeters:"))
#convert centimeter to feet
feet = cm // 30.48
#convert centimeter to inches
inches = cm // 2.54
#result
print(f'I am {cm} cm tall, i.e. {feet} feet and {inches} inches.')
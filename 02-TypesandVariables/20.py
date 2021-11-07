#input variables
height_cm = int(input("Enter your height in cm : "))/100
weight_kg = int(input("Enter your weight in kg : "))
#step2. Find the formula on the Internet for calculating BMI.
bmi_index = weight_kg/(height_cm**2)
#result
print("BMI index for man :",round(bmi_index,3))
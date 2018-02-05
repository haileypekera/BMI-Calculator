#Calculating BMI
weight= input("Enter your weight in pounds: ")
height= input("Enter your height in inches: ")
BMI= 703*(int(weight)/int(height)**2)
if(int(BMI) <=18):
	print("You are underweight")
elif(int(BMI)> 18) and (int(BMI)<26):
	print("You are normal weight")
else:
	print("You are overweight")
import sys
# Ask the user to enter the birth year and calculate how many years they have
BirthYear = int(input('Hey there! \n Enter your year of birth: '))
currentYear = 2024
userAge = currentYear - BirthYear
print("You are", userAge, "years old")
# ask the user to provide the his/her height measurement
userHeight = float(input("Enter your height in meatres: "))
print('your are', userHeight, ' metres long')
# prints the data type of the entered inputs
print('the data type of Year of birth is ' , type(BirthYear))
print('the data type of user height ' , type(userHeight))

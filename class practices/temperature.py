def celciousToFerrads(userInput):
    ferrads = ((5/9)-32)
    print('the temperature in ferrads is:',ferrads)
def ferradsToDegrees(userInput):
    degree = ((9/5)+ 32)
    print('the temperature in ferrads is:',degree)

print('Hello✌✌. \n today i will help you convert temperature in ether degress or ferrads \nplease press 1 to convert from degrees to celcious \n2 to cpnvert fro ferrass to degrees')

choice =  int(input('Enter choice'))
if choice == 1:
    userInput = int( input('Enter the temperature in degrees')) 
    celciousToFerrads(userInput)
else:
    userInput =  int(input('Enter the temperature in ferrads')) 
    ferradsToDegrees(userInput)
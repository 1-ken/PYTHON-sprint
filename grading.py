#a program to get user marks and calculate the grade the user has scored
def  get_marks():
    marks = float(input("Enter the marks you scored : "))
    if marks  >=70:
        print('cogratulations you scored an A')
    elif marks >=60 and  marks <70:
        print('you scored a B')
    elif marks >=50 and marks < 60:
        print('you scored a C')
    elif marks  >=40 and marks < 50:
        print('your score is D')
    else:
         print('you failed')
get_marks()
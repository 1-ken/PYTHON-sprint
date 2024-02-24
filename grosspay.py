# a program to calculate the salary of an employee
def  calculate_salary(hours,allowance ):
    rate = 100
    if hours < 0 :
        print('you have entered invalid  number of working hours')
    
    else:
        salary = (rate * hours  )+ allowance
        print(f"your  salary is {salary}")
    
      
print('hello, i will helo you calculate your salary \n enter the number of hours you have worked:')
hours = int(input())
allowance = int(input( "enter your allowance :"))
calculate_salary(hours,allowance)
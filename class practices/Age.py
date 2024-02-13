import datetime
current_year = datetime.datetime.now().year
def get_age(birthdate):
    birth_year = int(birthdate[:4])
    if current_year - birth_year < 0:
        return "Error: Invalid year entered"
    else:
        age = current_year - birth_year
        month = int(birthdate[5:7])
        day = int(birthdate[8:10])
        return age
age = (input('Enter the date of birth: '))
print(get_age(str(age)))

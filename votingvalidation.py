def check_voting_eligibility(age, citizenship):
    # Check if the person is above 18 years and a citizen of Kenya, Uganda, or Tanzania
    if age >= 18 and citizenship.lower() in ["kenya", "uganda", "tanzania"]:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not eligible to vote.")

# Get user input 
user_age = int(input("Enter your age: "))
user_citizenship = input("Enter your citizenship (Kenya/Uganda/Tanzania): ")

#check eligibility
check_voting_eligibility(user_age, user_citizenship)
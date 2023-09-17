user_license = input("Do you have a license? \n")
user_age = int(input("Please enter your age: \n"))
if user_license.lower() == "yes" and user_age >= 18:
    print("You can drive")
elif user_license.lower() == "no" or user_age < 18:
    print("Sorry you can't drive")
else:
    print(f"Sorry, your entery of [ {user_license} ] is not understood")

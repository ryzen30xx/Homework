user_age = int(input("Enter your age: "))
if user_age < 0 or user_age > 100: 
    print("wrong age!"); exit()
elif user_age < 18: 
    print("You are not eligible to apply for a driver's license.")
elif 18<= user_age <= 19: 
    print("You are eligible to apply for a driver's license.")
elif user_age == 20: 
    print("You are eligible to apply for a driver's license. \nYou need to be at least 21 years old to rent a car.")
else: 
    print("You are eligible to apply for a driver's license. \nYou are also eligible to rent a car.")
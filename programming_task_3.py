#4
username = input("enter username: ")
password = input("enter password: ")
if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and practice Questions")
else:
    print("Invalid Credentials, Plese try again")

#5
traffic_input = input("enter traffic light (red/yellow/green): ")
if traffic_input == "red":
    print("stop")
elif traffic_input == "yellow":
    print("slow down")
elif traffic_input == "green":
    print("go")
else:
    print("invalid traffic light")


#6
season_number = int(input("enter season number: "))
match season_number:
    case 1:
        print("spring")
    case 2:
        print("summer")
    case 3:
        print("autumn")
    case 4:
        print("winter")
    case _:
        print("unknown")

#   case 1 | 2 | 3 | 4:
#       print("known season")
#   case _:
#       print("unknown")

#7
age_input = int(input("enter age: "))
monthly_salary_input = int(input("enter monthly salary: "))
credit_score_input = int(input("enter credit score: "))
if age_input in range (21, 61) and monthly_salary_input > 30000 and credit_score_input > 700:
    print("loan approved")
elif not (age_input in range (21, 61)):
    print("invalid age")
elif monthly_salary_input <= 30000:
    print("insufficient monthly salary")
elif credit_score_input <= 700:
    print("insufficient credit score")
else:
    print("unknown error ")

#8
membership_card_input = input("do you have a membership card? (yes/no): ").lower()
age_input = int(input("enter age: "))

if age_input < 12:
    price = 0
elif age_input <= 60:
    if membership_card_input:
        price = 150
    else:
        price = 200
else:
    price = 100

print(f"ticket price: Rs. {price}")


#9
salary_input = int(input("enter salary: "))
services_input = int(input("enter years of service: "))
if services_input > 5:
    bonus = salary_input * 0.05
    print(f"bonus amount: Rs. {bonus}")
else:
    print("no bonus")

#10
radius_input = float(input("enter radius of the circle: "))
area = 3.14 * radius_input ** 2
print(f"area of the circle: {area}")

#11
age_input = int(input("enter age: "))
gender_input = input("enter your gender (M/F): ").upper()
if age_input in range (18, 30):
    if gender_input == "M":
        print("wage = 700")
    elif gender_input == "F":
        print("wage = 750")
elif age_input in range (30, 41):
    if gender_input == "M":
        print("wage = 800")
    elif gender_input == "F":
        print("wage = 850")
else:
    print("invalid input")

#12
number_input = int(input("enter a number: "))
if number_input % 3 == 0 and number_input % 5 == 0:
    print("Fizz Buzz")
elif number_input % 3 == 0:
    print("Fizz")
elif number_input % 5 == 0:
    print("Buzz")
else:
    print(number_input)

#13
usage_input = int(input("enter electricity uses unit: "))
if usage_input < 100:
    bill_amount = usage_input * 5
elif usage_input < 300:
    bill_amount = (100 * 5) + ((usage_input - 100) * 8)
else:
    bill_amount = (100 * 5) + (200 * 8) + ((usage_input - 300) * 10)

print(f"electricity bill amount: Rs. {bill_amount}")

#14
user1_input = input("player1 enter rock, paper, or scissors: ").lower()
user2_input = input("plater2 enter rock, paper, or scissors: ").lower()
if user1_input in ["rock", "paper", "scissors"] and user2_input in ["rock", "paper", "scissors"]:
    if user1_input == user2_input:
        print("tie!")
    elif (user1_input == "rock" and user2_input == "scissors") or (user1_input == "paper" and user2_input == "rock") or (user1_input == "scissors" and user2_input == "paper"):
        print("User 1 wins!")
    else:
        print("User 2 wins!")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")

#15
number_input = int(input("enter a number: "))
if number_input > 0:
    print("positive")
    if number_input % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("negative")

#16
total_amount = int(input("enter total bill amount: "))
is_member_input = bool(input("are you a member? (True/False): "))
if total_amount > 1000:
    if is_member_input:
        total_amount = total_amount - (total_amount * 0.2)
        print(f"Total amount = Rs. {total_amount}")
    else:
        total_amount = total_amount - (total_amount * 0.1)
        print(f"Total amount = Rs. {total_amount}")
else:    
    print(f"Total amount = Rs. {total_amount}")\
    
#17
weight_input = float(input("enter weight: "))
planet_input = int(input("enter planet number (1-7): "))
if planet_input == 1:
    weight_on_planet = weight_input * 0.38
    print(f"your weight on Mercury is: {weight_on_planet}")
elif planet_input == 2:
    weight_on_planet = weight_input * 0.91
    print(f"your weight on Venus is: {weight_on_planet}")
elif planet_input == 3:
    weight_on_planet = weight_input * 0.38
    print(f"your weight on Mars is: {weight_on_planet}")
elif planet_input == 4:
    weight_on_planet = weight_input * 2.53
    print(f"your weight on Jupiter is: {weight_on_planet}")
elif planet_input == 5:
    weight_on_planet = weight_input * 1.07
    print(f"your weight on Saturn is: {weight_on_planet}")
elif planet_input == 6:
    weight_on_planet = weight_input * 0.89
    print(f"your weight on Uranus is: {weight_on_planet}")
elif planet_input == 7:
    weight_on_planet = weight_input * 1.14
    print(f"your weight on Neptune is: {weight_on_planet}")
else:
    print("invalid planet number")

#18
marks1_input = int(input("enter marks for subject 1: "))
marks2_input = int(input("enter marks for subject 2: "))
marks3_input = int(input("enter marks for subject 3: "))
marks4_input = int(input("enter marks for subject 4: "))
total_marks = marks1_input + marks2_input + marks3_input + marks4_input
average_marks = total_marks / 4
if average_marks >= 70:
    print("grade: distinction")
elif average_marks >= 60:
    print("grade: first")
elif average_marks >= 40:
    print("grade: pass")
else:    
    print("grade: fail")
print(f"total marks: {total_marks}, percentage: {average_marks}")

#19
balance = 5000
correct_pin = "123"
print("Welcome to the ATM!")
is_card_valid = True
if is_card_valid:
    pin = input("Please enter your PIN: ")
    if pin == correct_pin:
        print("PIN accepted. You can now access your account.")
        print("Your current balance is: $", balance)
        print("2 - check balance 1 - withdraw money 3 - exit")
        choice = input("Please select an option: ")
        if choice == "2":
            print("Your current balance is: $", balance)
        elif choice == "1":
            amount = float(input("Enter the amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds. Your current balance is: $", balance)
            elif amount >= 499:
                balance -= amount
                print("Please take your cash. Your new balance is: $", balance)
        elif choice == "3":
            print("Thank you for visiting.")
        else:
            print("Invalid option.")
    else:
        print("Incorrect PIN.")
else:
    print("Invalid card.")

#20
print("Welcome to the Magic Forest")
direction_input = input("Go (north/ south)?").lower()
if direction_input == "north":
    river_input = input("(Cross the river/follow the path)?").lower()
    if river_input == "follow the path":
        role_input = input("(fairy/oger/elf)?").lower()
        if role_input == "elf":
            print("you win!")
        else:
            print("invalid choice. End")
    else:
        print("cross the river. end")
elif direction_input == "south":
    print("south. end")
else:
    print("invalid choice")

#21
floor_input = int(input("enter floor number: 1 - 10: "))
if floor_input in range(1, 11):
    weight_input = int(input("enter weight: 1 - 500: "))
    if weight_input in range(1, 501):
        door_input = bool(input("is door closed? (True/False): "))
        if door_input   == True:
            print("elevator in motion")
        else:
            print("door is open")
    else:
        print("invalid weight")
else:   
    print("invalid floor number")

print("rest of the option")




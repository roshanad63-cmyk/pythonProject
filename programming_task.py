#1
input_number = int(input("Enter a number to check if it is between 1 and 100: "))
if 1 < input_number < 100:
    print("The number is between 1 and 100.")
else:
    print("The number is not between 1 and 100.")

#2
number = int(input("Enter a number to check if it is even or odd: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#3
month_number = int(input("Enter a number between 1 and 12 to get the corresponding month: "))

month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if month_number in month:
    print(month[month_number])
else:
    print("Error: Please enter a number between 1 and 12.")


#4
marks = int(input("Enter marks: "))
if marks < 25:
    print("Grade: F")
elif 25 <= marks < 45:
    print("Grade: E")
elif 45 <= marks < 50:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: C")
elif 60 <= marks < 80:
    print("Grade: B")
elif marks >= 80:
    print("Grade: A")
else:
    print("Error: Please enter valid marks.")

#5
number_to_check = int(input("Enter a number to check if it is divisible by 7: "))
if number_to_check % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")

#6
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    result = first_number + second_number
    print(f"Your Answer is: {result}")
elif operator == '-':
    result = first_number - second_number
    print(f"Your Answer is: {result}")
elif operator == '*':
    result = first_number * second_number
    print(f"Your Answer is: {result}")
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f"Your Answer is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please enter one of +, -, *, /.")

#7
salary_input = float(input("Enter your salary: "))
credit_score_input = int(input("Enter your credit score: "))
if salary_input >= 50000 and credit_score_input >= 700:
    print("Eligible")
else:
    print("Not Eligible")

#8
number_input = int(input("Enter an integer: "))
if number_input % 3 == 0 and number_input % 5 == 0:
    print("FizzBuzz")
elif number_input % 5 == 0:
    print("Buzz")
elif number_input % 3 == 0:
    print("Fizz")
else:
    print(number_input)

#9
character_input = input("Enter a character: ").lower()
if character_input in 'aeiou':
    print("The character is a vowel.")
elif character_input.isalpha() and len(character_input) == 1:
    print("The character is a consonant.")
else:
    print("Error: Please enter a single alphabetic character.")

#10
marks_input = int(input("Enter your marks: "))
if 90 <= marks_input <= 100:
    print("Grade: A")
elif 80 <= marks_input < 90:
    print("Grade: B")
elif 70 <= marks_input < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

#11
age_input = int(input("Enter your age: "))
if age_input < 13:
    print("Category: Child")
elif 13 <= age_input <= 19:
    print("Category: Teenager")
else:
    print("Category: Adult")

#12
char_input = input("Enter a character: ")
if char_input.isupper():
    print("The character is uppercase.")
elif char_input.islower():
    print("The character is lowercase.")
elif char_input.isdigit():
    print("The character is a digit.")
else:
    print("The character is neither uppercase, lowercase, nor a digit.")

#13
color_input = input("Enter a traffic light color (Red, Yellow, Green): ").lower()
if color_input == "red":
    print("Action: Stop")
elif color_input == "yellow":
    print("Action: Get Ready")
elif color_input == "green":
    print("Action: Go")
else:
    print("Error: Invalid color. Please enter Red, Yellow, or Green.")

#14
age_input = int(input("Enter your age: "))
experience_input = int(input("Enter your experience (in years): "))
if age_input > 18 and experience_input >= 2:
    print("Eligible")
else:
    print("Not Eligible")

#15
temperature_input = float(input("Enter the temperature in °C: "))
if temperature_input > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature_input <= 30:
    print("Enjoy the weather!")
else:    
    print("It's cold, wear warm clothes!")

#16
menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").lower()
if menu_option == "pizza":
    print("Price: $10")
elif menu_option == "burger":
    print("Price: $7")
elif menu_option == "pasta":
    print("Price: $8")
else:
    print("Please enter Pizza, Burger, or Pasta.")

#17
height_input = float(input("Enter the player's height in feet: "))
if height_input >= 6:
    print("Selected")
else:
    print("Not Selected")

#18
age_input = int(input("Enter your age: "))
if age_input >= 18:
    print("Allowed")
else:
    print("Not Allowed")

#19
username_input = input("Enter username: ")
password_input = input("Enter password: ")
if username_input == "admin" and password_input == "password123":
    print("Access Granted")
else:
    print("Access Denied.")

#20
month_input = int(input("Enter a month number (1-12): "))
if month_input in [12, 1, 2]:
    print("Season: Winter")
elif month_input in [3, 4, 5]:
    print("Season: Spring")
elif month_input in [6, 7, 8]:
    print("Season: Summer")
elif month_input in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

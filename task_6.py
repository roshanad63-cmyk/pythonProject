#1
for i in range (1, 6):
    if i % 2 == 0:
        print(f"Number {i} is even.")
    else:
        print(f"Number {i} is odd.")

#2
list = [10, 20, 30, 40]
total = 0
for num in list:
    total += num
    print(f"Added {num}. Running total is {total}")
print("---------------------------")
print(f"Total Sum: {total}")

#3
students_names = ["Ram", "Hari", "Sita"]
print("---Email Greetings Generated---")
for name in students_names:
    print(f"Hi {name}, your course approval is ready!")

#4
pages=[45, 30, 50, 40]
print("---Book chapter summary----")
for i in range (len(pages)):
    print(f"Chapter {i+1} has {pages[i]} pages.")

#5
provided_numbers = [4, 5, 3, 2]
for num in provided_numbers:
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    print()

#6
for i in range (1 ,11):
    print(f"{i} x {11} = {i*11}")

#7
list = [3, 2, 1, 4, 5]
reversed_list = []
for i in range(len(list)-1, -1, -1):
    reversed_list.append(list[i])

print(reversed_list)

#8
first_list = [1, 2, 3, 4, 5]
second_list = [3, 4, 5, 6, 7]
common_elements = []
for element in first_list:
    if element in second_list:
        common_elements.append(element)
print(common_elements)

#9
lst = [1, 2, 3, 4]
for i in lst:
    if i == 1 or i == 4:
        print(i)

#10 
user_input = input("Enter a string: ").lower()
vowels = "aeiou"
result = ""
for char in user_input:
    if char not in vowels:
        result += char
print(result)

#11
given_string = "Loops are Fun".lower()
vowels = "aeiou"
vowels_count = 0
consonants_count = 0
for char in given_string:
    if char in vowels:
        vowels_count += 1
    elif char == ' ':
        continue
    else:
        consonants_count += 1
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")

#12
list = [1, 2, 3, 4, 5]
even_list = []
odd_list = []
for i in list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f"Even numbers: {even_list}")
print(f"Odd numbers: {odd_list}")

#13
user_input = int(input("Enter a number: "))
is_prime = True
for i in range(2, user_input):
    if user_input % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

#14
given_list = [1, 2, 3, 4, 'a', 'b']
numbers_list = []
strings_list = []
for item in given_list:
    if isinstance(item, int):
        numbers_list.append(item)
    elif isinstance(item, str):
        strings_list.append(item)
print(f"Numbers: {numbers_list}")
print(f"Strings: {strings_list}")

#15
user_input = input("Enter a string: ")
digit_count = 0
letter_count = 0
for char in user_input:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
        
print(f"Number of digits in the string: {digit_count}")
print(f"Number of letters in the string: {letter_count}")

#16
username = input("Enter a username: ")
password = input("Enter a password: ")
if username == "admin" and password == "password123":
    print("valid username and password.")
else:
    print("Invalid username or password.")

#17
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#18
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}.")

#19
list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list:
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")
    print()

#20
lst = [1, 2, 3, 4]
for i in lst:
    if i == 1 or i == 2:
        print(i)

#21
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))
odd_sum = 0
if range_start < range_end:
    for i in range(range_start, range_end + 1):
        if i % 2 != 0:
            odd_sum += i
    print(f"The sum of odd numbers between {range_start} and {range_end} is {odd_sum}.")
else:    
    print("Invalid range. Start should be less than end.")

#22
even_sum = 0
if range_start < range_end:
    for i in range(range_start, range_end + 1):
        if i % 2 == 0:
            even_sum += i
    print(f"The sum of even numbers between {range_start} and {range_end} is {even_sum}.")
else:    
    print("Invalid range. Start should be less than end.")

#23
input_string = input("Enter a string: ")
total_spaces = 0
for char in input_string:
    if char == ' ':
        total_spaces += 1
print(f" Total spaces: {total_spaces}")

#24
given_list = [1, 2, 3, 4]
empty_list = []
for i in given_list:
    empty_list.append(i**3)
print(empty_list)

#25
st = 'programming'
reversed_string = ''
for i in range(len(st)-1, -1, -1):
    reversed_string += st[i]
print(reversed_string)

#26
for i in range (0, 51):
    print(i)
    if i >= 7:
        break

#27
input_string = input("Enter a string: ")
for char in input_string:
    print(char)

#28
a=["ram","shyam",1,2]
for i in a:
    if isinstance(i, str):
        print(f"hello! {i}")

#29
a=["ram","shyam"]
for i in a:
    a.append(f'dr. {i}')
print(a)

#30
numbers = input("Enter numbers separated by space: ").split()
squired_numbers = []
for num in numbers:
    squired_numbers.append(int(num) ** 2)
print(squired_numbers)

#31
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []
for num in lst1:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)

#32
list=[0,1,2,3,4,5,6]
for i in list:
     if i != 3 and i !=6:
         print(i)

#33
input_list = input('provide a list separated by space: ').split()
element_types = []
for element in input_list:
    if element.isdigit():
        element_types.append('number')
    else:
        element_types.append('string')

print(element_types)

#34
for i in range(1,10):
    if i < 9:
        print(i)
        continue
    else:
        print('done')


#35
for i in range(105,6,-7):
    print(i)

#36
bad_chars = [';', ':', '!', "*", ' ']
string = "py;th* o:n ! ;py * t*h:o !n"
for char in bad_chars:
    string = string.replace(char, "")
print(string)

#37
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))
odd_count = 0
even_count = 0
if range_start < range_end:
    for i in range(range_start, range_end + 1):
        if i % 2 != 0:
            odd_count += 1
        else:
            even_count += 1
    print(f"The count of odd numbers between {range_start} and {range_end} is {odd_count}.")
    print(f"The count of even numbers between {range_start} and {range_end} is {even_count}.")
else:    
    print("Invalid range")

#38
sum_multiples = 0
for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        sum_multiples += i
print(f'sum = {sum_multiples}')

#39
sum_even = 0
sum_odd = 0
for i in range(1, 100):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f'even numbers = {sum_even}')
print(f'odd numbers = {sum_odd}')

#40
list1= [10, 20 , 10 ,30, 10 , 40, 50]
target = 10
count = 0
for num in list1:
    if num == target:
        count += 1
print(f'{target} appears {count} times')

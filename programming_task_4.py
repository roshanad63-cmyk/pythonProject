#1
student_records = {'ram' : 'ram@gmail.com', 
                   'hari' : 'hari@gmail.com'}

name = input('enter name: ').lower()

s_record = student_records.get(name, 'contact not found')
print(s_record)

if name in student_records:
    print(student_records[name])
else:
    print('contact not found')

#2

shopping_list = {'milk', 'bread', 'eggs'}
bought_items = {'bread', 'eggs'}

a = shopping_list.difference(bought_items)

if a:
    print('you need to buy', a)
else:
    print('shopping complete')


#3
class_list = ['ram', 'sita', 'laxman']
name = input('enter name: ').lower()
if name in class_list:
    print(name, 'already exists')
else:
    class_list.append(name)
    print(name, ' added')

#4
votes = ['blue', 'green', 'red', 'blue', 'blue']
i = 0
for vote in votes:
    if vote == 'blue':
        i = i + 1

if i >=3:
    print('blue wins')
else:
    print('blue did not win')

#5
grades = {"ram": 92, "sita": 88}
name = input("enter name: ").lower()
grade = grades.get(name, "grade is not available")
print(grade)

#6
applicant={'name':'Priya', 'skills':['Java', 'sQL'], 'experience_years':1}
required_skills = {'Python', 'Java'}
if required_skills.issubset(set(applicant['skills'])) and applicant['experience_years'] >= 2:
    print(f"{applicant['name']} qualifies")
else:
    print(f"{applicant['name']} does not qualify")

#7
banned_items = {'scissors', 'knife', 'lighter'}
item = input('enter item: ').lower()
weight = float(input('enter weight: '))
if item in banned_items and weight < 7:
    print('bag not allowed')
else:
    print('bag allowed')

#8 
sample_dict = {'emp1': {'name': 'Jhon', 'salary':7500},
               'emp2': {'name': 'Emma', 'salary':8000},
               'emp3': {'name': 'Shyam', 'salary':500}}

sample_dict['emp3']['salary'] = 8500

#9

ram_items = set(input('enter items separated by comma').split(','))
laxman_items = set(input('enter items separated by comma').split(','))

if ram_items.isdisjoint(laxman_items):
    print('they picked completely different items')
else:
    print('they have some common items')

#16
menu = {'Pizza': 15, 'Burger':10, 'Salad': 8}
order = 'Pizza'
if order in menu:
    print(f"{order} costs ${menu[order]}")
else:
    print('item not found')

#17
student_data = {'name': 'Sam', 'score': 85}
if student_data['score'] >= 80:
    status = 'pass'
else:
    status = 'fail'
print(f'{student_data} {status}')

#18
database = {'admin': '1234', 'user': 'abcd'}
user_input = 'admin'
user_pass = '1234'
if user_input in database and database[user_input] == user_pass:
    print('login successful')
else:
    print('login failed')

#20]
inventory = {'A1': 50 , 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'
if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print('dispash item')
    else:
        print('stock error')
else:
    print('invalid zone')

#21
valid_couses = {'python', 'robotics', 'java'}
hs_grades = [9, 10, 11, 12]
student_records = {}
name = input('enter name: ')
course = input('enter course: ').lower()
grade = int(input('enter grade: '))
student_records[name] = {'course': course, 'grade': grade}
if student_records[name]['course'] in valid_couses:
    if student_records[name]['grade'] in hs_grades:
        if student_records[name]['course']== 'robotics' and student_records[name]['grade'] > 9:
            print(f"{name} is eligible for robotics")
        else:
            print(f"{name} is eligible for {student_records[name]['course']}")
    elif student_records[grade] < 9:
        print('grade too low')
    else:
        print('grade too high')
else:
    print(f'course {student_records[name]} selected an invalid course')
        
        

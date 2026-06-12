#1
while (user_input := input('enter a age :')).lower != 'stop':
    if int(user_input)< 18:
        print('u are an minor')
    elif int(user_input)<60:
        print('u are an adult')
    else:
        print('u are a  senior citizen')

print('rest of the program')

#2
while (user_input := input('enter a vehicle ')).lower != 'bus':
    print('---------waiting--------')
else:
    print('finally the wait is over')

print('rest of the program')

#3
Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_ratings={}
i=0
while i < len(Ratings):
    if Ratings[i] in content_ratings:
        content_ratings[Ratings[i]]+=1
    else:
        content_ratings[Ratings[i]]=1
    i += 1

print(content_ratings)

#4
import random
num = random.randint(1, 10)
i = 1
while (user_input := int(input('guess a number between 1 to 10: '))) != num:
    i += 1
    if user_input > num:
        print('guess low ')
    else:
        print('gusee high ')
print(f'{num} was the random num. you guessed {i} times.')

#5
i = 3
while True:
    if i==0:
         print('too many attempt failed')
         break
    
    i-=1
    username = input('username : ')
    password = input('password :')
    if username != 'admin' and password  != '1234':
        print(f'you have {i} attempts')
    else:
            print('login sucessful')
            break

print('rest')

#6
import random
while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    if num1*num2 == int(input(f'{num1}*{num2} = ')):
         print('correct')
    else:
         print('Incorrect, try again')
    if input('continue or exit?') == 'exit':
         break
print('rest of the code')

#7
good_luck_count = 0

while good_luck_count < 3:
    user_input = input('enter a name').lower()
    
    if user_input == 'good luck':
        good_luck_count += 1
        
        if good_luck_count == 3:
            print('you typed good luck three times')
        else:
            print(f'you typed the same word {good_luck_count} times')
    else:
        print(f'You entered: {user_input}')

print('rest of the code')

#8
import random
num = random.randint(1, 50)
i = 7
while (user_input := int(input('guess a number between 1 to 50: '))) != num:
    if i==1:
        print('too many attempt failed')
        break
    i -= 1
    if user_input > num:
        print('guess low')
    else:
        print('gusee high ')
    print(f'you have {i} attempts left')
print(f'{num} was the random num.')

#9
floor = 1

while (user_input := input('provide destination floor : ')) != '0':

    if user_input.isdigit():
        int_input = int(user_input)

        if int_input > floor:
            print('going up')
            floor = int_input
        elif int_input < floor:
            print('going down')
            floor = int_input
        else:
            print('current floor selected')
    
    else:
        print('provide valid input')

else:
    print('goodbye!')

#10
player1_score = 0
player2_score = 0
while True:
    user1_input = input("player1 enter rock, paper, or scissors: ").lower()
    user2_input = input("plater2 enter rock, paper, or scissors: ").lower()
    if user1_input in ["rock", "paper", "scissors"] and user2_input in ["rock", "paper", "scissors"]:
        if user1_input == user2_input:
            print("tie!")
        elif (user1_input == "rock" and user2_input == "scissors") or (user1_input == "paper" and user2_input == "rock") or (user1_input == "scissors" and user2_input == "paper"):
            print("1 point for player_1")
            player1_score +=1
        else:
            print("1 point for player_2")
            player2_score +=1
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

    if player1_score == 5:
        print('player 1 won the game')
        break
    elif player2_score == 5:
        print('player 2 won the game')
        break

#11
i = 49
j = 1
while i > 0:
    print (f'{j} - {i}')
    i -= 1
    j += 1

print('rest')

#12
user_input = int(input('provide a number : '))
sum = 0
while (user_input > 0):
    sum += user_input
    user_input -= 1

print(sum)

#13
i = 65
while i <= 90:
    print(chr(i), end=" ")
    i += 1

#14
number = [2, 40, 21, 31, 10, 7, 5]
i = 0
while i < len(number):
    if number[i] < 20:
        print(number[i])

    i += 1

print('rest')

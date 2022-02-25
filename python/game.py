
from random import randint
number = randint(1, 99) # 44
player_name = input("Hello, What's your name?")
count_guess = 0
inp_user = int(input())
lst = []

for i in range(1,int(inp_user)):
    guess = int(input()) 
    count_guess += 1

    if guess < number:
        print('you guess bigger number ')

    if guess > number:
        print('Your guess is small number ')

    if guess == number:
        print(f'amazing player is {player_name} + guess count is : {str(count_guess)}')
        break

print('the guess number is :', number)
hads = input('Are you exit gameplay:?')
if hads == 'yes':
    r = input('\press enter key for exit game.')
else:
    print('good bye!')


# return gameplay if hads enter yes ,every input hads program break it!

# second solve for this example
'''
import random,math
numbers = []
for i in range(1,100):
    numbers.append(i)

while True:
    myRandom = random.choice(numbers)
    print('the computer gauss :', myRandom)
    inp = input('enter k or b or d keys for run it : \n')
    if inp == 'k':
        del numbers[numbers.index(myRandom):]
        print(myRandom)
        #numbers = list(filter(lambda a: a < myRandom, numbers)) # smaller numbers
        print(numbers)
    elif inp == 'b':
        del numbers[:numbers.index(myRandom)+1]
        #numbers = list(filter(lambda a: a > myRandom, numbers)) # bigger numbers
        print(numbers)
    elif inp =='d':
        print('hooooo!! my guess is True!')
        break
    else:
        print('what is this command? idont know this')

'''













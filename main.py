#The game 
import random
from typing import List

INT_RAN = random.randint(1, 20)
print(INT_RAN)
print('Try to guess the number between 1 and 20.')
jj = input('Do you want to play on "easy" or "hard" level?\n').lower()
att = 0
if jj == 'hard' :
    att = 5
else :
    att = 10
print(att)

contador = 0
while contador < att : 
    user = int(input('What´s your number: '))
    if user == INT_RAN :
        print(f'You win, the number guessed is {INT_RAN}')
        contador = contador =+ 1
        break
    if user < INT_RAN :
        print('Low')
        contador = contador =+ 1
    if user > INT_RAN :
        print('High')
        contador = contador =+ 1
if user == INT_RAN :
    print(f'You won!')
if user != INT_RAN :
    print(f'Your lose, the guessed number was {INT_RAN}')
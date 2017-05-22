# This is a guess game
import random

def getInput(number):
    try:
        return int(number)
    except ValueError:
        print ('the argument is not a number')

print('Hello ! , What is your name ? ')
name = input()
print('Well,' + str(name) + ' I am thinking of a number between 1 and 100')
computer_guess = random.randint(1,20)

guessed = False

for i in range(3):
    print('Take a guess')
    your_guess = getInput(input())

    if computer_guess < your_guess:
        print ("your guess is high !")

    if computer_guess > your_guess:
        print ("your guess is too low !")

    if computer_guess == your_guess:
        print ("congratulations ! you found it !")
        guessed = True
        break

if not guessed:
    print ("The number I thought was ,"+ computer_guess)

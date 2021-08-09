# This is a Guess the Number game
import random
guessesTaken = 0
myName = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print('Well ' + myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):

    try:
        guess = int(input('Take a guess.\n'))
        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        elif guess  == number:
            break
    except ValueError:
        print('Please enter a number!')

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses.')
else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')

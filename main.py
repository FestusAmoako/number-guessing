from colours import *
from random import randint

# welcome screen message
print(BLUE, '****welcome to Your world of Guessing****')
user_input = int(input((White + 'choose your level\n'
                                '1. normal (1-50)\n'
                                '2. intermediate(1-200)\n'
                                '3. hard(1-500)\n'
                                '4. exit application\n'
                                'Enter request: ')))

#  user input
guess_range = 0
if user_input == 1:
    guess_range = 50
elif user_input == 2:
    guess_range = 200
elif user_input == 3:
    guess_range = 500
elif user_input == 4:
    print('**** Thanks For Using Our App , Hope To See You Again')
    exit(1)
else:
    print(Red + 'invalid Request, Try Again')

# Generate Random number between certain numbers,
generate_number = randint(1, guess_range)

# user chances
user_chances = 4

for i in range(4):
    user_guess = int(input('provide Your Guess Number: '))

    # determine if the guess is correct
    if user_guess == generate_number:
        print(Green, f'Hurray!!!, Your Guess is Correct')
        break
    elif user_guess > generate_number:
        print(Yellow, 'You Guessed Too high Try Again')
    elif user_guess < generate_number:
        print(Yellow, 'you  Guessed Too low ')
    # reducing user chance and prompt user chances left
    user_chances -= 1
    print(f'number of chances left is {user_chances}')
# inform user of the correct guess number
if user_chances == 0:
    print(Red,f'the correct guess is {generate_number}')

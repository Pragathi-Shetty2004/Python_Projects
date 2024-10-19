import random
import pyfiglet

text='GUESS THE NUMBER'
ascii_art=pyfiglet.figlet_format(text,justify='center')
print(ascii_art)
print('Let me think of number between 1 to 50')
level=input("Choose the level of difficulty 'easy' or 'hard' ")
if level=='easy':
    no_of_attempts=10
else:
    no_of_attempts=5

number=random.randint(1,50)
end_game=True
while end_game:
    guess_number=int(input('Enter number'))
    if guess_number==number:
        print(f'Your guess was right\n Answer was {number}')
        exit()
    elif guess_number>number:
        print('your guess is too high')
        no_of_attempts-=1
        print(f'You are left with {no_of_attempts} chances to guess\nGuess again')
    else:
        print('Your guess is too low')
        no_of_attempts-=1
        print(f'You are left with {no_of_attempts} chances to guess\nGuess again')
    if no_of_attempts==0:
        print('You are out of guesses\nYou lose')
        end_game=False


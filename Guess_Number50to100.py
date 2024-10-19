import random
import pyfiglet
easy_attempts=10
hard_attempts=5

text='GUESS THE NUMBER'
ascii_art=pyfiglet.figlet_format(text,justify='center')
print(ascii_art)
print('Let me think of number between 50 to 100')
answer=random.randint(1,50)

level=input('Enter difficulty level,"easy" or "hard"')
def attempts():
    if level=='easy':
        return easy_attempts
    elif level=='hard':
        return hard_attempts
    else:
        return
def guessed_answer(Guess,answer,no_of_attempts)   :
    if Guess==answer:
        print(f'Your guess was right\n Answer was {answer}')
        exit()
    elif Guess>answer:
        print('your guess is too high')

    else:
        print('Your guess is too low')


def game():
       no_of_attempts=attempts()

       if no_of_attempts==None:
           print('Wrong input')
           exit()

       Guess=0
       while answer!=Guess:
           Guess=int(input('Guess the number'))
           guessed_answer(Guess, answer, no_of_attempts)
           no_of_attempts -= 1
           print(f'You are left with {no_of_attempts} chances to guess\n')
           if(no_of_attempts==0):
               exit()
           else:
               print('Guess again')


game()





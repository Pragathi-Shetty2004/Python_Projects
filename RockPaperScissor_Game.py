import random
userChoice=int(input('Enter choice\nEnter0-Rock\n1-Paper\n2-Scissor\n'))
if(userChoice>3 or userChoice<0):
    print('Invalid entry')
    exit()
if(userChoice==0):
    print('Your choice is Rock')
elif(userChoice==1):
    print('Your choice is Paper')
else:
    print('Your choice is Scissor')

computerChoice=random.randint(0,2)
#print(f'{computerChoice} is computerChoice')
#if(computerChoice>3 or computerChoice<0):
    #print('Invalid entry')
    #exit()
if(computerChoice==0):
    print('computer choice is Rock')
elif(computerChoice==1):
    print('computer choice is Paper')
else:
    print('computer choice is Scissor')
print(f'{userChoice} v/s {computerChoice}')
if(computerChoice==userChoice):
    print('It\'s Draw')
elif(computerChoice==0 and userChoice==2):
    print('Computer wins')
elif(computerChoice==2 and userChoice==0):
    print('You win')
elif(computerChoice>userChoice):
    print('Computer wins')

else:
    print('You win')


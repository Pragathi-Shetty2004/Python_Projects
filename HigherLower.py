import pyfiglet
import random
import game_database
import os
score=0
text='HIGHER LOWER GAME'
ascii_art=pyfiglet.figlet_format(text,justify='center')
end_Game=True
print(ascii_art)
compare_1=random.choice(game_database.data)
while end_Game:

    print(f'Compare 1:{compare_1['Name']},{compare_1['Description']},{compare_1['Country']}')
    vs='VS'
    ascii_art2=pyfiglet.figlet_format(vs)
    print(ascii_art2)
    compare_2=random.choice(game_database.data)
    print(f'Compare 2:{compare_2['Name']},{compare_2['Description']},{compare_2['Country']}')
    def comparision(compare_1,compare_2):
        if compare_1['Follower Count']>compare_2['Follower Count']:
            return 1
        else:
            return 2
    max=comparision(compare_1,compare_2)


    if max==int(input('Who has more followers on Instagram\nType"1" or "2"')):
        score+=1
        os.system('cls')
        print(ascii_art)
        print(f'You are right\nYour score is {score}')
        compare_1 = compare_2

    else:
        os.system('cls')
        print(ascii_art)
        print(f'You are wrong,Your final score is {score} ')
        end_Game=False







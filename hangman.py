import random
import word_file
#Word_list=['apple','elephant','parrot','lion','town','christmas','cartoon','jungle']
word=random.choice(word_file.words)
length=len(word)
list=[]
word_list=[]
for i in range(length):
    word_list+=word[i]
for i in range(length):
    list+='_'
print('let\'s play a Hangman game ')
print("\U0001F604 \U0001F642 \U0001F604")
print('You have only 6 lives!!')
print(list)
lives=6
while (lives!=0 and word_list!=list):
    Guessed_letter = input('Guess a letter ')

    if Guessed_letter in word_list:
       for i in range(length):
           if Guessed_letter==word_list[i]:
               pos=i
               list[pos]=Guessed_letter
               print(list)

    else:
        lives-=1
        print(f'You are left with {lives} lives !!')
        if(lives==5):
                print('+-----+')
                print('   |  |')
                print('   O  |')
                print('      |')
                print('      |')
                print('      |')
                print('=======')
        elif(lives==4):
                print('+-----+')
                print('   |  |')
                print('   O  |')
                print('   |  |')
                print('      |')
                print('      |')
                print('=======')
        elif(lives==3):
                print('+-----+')
                print('   |  |')
                print('   O  |')
                print('  /|  |')
                print('      |')
                print('      |')
                print('=======')
        elif(lives==2):
                print('+------+')
                print('   |   |')
                print('   O   |')
                print('  /|\\ |')
                print('       |')
                print('       |')
                print('=======')
        elif(lives==1):
                print('+------+')
                print('   |   |')
                print('   O   |')
                print('  /|\\ |') #     Escape meaning of backslash is removed by using \\
                print('  /    |')
                print('       |')
                print('=======')
        elif(lives==0):
                print('+------+')
                print('   |   |')
                print('   O   |')
                print('  /|\\  |')  #Escape meaning of backslash is removed by using r before string
                print('  / \\  |')
                print('       |')
                print('=======')

if(lives==0):
    print('Out of lives!!')
    print("\U0001F641")
    print(f'The word is {word}')
if(word_list==list):
    print('You won !!')
    print("\U0001F44C")

print('GAME OVER!!')





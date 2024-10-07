import random
import string

n_letters=int(input('Enter number of letters'))
n_symbols=int(input('Enter number of symbols'))
n_numbers=int(input('Enter number of numbers'))

l1=list(string.ascii_lowercase)
l2=list(string.ascii_uppercase)
L1=l1+l2
l3=['!','@','#','$','%','^','&','*','(',')','+','=']
l4=['0','1','2','3','4','5','6','7','8','9']
password_list=[]

for i in range(1,n_letters+1):
    password_list+=random.choice(L1)

for i in range(1,n_symbols+1):
    password_list+=random.choice(l3)

for i in range(1,n_numbers+1):
    password_list+=random.choice(l4)
random.shuffle(password_list)
print('Your password is here')
password=""
for i in password_list:
    password+=i
print(f'{password} is your password')
import random
import string

n_letters=int(input('Enter number of letters'))
n_symbols=int(input('Enter number of symbols'))
n_numbers=int(input('Enter number of numbers'))

l1=list(string.ascii_lowercase)
l2=list(string.ascii_uppercase)
L1=l1+l2
l3=['!','@','#','$','%','^','&','*','(',')','+','=']
l4=['0','1','2','3','4','5','6','7','8','9']
password_list=[]

for i in range(1,n_letters+1):
    password_list+=random.choice(L1)

for i in range(1,n_symbols+1):
    password_list+=random.choice(l3)

for i in range(1,n_numbers+1):
    password_list+=random.choice(l4)
random.shuffle(password_list)
print('Your password is here')
password=""
for i in password_list:
    password+=i
print(f'{password} is your password')

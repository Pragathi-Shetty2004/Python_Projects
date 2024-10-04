import random
names=input('Enter names seperated by comma')
list=names.split(",")
length=len(list)
print('Using randint function')
print(list[random.randint(0,length-1)]+" will pay bill")
#using choice
print('Using choice function')
person=random.choice(list)
print(f'{person} will pay bill')
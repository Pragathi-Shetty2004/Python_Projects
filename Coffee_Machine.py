import pyfiglet
ascii_art=pyfiglet.figlet_format('C O F F E E    \nM A C H I N E')
print(ascii_art)
not_end=True
Total={
'Water':1000,
    'Milk':1000,
    'Coffee':500,
    'Profit':0
}

latte={
    'Water':100,
    'Milk':50,
    'Coffee':50,
    'Price':150

}
espresso={
'Water':200,
    'Milk':70,
    'Coffee':25,
    'Price':100

}
cappuccino={
'Water':75,
    'Milk':55,
    'Coffee':50,
    'Price':200
}
drinks = {              #***Nested dictionary***
    'latte': latte,
    'espresso': espresso,
    'cappuccino': cappuccino
}

while not_end:

    Choice=input('What would you like to have ? (latte/espresso/cappuccino) ')

    if Choice == 'report':
        print(Total)
        Choice = input('What would you like to have ? (latte/espresso/cappuccino) ')


    if Choice == 'off':
        exit()
    def resources():
        for i in Total:
            if Total[i]<0 and Total[i]==0:
                print(f'Sorry there\'s shortage of {i}')
                return -1

    def After_Pay():
        global Profit

        if resources()!=-1:

            print('Insert coins')
            five=int(input('How many 5Rs. coin received ?'))
            ten=int(input('How many 10Rs. coin received ?'))
            twenty=int(input('How many 20Rs. coi received ?'))
            total_money=five*5+ten*10+twenty*20
            # print(total_money)

            if(total_money>drinks[Choice]['Price']):

                change=total_money-drinks[Choice]['Price']
                print(f'Here\'s your change of Rs.{change} ')
                Total['Profit']+=drinks[Choice]['Price']

            elif total_money<drinks[Choice]['Price']:
                print(f'Money is not sufficient,Your {total_money} Rs is refunded')
            else:

                Total['Profit']+=total_money
    After_Pay()
    print('Payment successful')
    def deduction():
        for i in Total:
            if i=='Profit':
                continue
            Total[i]-=drinks[Choice][i]
        return Total
    Total_left=deduction()
    print(f'Here\'s your {Choice}')







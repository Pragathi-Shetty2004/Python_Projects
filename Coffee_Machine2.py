resources={
    'ingredients':{
    'water':500,
    'milk':300,
    'coffee':300},
    'profit':0


}
latte={'ingredients':
           {'water':100,
                'milk':50,
                'coffee':50
            },
       'cost':150
}
espresso={
    'ingredients':{
'water':100,

    'coffee':50},
'cost':100


}
cappuccino = {
    'ingredients':{
    'water': 100,
'milk':100,
    'coffee': 100},
    'cost':
     200

}
Selection={
    'latte':latte,
    'espresso':espresso,
    'cappuccino':cappuccino
}


off=False
while not off:
    choice = input('What would you like to have ? (latte/espresso/cappuccino)[enter report to get details of resources and off to exit')
    if choice == 'report':
        print(f'water={resources['ingredients']['water']}ml\nmilk={resources['ingredients']['milk']}ml\ncoffee={resources['ingredients']['coffee']}gms\nprofit={resources['profit']}Rs')
    elif choice == 'off':
        off = True
    else:
        coffee_type=Selection[choice]
        print(coffee_type)
        def check_resources(order_ingredients):
         for item in coffee_type['ingredients']:
                if coffee_type['ingredients'][item]>resources['ingredients'][item]:
                      print(f'Sorry there\'s shortage of {item}')
                      return False
                else:
                      return True
        if check_resources(coffee_type['ingredients']):
         def calculate_money():
            print('Insert coins')
            five=int(input('How many 5 Rs. coins inserted ? '))
            ten=int(input('How many 10 Rs. coins inserted ? '))
            twenty=int(input('How many 20 Rs. coins inserted ? '))
            total_money=five*5+ten*10+twenty*20
            return total_money


         money=calculate_money()
         def is_payment_successful(money,coffee_cost):
             if money>coffee_cost:
                 change=money-coffee_cost
                 print('Payment successful')
                 print(f'Here\'s your change of Rs.{change}')
                 resources['profit']+=coffee_cost
                 return True
             elif money<coffee_cost:
                 print('Sorry,Money is insufficient,Your money is refunded')
                 return False
             else:
                 resources['profit'] += coffee_cost
                 print('Payment successful !!')
                 return True
         if is_payment_successful(money,coffee_type['cost']):
             def make_coffee(choice,order_ingredients):
                 for item in order_ingredients:
                     resources['ingredients'][item]-=order_ingredients[item]
                 print(f'Here\'s your {choice}')


             make_coffee(choice,coffee_type['ingredients'])



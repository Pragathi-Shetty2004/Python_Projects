import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator():
    n1=float(input('Enter First number'))

    calculation={
        '+':add,
        '-':sub,
        '*':prod,
        '/':div
    }
    continuation=True
    while continuation:
        for i in calculation:
            print(i)
        operation = input('Enter operation')
        n2=float(input('Enter next number'))
        i=calculation[operation]
        output=i(n1,n2)
        print(f'{n1}{operation}{n2}={output}')
        c=input(f'If you want to continue with {output} enter "y",else type "n" to start from first,or enter"x" to exit')
        if c=='y':
            n1=output
        elif c=='n':
            continuation=False
            os.system('cls')
            calculator()
        else:
            continuation=False
calculator()



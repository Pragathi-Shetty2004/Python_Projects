import string
#text=input('Type encrypt for encryption and decrypt for decryption ')
condition=True
while condition !=False :
    text = input('Type encrypt for encryption and decrypt for decryption ')
    Message = input('Type ur message')
    length = len(Message)
    Shift_Number = int(input('Type the shift number'))
    l1 = list(string.ascii_lowercase)
    l2 = list(string.ascii_uppercase)


    def alphabet_position(letter):#u can also use .index() function
        if(letter.isupper()):

            return ord(letter)-ord('A')
        else:
             return ord(letter)-ord('a')
    def encrypt():
        New_Msg=""
        for char in Message:
              if char == " ":
                  New_Msg += " "
              elif char.isalpha():
                  #print(Message.index(char))
                  e = (alphabet_position(char) + Shift_Number) % 26# mod 26 helps to keep letters within loop of 26 letters i.e after z it returns to 'a'
                  if(char.isupper()):
                       New_Msg +=l2[e]
                  else:
                      New_Msg += l1[e]
        print(f'Here\'s the encrypted result:{New_Msg}')
    def decrypt():

        #print(f'Here\'s the encrypted result:{New_Msg}')
        decrypted_Msg=""
        for char in Message:

            if(char== " "):
                decrypted_Msg+=" "
            elif char.isalpha():
                d = alphabet_position(char) - Shift_Number

                if (d < 0):
                    d += 26
                    #print(f'{d}is after add')
                d = d % 26
                if (char.isupper()):
                    decrypted_Msg += l2[d]
                else:
                    decrypted_Msg += l1[d]

        print(f'Here\'s the decrypted result:{decrypted_Msg}')
    if text == 'encrypt':
        encrypt()
    elif(text == 'decrypt'):
        decrypt()
    condition = input('If you want to continue type yes,else type no').lower()
    if condition == 'yes':
         condition = True
    else:
        condition = False





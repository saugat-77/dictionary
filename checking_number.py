def phone_number(number):


        if len(number)>=10:

        # for i in range (1):
            if (number[0]== '9' and number[1]=='8'):
                return True


message=input('enter your message with phone number: ')

for i in range (len(message)):
    chunk=message[i:i+10]
    
    if phone_number(chunk):
#        if (chunk.is_integer()):
        print('the number is: ' +chunk)
        
#this can also be donw by using regular expression
import re

message=input('enter message along with your phone number')

phoneNumRegex = re.compile(r'98\d\d\d\d\d\d\d\d')
mo = phoneNumRegex.search(message)
print('Phone number found: ' + mo.group())

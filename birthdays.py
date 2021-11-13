birthdays={'anita':'shrawn 28','simran':'magh 1','rakshya':'march 1',
            'preethuja':'march 4','shreya':'bhadra 24','sumaly':'december 28','namuna':'shrawn 31', 'vedisha':'bhadra 22', 'sushan-thapa':'mangsir 13', 'goli':'falgun 10', 'rizuta':'falgun 4'
}	

while True:
    print("enter the name of your friend or press enter to exit")
    name=input()
    if name=="":
        break

    if name in birthdays:
        #print("happy birthay"+name)
        print(birthdays[name] + ' is the birthday of ' + name)
        print("\n")

    else:
        print(name+ "'s birthday is not registered.Please register below")
        print("when is their birthday?")
        bday=input()
        if bday=="":
            break
        birthdays[name]=bday
        print("database updated")

print(birthdays)    #yesto garda curently chai database ma update huncha

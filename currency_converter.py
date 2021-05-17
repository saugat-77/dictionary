dictionary={}

with open('currency_value_x-rates.txt') as f:       #name of your file where you have your currency list
    currency_value_file = f.readlines()

for line in currency_value_file:
    parsed= (line.split('\t'))
    dictionary[parsed[0]]=parsed[1]

print('we have following information:\n')
for v in dictionary.keys():
    print(v)
print()    

value=input('enter the country currency you want to convert to: ')
amount=int(input('how much amount you have in nepali: '))

print(f'The {amount} in NRS is equivalent {amount*float(dictionary[value])} in {value}')

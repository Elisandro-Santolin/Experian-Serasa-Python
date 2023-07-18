# 3. Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.

D = {'pares': [], 'impares':[]}
counter = 0

storage = {
        'pares': [], 
        'impares':[]
          }

while (counter <= 10): 
    number = int(input("Digite um número: "))
    if (number % 2 == 0):
        storage['pares'].append(number)    
    else:
        storage['impares'].append(number)
    counter += 1

print(storage)
# 4. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio.
# (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.
 

def checker(number):
    sum = 0

    for i in range(1, number):
        if (number % i == 0):
            sum += i
    if (sum == number):
        return True
    else:
         return False

num = int(input('Digite um número: '))

if checker(num):
     print(f'O número{num}é perfeito.')
else:
     print(f'O número{num}não é perfeito.')

# 2. Faça um código que leia um número informado pelo usuário e que ao final informe se o número é par ou ímpar.

number = float(input('Digite um número: '))

if(number%2 == 0):
    print('O número digitado é par!',number)
else:
    print('O número digitado é ímpar!', number)
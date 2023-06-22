# 1. Desenvolva um programa que leia dois números e informe o maior deles.

number1 = float(input('Digite um número: '))
number2 = float(input('Digite outro número: '))

if(number1 > number2):
    print('O primeiro número é maior que o segundo número.')
elif(number1 < number2):
    print('O primeiro número é menor que o segundo número.')
elif(number1 == number2):
    print('O primeiro número é igual ao segundo número.')
else:
    print('Você não digitou um número')
# 5. Escreva um programa que calcule um aumento de salário. No programa o usuário deve ser capaz de inserir o valor atual do salário, a porcentagem de aumento que receberá e o programa deverá informar ao final o novo valor do salário e qual o valor do acréscimo do salário.

payment = float(input('Digite seu salário atual: '))
percent = float(input('Digite a porcentagem de aumento: '))

wage = (payment*percent)
totalWage=(payment+wage)

print('O valor do salário com o aumento é:',totalWage)


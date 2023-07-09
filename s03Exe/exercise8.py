# 8.Faça um script que leia números do usuário, enquanto ele não digitar 0. Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0,  O valor máximo e o valor mínimo.

numbers = []

while True:
  number = int(input('Digite um número:'))
if (number == 0):

numbers.append(number)

if len(numbers) > 0:
    numbers_quantity = len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)

else:
print('Nada foi digitado')
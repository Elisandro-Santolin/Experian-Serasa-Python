# 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade de divisores desse número e quais são eles.

number = (input('Digite um número: '))
number_dividers = []

for i in range(1, number + 1):
  if (number%i == 0):
     number_dividers.append(i)

len_dividers = len(number_dividers)
print('Os divisores são: ', number_dividers,len_dividers)
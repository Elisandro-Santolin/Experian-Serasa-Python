# 1. Escreva uma função que retorne o maior número entre dois números.
 
number  = float(input('Digite um número: '))
number2 = float(input('Digite outro número: '))

def verification(number, number2):
    if (number > number2):
         print('O maior número é:', number)
    elif (number2 > number):
         print('O maior número é:', number2)
    else:
         print('Os número são identicos')

verification(number, number2)
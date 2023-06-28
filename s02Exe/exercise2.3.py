# 3. Partindo da solução da questão anterior. Crie um programa que calcule o quadrado de um número quando ele for par e que calcule o cubo do número caso ele seja ímpar.

number = float(input('Digite um número: '))

if(number%2 == 0):
    numberScared = (number**2)
    print(f'Número digitado ao quadrado:',numberScared)
else:
    numberCubed = (number**3)
    print(f'Número digitado ao cubo:',numberCubed)
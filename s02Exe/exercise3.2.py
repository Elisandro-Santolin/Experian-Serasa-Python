# 2. Escreva um programa em que o usuário informará qual o último número a imprimir. E esse programa deverá mostrar apenas os números ímpares entre 1 e o número definido pelo usuário.

number  = float(input('Digite o último número da sequência: '))
counter = 1

while (counter <= number):
    print(counter)
    counter = counter +1
    
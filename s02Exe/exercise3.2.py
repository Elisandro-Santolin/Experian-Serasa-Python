# 2. Escreva um programa em que o usuário informará qual o último número a imprimir. E esse programa deverá mostrar apenas os números ímpares entre 1 e o número definido pelo usuário.

number  = float(input('Digite o último número da sequência: '))
counter = 0

while (counter < number):
    counter = counter +1
    if(counter%2 != 0):
        print(counter)
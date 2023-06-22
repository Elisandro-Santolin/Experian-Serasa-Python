# 1. Faça um programa que escreva a contagem regressiva do lançamento de um foguete. O programa deve imprimir na tela a sequência regressiva de 10 até 0 e 'Fogo!'.

from time import sleep
print('######## CONTAGEM REGRESSIVA ########')
counter = 10

while (counter >= 0):
    print(counter)
    counter = counter -1
    sleep(1)
 
print('Fogo!')

# https://docs.python.org/pt-br/3.9/library/time.html




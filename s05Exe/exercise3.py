# 3. Faça um programa para imprimir
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor x inteiro como parâmetro e imprima 
# uma linha com 1 até x. 
# Se x = 1 na função, imprime:
# 1
# Se x = 2 na função, imprime:
# 1   2

def print_out(number):
     for x in range(1, i + 1):
        print(x, end='')
     print()

n = int(input('Informe o número: '))

for i in range(1,n + 1):
    print_out(i)
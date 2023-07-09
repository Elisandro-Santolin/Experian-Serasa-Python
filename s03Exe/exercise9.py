# 9.Faça um script que informe o fatorial de um número. Utilize obrigatoriamente o comando for

number = float(input('Digite o número para ser fatorado: '))
number_factorial = 1

for i in range(1, number+1):
    number_factorial *= i

print(number_factorial)



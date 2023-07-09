# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.

number = float(input('Digite um número: '))
sum = 0
for i in range(1, number + 1):
   sum += i
 
print('A soma dos números é: ',sum)
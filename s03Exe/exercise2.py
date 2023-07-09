# 2. Crie uma lista com os números pares de 0 a 20 e em seguida atenda os seguintes comandos:
# a) Inverta a ordem dos elementos da lista.
# b) Inverta a ordem dos elementos da lista.
# c) Remova os números múltimos de 5 da lista.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list.sort(reverse=True)
for number in list:
  if(number %5 == 0):
      list.remove(number)
print(list)
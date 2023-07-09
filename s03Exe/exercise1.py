# 1. Adicione os números de 1 a 10 à lista "minha_lista" utilizando um loop, em seguida imprima esses valores na tela e por fim mostre o tamanho dessa lista.

my_list = []
for number in range(1, 11):
   my_list.append(number)

size_list = len(my_list)

print('Os itens da lista são: ',my_list)
print('A lista tem esse tamanho: ',size_list)


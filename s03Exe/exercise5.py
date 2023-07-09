# 5. Crie uma lista chamada "lista_repetida" com 5 repetições da lista "lista_concatenada".

my_list = []
for number in range(1, 11):
   my_list.append(number)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
concatenated_list = list + my_list

extended_list = (concatenated_list * 5)
print(extended_list)
# 6. Copie a lista "lista_concatenada" para uma nova lista chamada "copia_lista_concatenada" sem utilizar o operador de atribuição direta.

my_list = []
for number in range(1, 11):
   my_list.append(number)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
concatenated_list = list + my_list

concatenated_list_copy = concatenated_list.copy()

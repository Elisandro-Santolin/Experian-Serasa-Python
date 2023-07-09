# 3. Crie uma lista chamada "lista_concatenada" que seja a concatenação das listas criadas na questão 1 e na questão 2.

my_list = []
for number in range(1, 11):
   my_list.append(number)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
concatenated_list = list + my_list

print(concatenated_list)
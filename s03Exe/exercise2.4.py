# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".

term = (input('Digite uma palavra: '))
list_term = list(term)
list_term = list_term[::-1]
term = "".join(list_term)

print(term)
# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N. Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)

number = float(input('Digite um número: '))

if (number%2 == 0):
    number_pair = list(range(number, -number-1, -2))
else:
     number_pair = list(range(number-1, -number-1, -2))
for number in number_pair:
    print(number)

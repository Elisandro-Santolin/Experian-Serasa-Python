# 2. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

number = int(input("Digite um número: "))

def inverter(number):
    inverted = int(str(number)[::-1])
    return inverted
print(inverter(number))

# registrar novo fornecedor

def registration(supllier):
    identificador = int(input('Id? '))
    name = (input('Nome? '))
    idade = int(input('Idade? '))
    supllier.append((identificador, name, idade))
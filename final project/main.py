def options():
    print('''Escolha uma opção:

    1. Cadastrar Fornecedor
    2. Listar Fornecedores
    3. Procurar dados Fornecedor
    4. Deletar Fornecedor
    ''')

def main():
    supplier = []

    while True:
        options()
        option = int(input('Selecione uma opção: '))
        if (option == 1):
            registration(supplier)
        elif (option == 2):
            display(supplier)
        elif (option == 3):
            search(supplier)
        elif (option == 4 and len(supplier) != 0):
            delete(supplier)
        else:
            print('Opção inválida')

def registration(supllier):
    identifier = int(input('Informe ID: '))
    name  = (input('Informe Nome: '))
    phone = (input('Informe Telefone: '))
    mail  = (input('Informe E-mail:  '))
    supllier.append((identifier, name, phone, mail))

def display(supplier):
    for supplier in supplier:
        identifier, name, phone, mail = supplier
        print(f'id: {identifier}, nome: {name}, telefone: {phone}, email: {mail}')


def search(supplier):
    identifier_search = input('Id? ')
    for supplier in supplier:
        identifier, name, phone, mail = supplier
        if (identifier == identifier_search):
            print(f'id: {identifier}, nome: {name}, telefone: {phone}, email: {mail}')
            break
    else:
        print(f'{identifier_search} não localizado')

def delete(supplier):
    delete_search = input('Id? ')
    for supplier in supplier:
        identifier, name, phone, mail = supplier
        if (identifier == delete_search):
            print(f'id: {identifier}, nome: {name}, telefone: {phone}, email: {mail}')
            break
    else:
        print(f'{delete_search} não localizado')

main()




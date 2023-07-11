# listar os fornecedores existentes 

def listar(supplier):
    for supplier in supplier:
        identificador, nome, idade = supplier
        print(f'Nome: {nome}, idade: {idade}, id: {identificador}')
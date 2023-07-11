# código principal onde tudo funciona

from menu import options
from supplier_registration import registration
from supplier_search import listar

def main():
    pessoas = []

    while True:
        options()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        elif opcao == 4:
            deletar(pessoas)
        else:
            print('Opção inválida')
# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

counter = 0
storage = {
     'name': [],
     'price': []
          }

while (counter <= 3):
    name_product = input('Digite nome do produto: ')
    storage['nome'].append(name_product)
    price_product = float(input('Digite o preço: '))
    storage['preco'].append(price_product)
    counter += 1

print('Dados inseridos: ')
for i in range(len(storage['nome'])):
    name = storage['nome'][i]
    price = storage['preco'][i]
    print(f'Produto: {name} | Preço: R${price:.2f}')
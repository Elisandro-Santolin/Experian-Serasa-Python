# 2. Faça um script que receba os valores do nome, idade e e-mail de uma pessoa e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. Exiba as informações desse dicionário

name  = (input('Informe nome: '))
age   = int(input('Informe idade: '))
email = (input('Informe email: '))

storage = {
        'nome' : [],
        'idade': [],
        'email': []
             }

storage['nome'].append(name)
storage['idade'].append(age)
storage['email'].append(email)

print(storage)
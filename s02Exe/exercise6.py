# 6. Faça um programa que peça o nome e a idade do usuário e que ao final informe o ano de nascimento da pessoa.

name = str(input('Digite seu nome: '))
age  = int(input('Digite sua idade: '))
currentYear = 2023

birth = (currentYear - age)

print('Nome informado',name,'e o ano de nascimento é',birth)
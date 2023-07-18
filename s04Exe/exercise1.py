# 1. Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados
# pelo nome do aluno. Sabe-se que IMC = peso/altura**2
# print('Calculando o IMC dos alunos')

classes = []
option = 'S'

while (option == 'S'):
    name = (input('Insira o nome: '))
    weight = float(input('Insira o peso: '))
    height = float(input('Insira a altura: '))
    student_imc = (height/weight ** 2) 
    student_imc *= 1000
    student_imc = '{:.2f}'.format(student_imc)
    classes.append({'Nome': name, 'altura': height, 'peso': weight, 'imc': student_imc})

    ordered = sorted(classes, key=lambda x: x['nomes'])

    for student in ordered:
        name   = student['nome']
        height = student['peso']
        weight = student['altura']
        imc    = student['imc']

    print(f'Nome: {name} - IMC: {imc}')
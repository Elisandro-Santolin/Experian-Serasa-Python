# 4. Faça um programa que receba 3 notas de prova de um aluno, calcule a média e diga se ele foi aprovado ou reprovado. A média para aprovação é de pelo menos 6 (aprovado se média maior ou igual a 6).

studentGrade1 = float(input('Digite a primeira nota do aluno: '))
studentGrade2 = float(input('Digite a segunda nota do aluno: '))
studentGrade3 = float(input('Digite a terceira nota do aluno: '))

average = ((studentGrade1+studentGrade2+studentGrade3)/3)

if(average >= 6.0):
    print(f'Aluno aprovado com média -> {average:.2f}')
elif(average >= 5.0 and average < 6.0):
    print(f'Aluno em recuperação com média -> {average:.2f}')
else:
    print(f'Aluno reprovado com média -> {average:.2f}')
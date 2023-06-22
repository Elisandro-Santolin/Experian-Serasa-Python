# 5. Escreva um program que leia dois números e que pergunte qual operação o usuário deseja realizar. Esse programa deve aceitar como respostas a soma(+), a subtração(-), a multiplicação (*) e a divisão (/). Ao final, o programa deve exibir o resultado da operação escolhida.

number1 = float(input('Digite um valor: '))
number2 = float(input('Digite outro valor: '))

operation = (input('Digite a operação '))

if(operation == '+'):
    sum = (number1+number2)
    print('O resultado da soma é:',sum)
elif(operation == '-'):
    subtraction = (number1-number2)
    print('O resultado da subtração é:',subtraction)
elif(operation == '*'):
    multiplication = (number1*number2)
    print('O resultado da multiplicão é:',multiplication)
elif(operation == '/'):
    division = (number1/number2)
    print('O resultado da divisão é:',division)
else:
    print('Opção não localizada!')

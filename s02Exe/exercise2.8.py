# 8. Uma empresa concederá aumento de salário aos seus funcionários de acordo com o cargo.

# |Cargo | Aumento (%) |
# |--- |--- |
# |Gerente Geral | 30 |
# |Gerente de Relacionamento | 30 |
# |Analista | 25 |
# |Assistente de Atendimento | 20 |

# Crie um programa que solicite o salário e o cargo do funcionário. O programa deve calcular e imprimir o novo salário. Caso o cargo informado não esteja na tabela, o programa deve imprimir "Cargo inválido".

payment = float(input('Digite o seu salário: '))
adjustedPayment = 0
office =  (input('Selecione o seu cargo:\n1 |Gerente Geral\n2 |Gerente de Relacionamento\n3 |Analista\n4 |Assistente de Atendimento\n'))

if(office == '1'):
    adjustedPayment = (payment*(30/100)+payment)
    print(f'1 |Gerente Geral, salário aplicado aumento: {adjustedPayment:.2f}')
elif(office == '2'):
    adjustedPayment = (payment*(30/100)+payment)
    print(f'2 |Gerente de Relacionamento, salário aplicado aumento: {adjustedPayment:.2f}')
elif(office == '3'):
    adjustedPayment = (payment*(25/100)+payment)
    print(f'3 |Analista, salário aplicado aumento: {adjustedPayment:.2f}')
elif(office == '4'):
    adjustedPayment = (payment*(20/100)+payment)
    print(f'4 |Assistente de Atendimento, salário aplicado aumento: {adjustedPayment:.2f}')
else:
    print('Opção não localizada.')
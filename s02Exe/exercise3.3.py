# 3. Imagine o sistema de um caixa eletrônico. Construa um programa que receba um senha e 
# que essa senha tenha que ser validada. Considere que a senha é **123456**. Existem as seguintes restrições:
# - Ao acertar a senha, a mensagem a ser exibida é: "Olá! Seja bem-vindo ao banco!"
# - Quando o usuário errar a senha pela primeira vez, mostrar a mensagem: "Senha incorreta! 
# Você ainda tem 2 tentativas."
# - Se o usuário errar a senha pela segunda vez, mostrar: "Senha incorreta! Você ainda tem 1 tentativa."
# - Se o usuário errar a senha novamente, mostrar a mensagem "Sua senha foi bloquada! 
# Por favor, dirija-se a agência".
# senha_correta = '123456'
# senha_digita = input('Insira sua senha: ')
# tentativas = 3

attempts = 3 

while(attempts > 0):
    passwordValid = '123456'
    entryPassword = (input('Digite a sua senha: '))

    if(entryPassword == passwordValid):
            print('Olá! Seja bem-vindo ao banco!')
            break
    elif(entryPassword != passwordValid and attempts == 3):
            print('Senha incorreta! Você ainda tem 2 tentativas.')
            attempts = attempts -1
    elif(entryPassword != passwordValid and attempts == 2):
            print('Senha incorreta! Você ainda tem 1 tentativas.')
            attempts = attempts -1
    elif(entryPassword != passwordValid and attempts == 1):
            print('Sua senha foi bloquada! Por favor, dirija-se a agência.')
            attempts = attempts -1
            break
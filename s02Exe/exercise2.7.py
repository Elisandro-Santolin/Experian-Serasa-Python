# 7. Suponha que determinado usuário possua 2 logins em uma rede corporativa.

# |Login 1 | Login 2 |
# |--- |--- |
# |usuario: jardim | usuario: cordeiro |
# |senha: flores1206 | senha: la1506 |

# Escreva um programa que valide o acesso do usuário na rede. Caso o par usuário e senha estejam corretos, o programa deve imprimir a mensagem: "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".

login1 = ('jardim')
login2 = ('cordeiro')

password1 = ('flores1206')
password2 = ('la1506')

print('########## ACESSO A REDE ##########')

entryLogin = (input('Digite sua seu login: '))
entryPassword = (input('Digite sua senha: '))

if(entryLogin == login1 and entryPassword == password1):
    print('Seja bem vindo!')
elif(entryLogin == login2 and entryPassword == password2):
    print('Seja bem vindo!')
else:
    print('Usuário e senha não conferem.')
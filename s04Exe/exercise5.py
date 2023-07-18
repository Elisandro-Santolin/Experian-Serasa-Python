# 5. Escreva um programa que conta a quantidade de vowels em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.

text = (input('Digite um texto: '))

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in text:
   if letter.lower() in vowels:
         vowels[letter.lower()] += 1

print('Quantas vogais tem no texto?')
for vowel, quantity in vowels.items():
    print(f'{vowel}: {quantity}')
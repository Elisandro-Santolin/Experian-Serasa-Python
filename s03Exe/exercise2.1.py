# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.

text = (input('Digite uma palavra: '))
text_length = len(text)
counter = 0
index = 0

while(counter < text_length):
    print(text[index])
    counter += 1
    index += 1
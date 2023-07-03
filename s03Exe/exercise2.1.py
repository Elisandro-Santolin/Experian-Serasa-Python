# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.

text = (input('Digite apenas uma palavra: '))
textLength = len(text)
counter = 0
index = 0

while(counter < textLength):
    print(text[index])
    counter += 1
    index += 1
# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto.

text = (input('Digite um pequeno texto: '))
term = (input('Digite uma palavra para localizar no texto: '))
location_term = text.find(term)

if (len(term) > 0):
    print('Palavra localizada')
else:
   print('Palavra não localizada')
# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'

def changed_text(text):
    text = text.replace('a', '4')
    text = text.replace('e', '3')
    text = text.replace('I', '1')
    text = text.replace('t', '7')
    return text

term = (input('Digite uma palavra: '))
term_new = changed_text(term)

print('Nova palavra', term_new)
# 1. Construa um programa  em que o usuário informe a estatura em metros e o programa converta para centímetros.

height = float(input('Digite sua altura: '))
converter = (height * 100)

print(f'Sua altura em metros, convertida é {converter:.2f} centimetros.')
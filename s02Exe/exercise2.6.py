# 6. Escreva um programa que pergunte a distância que determinado passageiro deseja percorrer em km. A partir disso calcule o preço da passagem. É cobrado 0,50 centavos por km para viagens de até 300 km. E 0,45 centavos para viagens mais longas.


kilometer = float(input('Digite quando km deseja percorrer: '))

if(kilometer <= 300):
    value = (kilometer*0.50)
    print(f'O preço da passagem é: {value:.2f}')
else:
    value = (kilometer*0.45)
    print(f'O preço da passagem é: {value:.2f}')
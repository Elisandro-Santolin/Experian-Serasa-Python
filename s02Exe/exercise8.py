# 8. Uma mobiliária paga aos seus corretores um salário base de 1500 Reais. Além disso, uma comissão de 200,00 Reias por cada imóvel vendido e 5% do valor de cada venda. Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas. Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.

payment = 1500.00
bonus = 200.00

salesValue = float(input('Informe o valor total de vendas: '))
percent = (5/100)
commission = (salesValue*percent)

salesQuantity = int(input('Informe quantos imóveis foram vendidos: '))
bonusTotality = (salesQuantity*bonus) 

paymentTotality = (payment+commission+bonusTotality)

print(f'O total do salário é:{paymentTotality:.2f}')
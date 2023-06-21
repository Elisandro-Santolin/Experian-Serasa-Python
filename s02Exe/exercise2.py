# 2. Construa um programa que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido(em segundos). Ao fim, calcule a velocidade média.
# Obs.: velocidade_media = variação_do_deslocamento/tempo_percorrido

meters  = float(input('Digite variação de deslocamento em metros: '))
seconds = float(input('Digite a variação do tempo em segundos: '))

velocityAverange = (meters/seconds)

print('A velocidade média do objeto é:', velocityAverange)
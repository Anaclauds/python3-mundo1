"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$07,00 por cada km acima do limite"""

velocidade = float(input('Qual a velocidade?'))
if velocidade > 80:
    excesso = velocidade - 80
    multa = 7 * excesso
    print('Você foi multado! O valor da sua multa é: {:.2f}'.format(multa))
else:
    print('Você não estava acima do limite de velocidade!')

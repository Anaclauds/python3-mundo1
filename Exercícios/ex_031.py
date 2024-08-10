"""Desenvolva um programa e pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas"""

"""distancia = float(input('Qual a distancia da viagem em Km?'))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O valor da sua passagem é: {:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O valor da sua passagem é: {:.2f}'.format(passagem))"""

#método mais simplificado para resolver:
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

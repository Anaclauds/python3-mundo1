#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considerando US$1,00 = R$3,27
valor = float(input('Insira um valor: '))
quantidade = valor/3.27

print('Você pode comprar {:.2f} dólares'.format(quantidade))

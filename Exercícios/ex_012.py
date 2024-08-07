#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Insira o preço do produto: '))
preco_com_desconto = preco - ((5/100)*preco)

print('O novo preço é:R${:.2f}'.format(preco_com_desconto))

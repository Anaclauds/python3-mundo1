#Faça um programa que leia a largura e a altura de uma parede, em metros, calcule sua área e a quantidade
#de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m^2
largura = float(input('Insira a largura: '))
altura = float(input('Insira a altura: '))
area = largura * altura
quantidade = area/2

print('Área é: {} m^2\nA quantidade de tinta necessária é: {} litros'.format(area, quantidade))

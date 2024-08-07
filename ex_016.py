#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Há 3 formas diferentes para resolver esse exercício:

#resolvendo o exercício importando uma biblioteca inteira
'''import math
num = float(input("Qual o número?"))
print("O número {} tem uma parte inteira que é {}".format(num,math.trunc(num)))'''

#resolvendo o exercício importando apenas a funcionalidade desejada da biblioteca
'''from math import trunc
num = float(input("Qual é o número?"))
print("O número {} tem uma parte inteira que é: {}".format(num, trunc(num)))'''

#resolvendo o exercício sem importar uma biblíoteca
num = float(input("Qual é o número?"))
print("O número {} tem uma parte inteira que é: {}".format(num, int(num)))



"""Desenvolva um programa que leia um comprimento de três retas e diga ao usuário se elas pode ou não formar
um triângulo. Pesquisar o princípio matemático para a formação de triângulos"""
r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira retra: '))
if (r1 + r2 > r3) and (r1 + r3> r2) and (r3 + r2 > r1):
    print('Temos um triângulo!')
else:
    print('Não temos um triângulo!')
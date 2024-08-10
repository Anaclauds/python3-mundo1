"""Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar"""
numero = int(input('Insira um número inteiro: '))
if numero % 2 == 0:
    if numero == 0:
        print('Este é um número neutro!')
    else:
        print('Este número é par!')
else:
    print('Este número é ímpar!')

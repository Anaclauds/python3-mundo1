"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO"""
from datetime import date
ano = int(input('Insira um ano ou 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este é um ano bissexto!')
else:
    print('Este não é um ano bissexto!')




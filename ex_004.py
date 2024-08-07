#Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
#possíveis sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(a))), """forma aceitável a partir do python 3.7"""
print('Só tem espaços? ', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É letras maiúsculas? ', a.isupper())
print('É letras minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())


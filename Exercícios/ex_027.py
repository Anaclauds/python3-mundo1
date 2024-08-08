"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza"""
n = input('Digite seu nome completo: ').strip()
nome = n.split()
print('O primeiro nome: {} '.format(nome[0]))
print('O último nome: {} '.format(nome[len(nome)-1])) #pega o len que sabe o tamanho da posição e diminui 1
#pois começa em 0

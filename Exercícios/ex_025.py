"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" ou não no nome"""
nome = input('Insira seu nome completo: ').strip() #para evitar espaços extras
print('SILVA' in nome.upper().split()) #split para dividir as palavras e não reconhecer nomes como "SILVANA"


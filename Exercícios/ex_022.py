"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas

- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome"""

nome = input("Qual o seu nome?")
print('O nome com todas as letras maiúsculas é: {}'.format((nome.upper())))
print('O nome com todas as letras minúsculas é:', nome.lower())
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #subtrai pela quantidade de espaços

#outra forma de resolver
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



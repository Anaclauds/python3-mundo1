#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice
nome1 = str(input('Primeiro aluno(a): '))
nome2 = str(input('Segundo aluno(a): '))
nome3 = str(input('Terceiro aluno(a): '))
nome4 = str(input('Quarto aluno(a): '))
listadealunos = [nome1,nome2, nome3, nome4]
escolhido = choice(listadealunos)
print('O aluno sorteado foi {}'.format(escolhido))

"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

"""print('O computador está pensando em um número...tente adivinhar!')
n = int(input('Qual número inteiro você acha que o computador pensou?'))
if n == 5:
    print('Parabéns, você adivinhou!')
else:
    print('Número errado!')"""

#uma forma mais completa de resolver:
from random import randint
from time import sleep
computador = randint(0,5) #faz o computador sortear um número entre 0 e 5
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #Tentativa do jogador
print('PROCESSANDO...')
sleep(3) #tempo até aparecer a resposta
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))

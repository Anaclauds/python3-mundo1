nome = input('Qual o seu nome?')
print('Prazer em te conhecer{:=^20}!'.format(nome)), """Dessa forma, é possível centralizar ou alinhar"""

#Se a variável não vai ser utilizada depois, pode-se concatenar:
n1= int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma é:{}'.format(n1+n2))

#Também é possível:
n1= int(input('Um valor: '))
n2= int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisão é{:.3f}'.format(s, m, d)), """Passando 3f se lê 3 casas flutuantes"""
print('Divisão inteira {} e portência {}'.format(di, e))

#No final da linha , end=' ', não quebra a linha
# \n quebra a linha

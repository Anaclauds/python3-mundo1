"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez"""
frase = input('Insira uma frase aleatória: ').upper().strip()
print("A letra A aparece {} vezes".format(frase.count('A')))
print("Ela aparece a última vez na posição: {}".format(frase.find('A')+1)) #find para achar a primeira posição de A
#pois, a primeira posição é 0 para o sistema
print("Ela aparece a última vez na posição: {}".format(frase.rfind('A')+1)) #Rfind - da direota para esquerda

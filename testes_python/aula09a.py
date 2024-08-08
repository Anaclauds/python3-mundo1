#FATIAMENTO
#Quando está se trabalhando com fatiamento de string, elas são divididas em pequenos blocos
#ao escrever frase[9:13] é preciso lembrar que serão retornados os caracteres de 9 à 12, pois
#o último valor do range de caracteres não é contabilizado no retorno sendo sempre N-1

#Ao ler: frase[9:21:2]
# 9 é a posição inicial
# 21 é a posição final (n -1)
# 2 é a quantidade de vezes que irá "pular", o número na próxima posição não será contado

#Ao ler: frase[:5]
#Significa que serão considerados todas as posições do início até a posição 5
#se fosse ao contrário, iria também até o final da string

#Ao ler: rase[8::3]
#Significa que irá iniciar no 8, irá até o final, pegando sempre a terceira posição na contagem pulada

#ANÁLISE
#lean(frase) - verifica o comprimento da frase
#frase.count('o') - conta quantas vezes aparece o caractere escolhido
#frase.count('0', 0, 13) - faz a contagem já com o fatiamento
#frase.find('deo' - indica em que posição começou esses caracteres
#- se coloca uma string inexistente na frase, retorna -1
#'Curso' in frase - retorna true ou false se a condição for verdadeira

#TRANSFORMAÇÃO
#frasse.replace('Python', 'Android') - substitui a primeira palavra pela segunda, não precisa ter a mesma quantidade
#não substitui em todas as estancias se vc não salvar dentro da variável
#frase.upper() - transforma tudo em maiúsculo
#frase.lower() - transforma tudo em minúsculo
#frase.capitalize() - transforma tudo em minúsculo, mantendo a primeira letra em maiúsculo
#frase.tile() - capitalize em cada palavra da frase
#frase.strip() - remove espaços inúteis no início e no final
#frase.rstrip() - remove os espaços inúteis de rigth (direita)
#frase.lstrip() - remove os espaços inúteis de left (esquerda)

#DIVISÃO
#frase.split() - divide as palavras a partir dos espaços vazios, lista com todas as palavras da cadeia de caracteres

#JUNÇÃO
#'-'.join(frase) - junta todos os alimentos da frase e adiciona o separador passado em aspas

frase = 'Curso em Vídeo Python'
print(frase[::2])

print(frase.upper().count('O'))

divido = frase.split()
print(divido[2][3]) #pega a palavra da segunda posição e o 3 caractere dela

#para printar na tela uma quantidade grande de caracteres, basta adicionar aspas triplas
print("""texto
muito
grande
vou escrever""")


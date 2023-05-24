#MANIPULANDO TEXTOS

frase = 'Curso em video Python'

print(frase[0])
print(frase[0:4])
print(frase[9:21:2]) #vai do 9 ao 21 pulando de 2 em 2
print(frase[:5]) #comeca em 0 e vai até a 5
print(frase[15:]) #vai do 15 até o final
print(frase[9::3]) #vai comecar no nove e vai até o final pulando 3

#ANÁLISE
print('length', len(frase))
print('count no o ->', frase.count('o'))
print('count no o com fatiamento->', frase.count('o', 0, 13)) #vai do 0 até o 12, entao tem só um o

print(frase.find('deo')) #comeca na posicao 11, entao printa 11
print(frase.find('Android')) #retorna -1, entao nao existe

print('Curso' in frase) #Retorna true

print(frase.replace('Python', 'Swift'))

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title()) #capitaliza palavra por palavra

print(frase.strip()) #remove espacos inuteis no comeco e final da string
print(frase.rstrip()) #remove espacos inuteis só nos ultimos espacos
print(frase.lstrip()) #remove espacos inuteis só no comeco, na esquerda

print(frase.split())  #divide a string em varios pedacos
print('-'.join(frase)) #coloca o caracter separando todas as letras

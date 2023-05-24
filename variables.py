#conversao de tipo
abc = 18
abc = str(abc)
print(type(abc))

#inteiro
idade = 18
ano = 2002

print(type(idade))
print(type(ano))

#float

altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))


#TIPO COMPLEXO (complex)
#Usado para representar números complexos -> cálculos geométricos e científicos
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))

#string (str)
nome = 'Aline'
profissao = 'Dev'

print(type(profissao))
print(type(nome))

#boolean
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))

#Listas
#Agrupam conj de elemntos variados, podendo conter inteiros, floats, strings, outras listas e outros tipos.

alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0]

print(type(alunos))
print(type(notas))


#Tuplas (tuple)
#São IMUTAVEIS, após a sua definicao as tuplas nao podem ser alteradas.
# Utilizamos parenteses e virgula.

valores = (90, 79, 54, 32, 21)
pontos = (100, 94.05, 86.8, 62)

print(type(valores))
print(type(pontos))

#dicionários (dict)
#usa estrutura de chave e valor
altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70}
peso = {'Amanda': 60, 'Ana': 58, 'João': 68}

print(type(altura))
print(type(peso))
"""
programa que leia nome, idade e sexo de 4 pessoas. No final, mostre:
- media de idade do grupo
- quantas mulheres tem menos de 20 anos
- qual o nome do homem mais velho
"""

media = 0
soma = 0
nomemaisvelho = ''
maisvelho = 0
menosdevinte = 0
for pessoa in range(1,5):
    nome = str(input("Nome "))
    idade = int(input("idade "))
    sexo = str(input("sexo F/M "))
    print('='*10)
    soma += idade
    if pessoa == 1 and sexo in "Mm":
        nomemaisvelho = nome
        maisvelho += idade
    if idade > maisvelho and sexo in "Mm":
        maisvelho += idade
        nomemaisvelho = nome
    if sexo in "Ff" and idade < 20:
        menosdevinte += 1
media = soma/5
print("A MEDIA DAS IDADES É", media)
print("O NOME DO HOMEM MAIS VELHO É ", nomemaisvelho)
print('QUANTIDADE DE MULHERES COM MENOS DE 20 É', menosdevinte)

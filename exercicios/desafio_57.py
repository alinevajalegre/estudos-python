"""
leia o sexo de uma pessoa, mas so aceite os valores
'M' ou 'F. Caso esteja errado, peça a digitacao
novamente até ter um valor correto
"""

sexo = str(input("Qual é o sexo? "))

while sexo not in 'MF':
    sexo = str(input('Digite novamente: '))

print('Fim')

"""
    leia o ano de nascimento de sete pessoas.
    No final mostre quantas pessoas ainda nao atingiram
    a maioridade e quantas ja sao maiores
"""

from datetime import date

lista = []
data_atual = date.today()
ano_atual = data_atual.year
contador_menor = 0
contador_maior = 0

for i in range(1, 8):
    dt = input("Ano de nascimento da pessoa {} -> ".format(i))
    lista.append(dt)

for value in lista:
    if value > '2005':
        contador_menor += 1
    else:
        contador_maior += 1

print('maiores ->', contador_maior)
print('menores ->', contador_menor)
print(lista)
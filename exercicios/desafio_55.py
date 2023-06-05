"""
leia o peso de cinco pessoas. no final, mostre qual foi o maior
e o menor peso lidos
"""
lista = []

for entrada in range(5):
    entrada = float(input("Digite o peso: "))
    lista.append(entrada)

print('Maior peso lido -> ', max(lista))
print('Menor peso lido -> ', min(lista))
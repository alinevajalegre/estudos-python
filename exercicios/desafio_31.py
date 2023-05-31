"""
Desenvolva um programa que pergunte a distancia de uma
viagem em km, calcule o preco da passagem, cobrando
0,50 por km para viagens de ate 200km e 0,45 para viagens mais longas
"""

distancia = float(input("Qual a distancia? "))

if distancia <= 200:
    preco = 0.50 * distancia
    print('O preco total fica {} para sua viagem de {}kms! '.format(preco, distancia))
else:
    preco = 0.45 * distancia
    print('O preco total fica {} para sua viagem de {}kms! '.format(preco, distancia))
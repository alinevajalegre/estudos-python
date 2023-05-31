"""
Escreva um programa que leia a veloc de um carro.
Se ele ultrapassar 80km/h mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar 7,00 por cada km acima do limite
"""

velocidade = float(input("Qual a velocidade? "))

if velocidade > 80:
    valor_multa = (velocidade-80) * 7
    print("Voce foi multado!, valor da multa -> ", valor_multa)
else:
    print("Voce nao foi multado")
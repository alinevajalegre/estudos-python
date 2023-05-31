"""
Escreva um programa que faca o computador pensar em um num
inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi
o numero escolhido pelo computador.
o programa deve escrever na tela se o usuario venceu ou perdeu
"""
from random import random, randrange

numero = randrange(6)

entrada_usuario = int(input("Digite um numero de 0 a 5 "))

if entrada_usuario < 5 or entrada_usuario > 0:
    if entrada_usuario == numero:
        print("Sua entrada ->", entrada_usuario)
        print("\nNumero escolhido pelo computador ->", numero)
        print("VENCEU")
    else:
        print("Perdeu")
else:
    print("Numero invalido")
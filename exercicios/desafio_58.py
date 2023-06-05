"""
melhore o desafio 28, onde o computador vai pensar em um numero entre 0 e 10. só
que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
"""
from random import randrange

numero = randrange(6)
entrada_usuario = int(input("Digite um numero de 0 a 5 "))

if entrada_usuario < 5 or entrada_usuario > 0:
    while numero != entrada_usuario:
        print('perdeu')
        numero = int(input('Digite um valor: '))
    print('Acertou')
    print('Fim')
else:
    print("Numero invalido")
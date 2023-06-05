"""
    crie um programa que leia dois valores
    e mostre um menu na tela
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa

    seu programa deverá realizar a operacao
    solicitada em cada caso
"""

print('Digite: ')
print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa')

menu = int(input('Qual opcao? '))

while menu != range(1,6):
    print("Digite uma opcao valida: ")

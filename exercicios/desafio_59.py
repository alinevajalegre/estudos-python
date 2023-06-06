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

print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa')
menu = int(input('Qual opcao? '))

while menu not in range(1,6):
    print("Digite uma opcao valida: ")
    menu = int(input('Qual opcao? '))

a = int(input('Digite o valor a: '))
b = int(input('Digite o valor b: '))

if menu == 1:
    soma = a + b
    print('A soma é -> ', soma)
elif menu == 2:
    multiplicacao = a * b
    print('A multiplicacao é -> ', multiplicacao)
elif menu == 3:
    if a > b:
        print('a é maior que b')
    else:
        print('a não é maior que b')

"""
    desenvolva um programa que leia o primeiro termo e a razao
    de uma PA. No final mostre os 10 primeiros termos dessa
    progressao
"""

primeiro_termo = int(input("Qual o 1o termo da PA? "))
razao = int(input("Qual a razao dessa PA? "))
decimo = primeiro_termo + (10-1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')

print('acabou')

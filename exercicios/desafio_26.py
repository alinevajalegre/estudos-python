"""
faca um programa que leia uma frase pelo tecladoe mostre
1- quantas vezes aparece a letra "A"
2- em que posicao ela aparece a primeira vez
3- em que posicao ela aparece a ultima vez
"""
frase = input('Digite a frase ')

#1
print('A letra A aparece -> {} vezes'.format(frase.count('a')))

#2
print('A letra A aparece a primeira vez na posicao -> {}'.format(frase.find('a')))

#3
print('A letra A aparece a ultima vez na posicao -> {}'.format(frase.rfind('a')))

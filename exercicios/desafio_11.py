"""
    Faca um programa que leia a largura e a altura de uma parede em metros
    calcule a sua area e a qtd de tinta necessaria para pinta-la,
    sabendo que cada litro de tinta pinta uma area de 2m quadrados
"""

largura = float(input('Qual a largura da parede? -> '))
altura = float(input('Qual a altura da parede? -> '))

area = largura * altura

qtd_de_tinta = area / 2

print('area -> ', area)
print('qtd_de_tinta -> ', qtd_de_tinta)
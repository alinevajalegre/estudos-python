"""
    Escreva um programa para aprovar um emprestimo bancario p
    a compra de uma casa. O programa vai pergutnar o valor da casa,
    o salario do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestacao mensal, sabendo que ela nao pode
    exceder 30% do salario ou entao o emprestimo será negado
"""

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salario do comprador? "))
anos = int(input("Em quantos anos será parcelado? "))

trinta_porcento = (salario * 30)/100

valor_parcela = valor_casa / (anos*12)

if valor_parcela > trinta_porcento:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado! Serão {} parcelas de {} cada, pagos em {} anos'.format((anos*12),valor_parcela,anos))

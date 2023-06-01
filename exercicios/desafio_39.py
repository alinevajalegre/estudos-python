"""
faca um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

 - se ele ainda vai se alistar ao servico militar
 - se é a hora de se alistar
 - se já passou do tempo do alistamento

 seu programa tambem devera mostrar o tempo que falta ou que passou
 do prazo

"""
idade = int(input("Qual a sua idade? "))

if idade >= 18 and idade <= 21:
    tempo_faltante = 21 - idade
    print("Já é hora de se alistar")
    print("Tempo faltante -> {} ano(s)".format(tempo_faltante))
elif idade < 18:
    print("Voce ainda vai se alistar")
elif idade > 21:
    print("Já passou do tempo")
    tempo_sobra = idade - 21
    print("Tempo que passou do prazo -> {} ano(s)".format(tempo_sobra))
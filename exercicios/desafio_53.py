"""
    leia uma frase qualquer e diga se ela é um palindromo,
    desconsiderando os espaços
"""

frase = str(input("Qual a palavra? ")).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print("PALINDROMO")
else:
    print("NAO")
print('O inverso de {} é {}'.format(junto, inverso))


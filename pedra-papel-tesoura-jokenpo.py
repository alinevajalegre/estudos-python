import random

jokenpo = ["pedra", "papel", "tesoura"]

escolha_programa = random.choice(jokenpo)

input = str(input("pedra, papel ou tesoura? "))

print("="*10)
print("Sua escolha -> ", input)
print("Escolha do computador -> ", escolha_programa)
print("="*10)

if input == escolha_programa:
    print("empate")
elif (input == 'papel' and escolha_programa == 'pedra') or (input == 'tesoura' and escolha_programa == 'papel') or (input == 'pedra' and escolha_programa == 'tesoura'):
    print("Voce venceu! ")
elif (input == 'pedra' and escolha_programa == 'papel') or (input == 'papel' and escolha_programa == 'tesoura') or (input == 'tesoura' and escolha_programa == 'pedra'):
    print("Voce perdeu! ")
else:
    print("Invalido!")
"""
mostre na tela uma contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com uma pausa de um segundo
entre eles
"""

import time

for number in reversed(range(11)):
    time.sleep(1)
    print(number)

vendas = range(1000, 5000)

print(list(vendas))

def bateu_meta(venda):
    if venda > 4000:
        return True
    else:
        return False

bateram_meta = filter(bateu_meta,vendas)
print(list(bateram_meta))


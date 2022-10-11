def metade(v):
    w = v/2

    return w


def dobro(v):
    w = 2 * v

    return w


def aumentar(v, taxa):
    w = (1 + (taxa/100)) * v

    return w


def diminuir(v, taxa):
    w = (1 - (taxa/100)) * v

    return w


#Maneira do professor
def moeda(val=0, simb='R$'):
    return f'{simb}{val:.2f}'.replace('.', ',')


# Maneira que eu fiz
'''
def moeda(num):
    num = f'{num:.2f}'
    dec = num[-2:]
    intei = num[:-3]

    return f'{intei},{dec}'
'''
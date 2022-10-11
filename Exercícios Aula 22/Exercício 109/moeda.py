def metade(v, form=False):
    w = v/2

    if form == True:
        return moeda(w)
    else:
        return w


def dobro(v, form=False):
    w = 2 * v

    if form == True:
        return moeda(w)
    else:
        return w


def aumentar(v, taxa, form=False):
    w = (1 + (taxa/100)) * v

    if form == True:
        return moeda(w)
    else:
        return


def diminuir(v, taxa, form=False):
    w = (1 - (taxa/100)) * v

    if form == True:
        return moeda(w)
    else:
        return w

#Maneira do professor
def moeda(val=0, simb='R$'):
    return f'{simb}{val:.2f}'.replace('.', ',')
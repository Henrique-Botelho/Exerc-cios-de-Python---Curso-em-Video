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


def moeda(val=0, simb='R$'):
    return f'{simb}{val:.2f}'.replace('.', ',')


def resumo(v, ta, td):
    res = dict()
    res['Preço analisado:'] = moeda(v)
    res['Dobro do preço:'] = dobro(v, form=True)
    res['Metade do preço:'] = metade(v, form=True)
    res[f'{ta}% de aumento:'] = aumentar(v, ta, form=True)
    res[f'{td}% de redução:'] = diminuir(v, td, form=True)
    
    
    print('='*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('='*40)
    for c in res.items():
        print(f'{c[0]:<20}{c[1]:>20}')
    print('='*40)
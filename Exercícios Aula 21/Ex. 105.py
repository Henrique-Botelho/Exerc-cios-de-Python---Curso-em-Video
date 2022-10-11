def notas(*n, sit=False):
    """Função para análise de notas de uma sala

    Args:
        *n (float, quantos quiser): o usuário pode colocar quantas notas desejar.
        sit (bool, opcional): apresenta a situação da média de notas da sala. Por padrão fica desativada (False).

    Returns:
        dicionário: o total de notas computadas, a maior nota, a menor nota, a média da sala e a situação da sala.
    """
    sala = dict()
    sala['total'] = len(n)
    sala['maior'] = max(n)
    sala['menor'] = min(n)
    sala['média'] = sum(n)/len(n)
    
    if sit:
        if sala['média'] < 5:
            sala['situação'] = 'RUIM'
        elif 5 <= sala['média'] < 7:
            sala['situação'] = 'RAZOÁVEL'
        else:
            sala['situação'] = 'BOA'
    
    return sala
    

#Programa pricipal
resp = notas(5.5, 2.5, 10, 6.5)
print(resp)
help(notas)
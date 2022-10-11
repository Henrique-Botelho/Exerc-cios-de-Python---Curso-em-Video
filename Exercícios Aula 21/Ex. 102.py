def fatorial(num, show = False):
    """Função de cálculo de fatorial

    Args:
        num (interiro): número o qual se deseja calcular o fatorial
        show (bool, optional): determina se a função irá mostrar para o usuário os números se multiplicando. Por padrão fica desativado (False). Para mostrar, digite True ou show=True.
    """
    print('-=-'*10)
    f = 1
    for c in range(num, 0, -1):
        if show:                
            if c > 1:
                print(f'{c} X', end=' ')
            else:
                print(f'{c} =', end=' ')
            f *= c
        else:
            f *= c
    return f'{f}'

print(fatorial(7, show=True))
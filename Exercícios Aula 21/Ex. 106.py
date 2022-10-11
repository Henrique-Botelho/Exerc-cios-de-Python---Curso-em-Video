def titulo(txt, t, fundo):
    tam = len(txt)
    print(f'\033[{t};{fundo}m')
    print()
    print(f'~'*(tam + 4))
    print(f'  {txt}  ')
    print(f'~'*(tam + 4))
    print(f'\033[m')

def ajuda(l):
    titulo(f'Acessando o manual do comando {l}', 30, 44)
    print('\033[30;47m',end='')
    help(l)
    print('\033[m')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 30, 42)
    esc = str(input('Função ou Biblioteca >'))
    if esc == 'fim':
        break
    ajuda(esc)

titulo('ATÉ LOGO!', 30, 41)

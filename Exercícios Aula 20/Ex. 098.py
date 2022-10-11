from time import sleep

def contagem(i, f, p):
    
    print('-=-'*15)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
        print()

    if i > f:
        for d in range(i, f - 1, -p):
            print(d, end=' ')
            sleep(0.3)
        print()


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
while True:
    passo = int(input('Passo: '))
    if passo > 0:
        break
    print('Inválido!')

contagem(inicio, fim, passo)
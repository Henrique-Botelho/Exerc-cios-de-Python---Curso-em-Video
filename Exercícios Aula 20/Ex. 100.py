from random import randint


def sorteia(ele, lista):
    for c in range(0, ele):
        lista.append(randint(0, 9))
    print(f'Os números sorteados para a lista: ', end='')
    for d in lista:
        print(d, end=' ')
    print()

def somaPar(lista):
    soma = 0
    for e in lista:
        if e % 2 == 0:
            soma += e
    print(f'Somando os valores pares de {lista}, temos {soma} ')

numeros = list()
sorteia(5, numeros)
somaPar(numeros)
# Módulos importados
from random import randint
from time import sleep

# Declaração de variáveis
jogo = []
num = 0

# Título
print('='*50)
print(f'{"JOGA NA MEGA SENA": ^50}')
print('='*50)

# Entrada e dados
jogos = int(input('Quantos jogos você quer que eu sorteie? '))

# Processamento
print(f'{f" SORTEANDO {jogos} JOGOS ":-^50}')

for c in range(1, jogos+1):
    for n in range(1, 7):
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    jogo.sort()
    print(f'Jogo {c} : {jogo}')
    jogo.clear()
    sleep(1)
print(f'{" < BOA SORTE! > ":=^50}')
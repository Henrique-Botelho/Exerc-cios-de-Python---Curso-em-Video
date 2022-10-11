# Declaração de variáveis
time = list()
jogador = dict()
partida = list()
esc = 0

while True:
    # Entrada de dados do jogador
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    partida.clear()
    soma = 0

    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    print('='*30)

    for c in range(1, (partidas + 1 )):
        gol = int(input(f'Quantos gols ele fez na {c}ª partida? '))
        partida.append(gol)
        soma += gol

    jogador['gols'] = partida[:]

    jogador['total'] = soma

    time.append(jogador.copy())

    while True:
        sair = str(input('Quer continuar?(S/N) ')).upper()[0]
        if sair in 'SN':
            break
        print('Inválido!')
    if sair == 'N':
        break

# Tabela com os resultados
print('='*45)

print(f'{"Num.":<6}', end='')
for c in jogador.keys():
    print(f'{c:<15}', end='')
print()
print('='*45)
for k, v in enumerate(time):
    print(f'{k:<6}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

# Análise de dados de cada jogador
while True:
    print('='*45)
    while True:
        esc = int(input('Mostrar dados de qual jogador?(999 interrompe) '))        
        if 0 <= esc < len(time) or esc == 999:
            break
        print('Inválido!')
    
    if esc == 999:
        break
    
    print(f' -- LEVANTAMENTO DO JOGADOR {time[esc]["nome"]}: ')
    for r, s in enumerate(time[esc]['gols']):
        print(f'      ==> No {r + 1}ª fez {s} gols')
    
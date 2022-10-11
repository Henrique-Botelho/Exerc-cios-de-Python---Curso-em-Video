# Declaração de variáveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Título
print('-='*15)
print(f'{"Gerador de Matriz 3x3": ^30}')
print('-='*15)

# Entrada de dados e processamento

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor do elemento [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    
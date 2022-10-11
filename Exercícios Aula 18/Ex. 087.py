# Declaração de variáveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
soma3 = 0
maior = 0

# Entrada de dados
for l in range(0, 3):        
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor do elemento [{l}, {c}]: '))

        # Processamento da soma dos valores pares
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]

        # Processamento da soma dos valores da terceira coluna
        if c == 2:
            soma3 += matriz[l][c]

        # Processamento do maior valor da 2ª linha    
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
       
# A estrutura da matriz
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

# Saída de dados
print('-='*30)
print(f'A soma dos valores pares da matriz é {somap}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')
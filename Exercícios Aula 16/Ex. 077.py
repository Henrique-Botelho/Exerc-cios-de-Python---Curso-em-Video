# Defino minha tupla com algumas palavras
conjunto = ('JOGAR', 'CASA', 'BRINCAR', 'PYTHON', 'MOUSE')

# Crio uma estrura de repetição que me mostra cada palavra
for palavra in conjunto:
    print(f'\nA palavra {palavra} tem a[s] vogal[ais] ', end='')
    # Crio outra estrutua de repetição que agora lê cada letra da palavra e confere se nela há vogais
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')
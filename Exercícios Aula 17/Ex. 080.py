# Declaração de variáveis
maior = 0
menor = 0
lista =[]

# Entrada e processamento
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na poisção {pos} da lista...')
                break
            pos += 1
# Saída
print('='*40)
print('Os valores digitados, em ordem, são ', lista)
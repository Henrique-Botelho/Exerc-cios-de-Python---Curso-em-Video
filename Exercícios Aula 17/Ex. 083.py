# Declaração de variáveis
pilha = []

# Entrada de dados
expr = str(input('Digite uma expressão que contenha parênteses: '))

# Processamento
for ele in expr:
    if ele == '(':
        pilha.append('(')

    elif ele == ')':
        if len(pilha) > 0:
           pilha.pop()
        else:
            pilha.append(')')
            break

# Saída de dados
if len(pilha) == 0:
    print('A sua expressão está correta!')

else:
    print('A sua expressão está errada!')
def leiaInt(texto=''):
    while True:
        l = input(texto)
        if l.isnumeric():
            l = int(l)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
    return l
                

print('-'*30)

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

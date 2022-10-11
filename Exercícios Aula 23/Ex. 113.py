def leiaInt(num):
    while True:
        try:
            w = int(input(num))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não fornecer esse número!\033[m')
            return '<nenhum>'
        else:
            return w
        

def leiaFloat(num):
    while True:
        try:
            w = float(input(num))
        except ValueError:
            print(f'\033[31mERRO! Por favor digite um número real válido!\033[m')
            continue
        else:
            return w


#Programa principal
n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n} e o número real digitado foi {f}.')
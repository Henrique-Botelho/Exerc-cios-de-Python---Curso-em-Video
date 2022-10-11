parada = 'SIM'
total = 0
contador = 0
maior = 0
menor = 0

while parada == 'SIM':
    num = float(input('Digite um número:'))
    total += num
    contador += 1

    if contador == 1:
        maior = num
        menor = num

    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    
    parada = str(input('Quer continuar?\n[qualquer coisa diferente de sim para]')).strip().upper()

print('A média entre os números é {}'.format(total/contador))
print('O menor número é {} e o maior número é {}'.format(menor, maior))
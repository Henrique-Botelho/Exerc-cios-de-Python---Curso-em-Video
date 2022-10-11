num = 0
cont = 0
soma = 0

while num != 999:
    num = float(input('Digite um número[999 para PARAR]:'))
    if num != 999:    
        soma += num
        cont += 1

print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))

#Outra maneira de fazer (maneira do professor)

num = cont = soma = 0

while num != 999:
    soma += num
    cont += 1
    num = float(input('Digite um número[999 para PARAR]:'))

print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))

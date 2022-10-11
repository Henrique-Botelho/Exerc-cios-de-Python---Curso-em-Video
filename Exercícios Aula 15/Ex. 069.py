contida = 0
conthom = 0
contmul = 0

print('='*20)
print('CADASTRANDO PESSOAS')
print('='*20)

while True:
    idade = int(input('Idade:'))

    sexo = str(input('Sexo[F/M]:')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Sexo[F/M]:')).strip().upper()
    print('='*10)
    
    if idade >= 18:
        contida += 1
    if sexo == 'M':
        conthom += 1
    if sexo == 'F' and idade < 20:
        contmul += 1

    pros = str(input('Deseja continuar?[S/N]')).strip().upper()
    print('='*10)

    while pros not in 'SN':
        pros = str(input('Deseja continuar?[S/N]')).strip().upper()
        print('='*10)

    if pros == 'N':
        break

print(f'Total de pessoas com mais de 18: {contida}')
print(f'O total de homens cadastrados é: {conthom}')
print(f'O total de mulheres com menos de 20 anos é: {contmul}')
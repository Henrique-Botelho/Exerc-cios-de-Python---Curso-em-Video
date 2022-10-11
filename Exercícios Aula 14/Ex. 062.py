print('-='*25)
print('CALCULADORA DE PA')
print('-='*25)

n = 0
s = 0
termos = -1

a1 = float(input('Digite o valor do primeiro termo dessa PA:'))
r = float(input('Digite o valor da razão dessa PA:'))


while n <= 9:
    n += 1
    an = a1 + (n-1)*r
    print(an, end='')
    print(' → ' if n <= 9 else '', end='')
    if n == 10:
        while termos != 0:
            termos = int(input('\nQuantos termos mais você deseja ver?'))
            s = termos + n
            if termos != 0:
                while n < s:
                    n += 1
                    an = a1 + (n-1)*r
                    print(an, end='')
                    print(' → ' if n < s else '', end='')
                
        print('Fim do programa!')
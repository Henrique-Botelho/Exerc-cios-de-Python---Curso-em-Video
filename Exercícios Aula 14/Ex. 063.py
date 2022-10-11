prim = 0
seg = 1
cont = 2

print('-='*25)
print('O N-ÉSIMO TERMO DE UMA SEQUÊNCIA DE FIBONACCI')
print('-='*25)
 
num = int(input('Quantos termos você quer mostrar?'))

print('{} → {}'.format(prim, seg), end='')

while cont < num:
    cont += 1
    terc = prim + seg
    print(' → {}'.format(terc), end='')
    prim = seg
    seg = terc
print('\nFIM')
print('-='*25)
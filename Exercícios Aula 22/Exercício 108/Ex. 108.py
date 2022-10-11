import moeda

valor = float(input('Digite um preço: R$'))

m = moeda.metade(valor)
d = moeda.dobro(valor)
aum = moeda.aumentar(valor, 10)
dim = moeda.diminuir(valor, 10)



print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(m)}') 
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(d)}')
print(f'Aumentando 10%, temos {moeda.moeda(aum)}')
print(f'Diminuindo 10%, temos {moeda.moeda(dim)}')

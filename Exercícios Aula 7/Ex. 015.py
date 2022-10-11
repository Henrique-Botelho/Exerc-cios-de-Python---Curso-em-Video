d = float(input('Por quantos dias o carro foi alugado?'))
k = float(input('Quantos quilômetros o carro rodou?'))
t = (60*d) + (0.15*k)
print('O total a pagar é: R${:.2f}'.format(t))

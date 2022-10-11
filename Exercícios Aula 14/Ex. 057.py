sexo = input('Informe seu sexo [M/F]:').strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Comando inválido. Por favor, informe seu sexo [M/F]:')).strip().upper()[0]

print('Sexo {} registrado com sucesso. Obrigado pela informação!'.format(sexo))

#Esse [0] no final serve para pegar apenas o primeiro digito do que foi inputado.

def eleitor(ano):
    # Dockstring
    """Função que mostra a obrigatoriedade de voto no Brasil

    Args:
        ano (inteiro): o ano de nascimento da pessoa
    """
    from datetime import date

    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos, não pode votar ainda!'
    elif 16 < idade < 18 or idade >= 70:
        return f'Com {idade} anos, o voto é opcional.'
    else:
        return f'Com {idade} anos, o voto é obrigatório!'


print('-=-'*10)

nas = int(input('Em que ano você nasceu? '))

print(eleitor(nas))

help(eleitor)
nome = input('Nome: ')
peso = float(input('Peso: '))

if peso < 52:
    print('Peso inválido.')
else:
    if peso < 65:
        categoria = 'Pesado'
    elif peso < 72:
        categoria = 'Leve'
    elif peso < 79:
        categoria = 'Ligeiro'
    elif peso < 86:
        categoria = 'Meio-médio'
    elif peso < 90:
        categoria = 'Médio'
    elif peso < 100:
        categoria = 'Meio-pesado'
    else:
        categoria = 'Pesado'

    print(f'O lutador {nome} se enquadra na categoria {categoria}')

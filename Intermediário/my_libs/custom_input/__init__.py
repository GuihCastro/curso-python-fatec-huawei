def ler_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Informe apenas valores numéricos.')


def ler_float(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('Informe apenas valores numéricos.')


def ler_placa(msg):
    while True:
        placa = input(msg).strip().upper()
        placa_valida = len(placa) == 7 and placa[0:3].isalpha() and placa[3].isdigit() and placa[6:].isdigit()
        if placa_valida or placa == 'FIM': return placa
        print('Informe um valor válido para a placa, obedecendo às seguintes regras:')
        print(
            '-> Deve ter 7 caractéres;'
            '\n-> Os 3 primeiros devem ser letras;'
            '\n-> Os caracteres 4, 6 e 7 devem ser números.'
        )


def ler_data(msg):
    while True:
        valor = input(msg).strip()
        if valor.isdigit() and len(valor) == 8: return valor
        print('Informe apenas 8 valores numéricos no formato AAAAMMDD.')


def ler_opcao(*args):
    while True:
        opcao = input(f'Escolha o item que deseja alterar: {args}').strip().lower()
        if opcao in args: return opcao
        print('Digite uma opção válida.')

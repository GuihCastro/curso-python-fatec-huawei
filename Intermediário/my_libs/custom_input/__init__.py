def ler_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Informe apenas valores numéricos.')
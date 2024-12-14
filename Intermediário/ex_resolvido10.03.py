"""
Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome, Capital e PIB. A Sigla deve
ser usada como chave para o dicionário e o valor deve ser uma tupla formada com (Nome, Capital,
PIB). A leitura termina quando um string vazio for fornecido para a Sigla. Exibir os dados na tela.
"""

def ler_sigla(msg):
    while True:
        sigla = input(msg)
        if sigla.isalpha() and len(sigla) == 2 or not sigla:
            return sigla
        print('A sigla deve ter exatamente 2 caractéres alfabéticos.')


def ler_float(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('Informe apenas valores numéricos.')


estados = {}

while True:
    sigla = ler_sigla('Informe a sigla do estado que será cadastrado (ou nada para encerrar): ')
    if not sigla:
        break
    estados[sigla.upper()] = (
        input('Informe o nome do estado: '),
        input('Informe a capital do estado: '),
        round(ler_float('Informe o PIB do estado: R$'), 2)
    )

print(f'{estados=}')

print('Estados adicionados:')
for sigla, dados in estados.items(): print(f'{sigla}: {dados}')

"""
Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero. Para
cada valor de X apresente na tela se é par ou ímpar.
"""

x = int(input('Digite um valor: '))
while x != 0:
    if x % 2 == 0:
        print(f'{x} é PAR')
    else:
        print(f'{x} é ÍMPAR')
    x = int(input('Digite outro valor (ou "0" para parar): '))
print('Fim do programa...')

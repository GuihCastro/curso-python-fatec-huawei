"""
Escreva um programa que leia do teclado um número inteiro D. Esse número deve ser
obrigatoriamente maior que zero. Em seguida exiba na tela todos os números inteiros menores que
100 e que sejam divisíveis por D.
"""

D = int(input('Informe um número inteiro maior que zero: '))
if D <= 0:
    print('Você deve informar um valor maior que zero')
else:
    i = 1

    print(f'Números inteiros menores que 100 e divisíveis por {D}:')
    while i < 100:
        if i % D == 0:
            print(f'{i}', end=' ')
        i += 1

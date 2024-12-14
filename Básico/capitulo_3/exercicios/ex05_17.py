"""
Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida mostre na tela os Qtde termos
da sequência de Fibonacci que sejam maiores que Prim.
"""

while True:
    try:
        qtde = int(input('Informe a quantidade de termos: '))
        break
    except ValueError:
        print('Por favor, informe apenas números.')

while True:
    try:
        prim = int(input('Informe o valor para Prim: '))
        break
    except ValueError:
        print('Por vaor, informe apenas números.')

i = termo = anterior = proximo = 0

while i < qtde:
    if termo > prim:
        if i == qtde - 1:
            print(f'{termo}', end=' ')
        else:
            print(f'{termo},', end=' ')
    if i == 0:
        i += 1
        termo += 1
        continue
    proximo = termo + anterior
    anterior = termo
    termo = proximo
    i += 1

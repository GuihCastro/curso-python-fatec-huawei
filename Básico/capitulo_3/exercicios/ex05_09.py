"""
Escreva um programa que leia dois números inteiros: LMin e LMax. Em seguida exiba na tela todos
os valores dentro do intervalo fechado [LMin, LMax].
"""

lmin = int(input('LMin: '))
lmax = int(input('LMax: '))

print(f'Valores entre {lmin} e {lmax}:')

while lmin <= lmax:
    print(f'{lmin}', end=' ')
    lmin += 1

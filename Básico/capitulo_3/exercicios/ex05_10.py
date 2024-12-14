"""
Escreva um programa que leia três números inteiros: LMin, LMax e D. Em seguida exiba na tela todos
os valores divisíveis por D que estão dentro do intervalo fechado [LMin, LMax].
"""

lmin = int(input('LMin: '))
lmax = int(input('LMax: '))
d = int(input('D: '))

print(f'Valores entre {lmin} e {lmax} divisíveis por {d}:')

while lmin <= lmax:
    if lmin % d == 0:
        print(f'{lmin}', end=' ')
    lmin += 1

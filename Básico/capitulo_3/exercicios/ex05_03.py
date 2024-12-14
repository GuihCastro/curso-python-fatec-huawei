"""
Escreva um programa que mostre na tela os 10 primeiros termos de uma progressão aritmética (PA)
com primeiro termo P e razão R. Os dois números P e R são inteiros e devem ser lidos do teclado.
"""

P = int(input('Primero termo da PA: '))
R = int(input('Razão da PA: '))
termo = P
i = 0

while i < 10:
    print(f'{i+1}º termo: {termo}')
    termo += R
    i += 1

"""
Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado.
"""

N = int(input('Informe um número: '))
i = 1
while i <= 10:
    resultado = N * i
    print(f'{N} x {i} = {resultado}')
    i += 1

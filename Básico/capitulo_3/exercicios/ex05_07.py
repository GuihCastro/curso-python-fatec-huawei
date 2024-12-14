"""
Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis
por 7 entre 1 e N (inclusive).
"""

N = int(input('Digite um número inteiro: '))
i = 1

print(f'Números divisíveis por 7 entre {i} e {N}')

while i <= N:
    if i % 7 == 0:
        print(f'{i}', end=' ')
    i += 1

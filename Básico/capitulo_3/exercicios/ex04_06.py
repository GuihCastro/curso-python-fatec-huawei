"""
Escreva um programa que leia um número inteiro e mostre na tela se ele é divisível por 10 ou não.
"""

number = int(input('Informe um número inteiro: '))

if number % 10 == 0:
    print(f'{number} É divisível por 10')
else:
    print(f'{number} NÃO É divisível por 10')

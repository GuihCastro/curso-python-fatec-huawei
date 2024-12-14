"""
Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for
digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista. Ao final exiba
a lista na tela e a quantidade de elementos que ela contém.
"""

numeros = []

while True:
    while True:
        try:
            num = int(input('Informe um número inteiro (ou "0" para parar): '))
            break
        except ValueError:
            print('Por favor, informe apenas números inteiros. Tente novamente.')
    if num == 0:
        break
    numeros.append(num)

print(f'A lista contém {len(numeros)} elementos: {numeros}')

"""
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios quaisquer. Exiba a lista na tela.
Em seguida verifique se existem e elimine valores que estiverem repetidos, deixando apenas uma
ocorrência de cada. A ordem relativa dos elementos na lista não deve ser alterada, com exceção às
consequências da eliminação dos repetidos. Exiba a nova lista sem repetidos e o seu tamanho.
"""

from random import randint

while True:
    try:
        qtde = int(input('Quantidade de número a ser gerada na lista: '))
        break
    except ValueError:
        print('Você deve informar apenas números inteiros. Tente novamente.')

numeros = [randint(0, 50) for _ in range(qtde)]

print(f'Lista gerada:\n{numeros}')

"""
for i, num in enumerate(numeros):
    while True:
        if num not in numeros[i+1:]:
            break
        del numeros[numeros.index(num, i+1)]
"""

lista_sem_repetidos = []
for num in numeros:
    if num not in lista_sem_repetidos:
        lista_sem_repetidos.append(num)

print(f'Lista sem repetições:\n{lista_sem_repetidos}')

"""
Escreva um programa que leia um número inteiro nA e gere uma lista A com nA valores inteiros
aleatórios, não repetidos e situados na faixa [1, 100]. Mostre-a na tela em ordem crescente.
Em seguida leia outro inteiro nB e gere a lista B usando as mesmas regras aplicadas à lista A. Mostrea na tela também em ordem crescente.
Crie e exiba uma lista contendo a união das listas A e B, sem conter valores repetidos. Mostre a lista
resultante e a quantidade de elementos dela.

Exemplo:
    nA = 7
    lista A = [8, 12, 29, 35, 44, 64, 81]
    nB = 5
    lista B = [10, 25, 35, 38, 64]
    Saída: União de A e B
    [8, 10, 12, 25, 29, 35, 38, 44, 64, 81] contém 10 elementos
"""

from random import randint

lista_a = []

while True:
    try:
        n_a = int(input('Quantos valores terá a lista A? '))
        break
    except ValueError:
        print('Você deve informar apenas números inteiros. Tente novamente.')

while len(lista_a) < n_a:
    num = randint(1, 100)
    if num not in lista_a:
        lista_a.append(num)

lista_a.sort()

print(f'{lista_a=}')

lista_b = []

while True:
    try:
        n_b = int(input('Quantos valores terá a lista B? '))
        break
    except ValueError:
        print('Você deve informar apenas números inteiros. Tente novamente.')

while len(lista_b) < n_b:
    num = randint(1, 100)
    if num not in lista_b:
        lista_b.append(num)

lista_b.sort()

print(f'{lista_b=}')

lista_c = lista_a[:]

for num in lista_b:
    if num not in lista_c:
        lista_c.append(num)

lista_c.sort()

print(f'A lista resultante da união entre A e B é a seguinte, contendo {len(lista_c)} elementos:\n{lista_c}')

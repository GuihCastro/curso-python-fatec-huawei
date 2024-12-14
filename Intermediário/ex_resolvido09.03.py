"""
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de inteiros aleatórios. Exiba a lista na tela. Em seguida elimine valores que estiverem repetidos,
deixando apenas uma ocorrência de cada. Exiba a nova lista sem repetidos e o seu tamanho.
"""

from random import randint

def read_integer(msg):
    while True:
        try:
            integer = int(input(msg))
            return integer
        except ValueError:
            print('Informe apenas números inteiros.')


qtde = read_integer('Quantos números inteiros aleatórios serão carregados na lista? ')
lista = sorted([randint(0, 50) for _ in range(qtde)])

print(f'{lista=}')

lista_sem_repetidos = sorted(list(set(lista)))
tamanho = len(lista_sem_repetidos)

print(f'{lista_sem_repetidos=}\n{tamanho=}')

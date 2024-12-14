"""
Escreva um programa que leia um inteiro Qtde e crie um conjunto com elementos numéricos inteiros
aleatórios dentro do intervalo fechado [1, 50]. Mostre o conjunto gerado na tela.
Lembre-se que os conjuntos não podem ter elementos repetidos, então a geração de números
aleatórios pode representar um problema. Como resolver isso?
Cuidado: Este programa tem potencial para entrar em laço infinito caso o valor fornecido para Qtde seja maior
que 50. Faça o teste e depois responda a pergunta: por que isso ocorre?
"""

from random import randint

my_set = set()

while True:
    try:
        qtde = int(input('Informe a quantidade de números para o conjunto (máximo de 50): '))
        if 0 < qtde <= 50:
            break
        print('A quantidade só pode ser maior que zero e menor ou igual a 50.')
    except ValueError:
        print('Informe apenas números inteiros.')

while len(my_set) < qtde:
    my_set.add(randint(0, 50))

print(f'{my_set=}')

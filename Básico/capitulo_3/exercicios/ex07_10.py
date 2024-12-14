"""
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios entre 1 e 100. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
que zero. Para cada valor de X verifique se ele está na lista gerada e caso esteja elimine-o. Se houver
mais de uma ocorrência de X na lista, elimine todas. Após as eliminações exiba a lista novamente.
"""

from random import randint

while True:
    try:
        qtde = int(input('Quantos números deverão ser carregados na lista? '))
        break
    except ValueError:
        print('Por favor, informe apenas números inteiros. Tente novamente.')

lista_aleatoria = [randint(1, 100) for _ in range(qtde)]

print(f'A lista gerada foi:\n{lista_aleatoria}')

while True:

    while True:
        try:
            x = int(input('Informe um número para removê-lo da lista ' \
                          '(ou qualquer valor menor ou igual a zero para encerrar): '))
            break
        except ValueError:
            print('Por favor, informe apenas números inteiros. Tente novamente.')

    if x <= 0:
        break

    if x in lista_aleatoria:
        while x in lista_aleatoria:
            lista_aleatoria.remove(x)
        else:
            print(f'\nA lista atualizada é:\n{lista_aleatoria}')
    else:
        print(f'O valor {x} não existe na lista. Tente novamente.')

print(f'\nFim do programa.\nA lista final ficou assim:\n{lista_aleatoria}')

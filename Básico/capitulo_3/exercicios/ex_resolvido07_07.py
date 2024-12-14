"""
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
que zero. Para cada valor de X verifique se ele está ou não na lista gerada. Caso esteja é preciso exibir
a quantidade de ocorrências.
"""

from random import randint

numeros_aleatorios = []

while True:
    try:
        qtde = int(input('Quantos números devem ser gerados? '))
        break
    except ValueError:
        print('Você deve informar apenas números inteiros. Tente novamente.')

for _ in range(qtde):
    num = randint(1, 10)
    numeros_aleatorios.append(num)

print('Agora, tente adivinhar os números que foram gerados:')
while True:
    while True:
        try:
            palpite = int(input('Chute um número (0 para encerra): '))
            break
        except ValueError:
            print('Por favor, informe apenas números inteiros. Tente novamente.')
    if palpite == 0:
        break
    if palpite in numeros_aleatorios:
        print(f'O número {palpite} está na lista, e foi gerado {numeros_aleatorios.count(palpite)} vezes!')
    else:
        print(f'O número {palpite} não foi gerado nenhuma vez.')

print(f'\nA lista com todos os números gerados foi a seguinte:\n{numeros_aleatorios}')

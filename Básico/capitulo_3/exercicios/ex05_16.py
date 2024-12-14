"""
Escreva um programa que leia uma quantidade Qtde e mostre na tela os Qtde primeiros termos da
sequência de Fibonacci.
A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência
são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Caso de teste: Se Qtde = 9, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

while True:
    try:
        qtde = int(input('Informe a quantidade de termos: '))
        break
    except ValueError:
        print('Por favor, informe apenas números.')

i = termo = anterior = proximo = 0

while i < qtde:
    if i == qtde - 1:
        print(f'{termo}', end=' ')
    else:
        print(f'{termo},', end=' ')
    if i == 0:
        i += 1
        termo += 1
        continue
    proximo = termo + anterior
    anterior = termo
    termo = proximo
    i += 1

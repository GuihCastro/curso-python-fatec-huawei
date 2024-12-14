"""
Escreva um programa que leia 3 números inteiros e mostre na tela se eles formam um triângulo ou
não. Caso formem um triângulo informe o tipo de triângulo (equilátero, isósceles ou escaleno).
Regra: Para três números formarem um triângulo precisa ocorrer que:
a) os três números precisam ser maiores que zero;
b) a soma dos dois menores valores deve ser maior que o terceiro.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    menor_1 = n2
    menor_2 = n3
elif n2 > n3:
    maior = n2
    menor_1 = n1
    menor_2 = n3
else:
    maior = n3
    menor_1 = n1
    menor_2 = n2

formam_triangulo = (n1 > 0 and n2 > 0 and n3 > 0) and (menor_1 + menor_2 > maior)

if formam_triangulo:
    print('Esses três números formam um triângulo', end=' ')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 != n3 and n1 != n3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Esses três números não formam um triângulo')

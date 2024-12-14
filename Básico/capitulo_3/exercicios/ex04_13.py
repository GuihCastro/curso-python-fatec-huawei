"""
Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
a) "Os três valores são iguais"
b) "Há dois valores iguais e um diferente"
c) "Os três valores são diferentes"
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 == n2 == n3:
    print('Os três valores são iguais')
elif n1 != n2 != n3 != n1:
    print('Os três valores são diferentes')
else:
    print('Há dois valores iguais e um diferente')

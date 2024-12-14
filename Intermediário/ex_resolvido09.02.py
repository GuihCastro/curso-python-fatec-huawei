"""
Escreva um programa que leia do teclado dois conjuntos de números inteiros digitados pelo usuário.
Exiba na tela a união e a interseção desses conjuntos.
"""

def read_integer(msg):
    while True:
        try:
            integer = int(input(msg))
            return integer
        except ValueError:
            print('Informe apenas números inteiros.')


set_a = set()
set_b = set()

print('Digite os valores para o CONJUNTO A ("0" para parar)')
while True:
    value = read_integer('Informe um número inteiro: ')
    if value == 0:
        break
    set_a.add(value)

print('Digite os valores para o CONJUNTO B ("0" para parar)')
while True:
    value = read_integer('Informe um número inteiro: ')
    if value == 0:
        break
    set_b.add(value)

print(f'A UNIÃO dos conjuntos A e B é: {set_a | set_b}\nA INTERSECÇÃO dos conjuntos A e B é: {set_a & set_b}')

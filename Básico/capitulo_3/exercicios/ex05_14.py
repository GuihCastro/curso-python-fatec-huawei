"""
Escreva um programa que leia um número inteiro N. Em seguida calcule e mostre na tela o fatorial
de N (N!).
"""

while True:
    try:
        n = int(input('Informe um número inteiro: '))
        break
    except ValueError:
        print('Por favor, informe apenas números.')

i = n
fatorial = 1
while i > 0:
    fatorial *= i
    i -= 1

print(f'O fatorial de {n} é: {fatorial}')

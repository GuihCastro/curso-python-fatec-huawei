"""
Escreva um programa que leia um número inteiro e informe se esse número é primo ou não.
Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.
"""

while True:
    try:
        n = int(input('Informe um número inteiro: '))
        break
    except ValueError:
        print('Por favor, informe apenas números.')

primo = True
i = n - 1

while i > 1:
    if n % i == 0:
        primo = False
        break
    i -= 1

if primo:
    print(f'O número {n} É primo.')
else:
    print(f'O número {n} NÃO É primo.')

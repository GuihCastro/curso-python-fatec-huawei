"""
Escreva um programa que leia três números inteiros: o primeiro termo P, a razão R e a quantidade Q
de termos de uma progressão aritmética. O programa deve calcular os Q termos da progressão
colocando-os em uma lista e no final exibi-la na tela.
obs: esse problema já foi abordado, sem o uso de listas, no exercício resolvido 5.3.
"""

progression = []

while True:
    try:
        p = termo = int(input('Primeiro termo: '))
        r = int(input('Razão: '))
        q = int(input('Quantidade de termos: '))
        break
    except ValueError:
        print('Por favor, informe apenas números inteiros. Tente novamente!')

for _ in range(q):
    progression.append(termo)
    termo += r

print(f'Os {q} primeiros termos da progressão aritmética de razão {r}, começando em {p}, são:\n{progression}')

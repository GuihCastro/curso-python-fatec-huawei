"""
Escreva um programa que leia um string contendo três números inteiros separados por espaços em
branco. Separe-os em objetos int, calcule sua soma e exiba na tela.
Entrada: 26 128 44 (string com três inteiros separados por espaço em branco)
Saída:
n1 = 26
n2 = 128
n3 = 44
Soma = 198
"""

while True:
    try:
        entrada = input('Informe 3 números inteiros, separados por um espaço entre cada um deles: ').strip().split()
        entrada = [int(valor) for valor in entrada]
        print(f'O resultado da soma entre {entrada[0]}, {entrada[1]} e {entrada[2]} é: {sum(entrada)}')
        break
    except ValueError:
        print('Por favor, informe apenas valores numéricos. Tente novamente.')
    except IndexError:
        print('Você deve informar 3 números, separados por um espaço entre cada.')

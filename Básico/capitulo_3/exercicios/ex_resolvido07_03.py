"""
Escreva um programa que leia um número inteiro N. Em seguida leia N números reais carregandoos em uma lista.
Ao final exiba os elementos da lista na tela, sendo um em cada linha
"""

numeros_reais = []

while True:
    try:
        n = int(input('Quantos números serão inseridos na lista? '))
        break
    except ValueError:
        print('Informe apenas números inteiros. Tente novamente.')

for _ in range(n):
    while True:
        try:
            num = float(input('Informe um número real: '))
            break
        except ValueError:
            print('Informe apenas números reais. Tente novamente.')

    numeros_reais.append(num)

print('Os números digitados foram:')
for num in numeros_reais:
    print(num)

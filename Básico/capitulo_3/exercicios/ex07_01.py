"""
Altere a solução do ex.resolvido 7.3 para exibir os números reais da lista com duas casas decimais.
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
    print(f'{num:.2f}')

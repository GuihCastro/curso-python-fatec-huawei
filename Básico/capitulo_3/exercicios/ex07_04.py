"""
Altere a solução ex.resolvido 7.3 para exibir os resultados em ordem crescente
Dica: Aplique o método .sort() apresentado no quadro 7.2 e visto no vídeo do exemplo 7.10
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

numeros_reais.sort()
print('Os números digitados foram:')
for num in numeros_reais:
    print(f'{num:.2f}')

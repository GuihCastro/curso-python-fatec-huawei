"""
Altere a solução do ex.resolvido 7.3 incluindo o comando try-except na leitura dos números reais
para evitar a digitação incorreta dos valores. Quando ocorrer uma exceção uma mensagem deve ser
exibida na tela informando esta condição.
Dica: Relembre o tratamento de exceções consultando o capítulo 6, em especial o exemplo 6.4
"""

# Mantive o mesmo código pois já estava fazendo a validação de input com try-except

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

"""
Altere a solução ex.resolvido 7.4 para exibir as listas em ordem crescente
"""

lista_positivos = []
lista_negativos = []

while True:
    try:
        n = int(input('Quantos números serão digitados? '))
        break
    except ValueError:
        print('Por favor, informe apenas números inteiros. Tente novamente.')

for _ in range(n):
    while True:
        try:
            num = int(input('Informe um número inteiro: '))
            break
        except ValueError:
            print('Por favor, informe apenas número inteiros. Tente novamente.')
    lista_positivos.append(num) if num >= 0 else lista_negativos.append(num)

lista_positivos.sort()
lista_negativos.sort()

print(f'Lista de números positivos, com {len(lista_positivos)} valores: {lista_positivos}')
print(f'Lista de números positivos, com {len(lista_negativos)} valores: {lista_negativos}')

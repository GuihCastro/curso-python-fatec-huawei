"""
Altere a solução ex.resolvido 7.6 de modo que todos os valores repetidos rejeitados sejam incluídos
em uma segunda lista. Ao final exiba essa segunda lista juntamente com seu tamanho.
"""

numeros = []
repetidos = []

while True:
    while True:
        try:
            num = int(input('Informe um número inteiro (ou "0" para parar): '))
            break
        except ValueError:
            print('Por favor, informe apenas números inteiros. Tente novamente.')
    if num == 0:
        break
    numeros.append(num) if num not in numeros else repetidos.append(num)

print(f'A lista contém {len(numeros)} elementos: {numeros}')
print(f'A lista dos repetidos contém {len(repetidos)} elementos: {repetidos}')

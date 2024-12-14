"""
Escreva um programa que permaneça em laço lendo três dados de um produto: o código (int), o
preço de compra (float) e o preço de venda(float). Com esses dados forme uma tupla e armazene-a
em uma lista. Os três dados devem ser lidos em uma única linha separados por espaço em branco.
O laço termina quando forem digitados três zeros: 0 0 0
Em seguida, para todas as tuplas presentes na lista, exiba o código do produto e a margem bruta de
lucro do produto em porcentagem e com uma casa decimal.
A margem bruta de lucro é calculada com a expressão:
𝑀𝑎𝑟𝑔𝑒𝑚𝐵𝑟𝑢𝑡𝑎 = ((𝑃𝑟𝑒ç𝑜 𝑉𝑒𝑛𝑑𝑎 / 𝑃𝑟𝑒ç𝑜 𝑑𝑒 𝐶𝑜𝑚𝑝𝑡𝑎) − 1) * 100%
"""

produtos = []

while True:
    while True:
        try:
            produto = input(
                'Informe: código, preço de compra e preço de venda, separados por um espaço ("0 0 0" para encerrar): '
            ).strip().split()
            produto = int(produto[0]), float(produto[1]), float(produto[2])
            break
        except ValueError:
            print('Por favor, informe apenas valores numéricos. Tente novamente.')
        except IndexError:
            print('Por favor, informe todos os 3 valores, e separados por um espaço entre cada. Tente novamente')

    if produto == (0, 0, 0):
        break

    produtos.append(produto)

print()
for produto in produtos:
    codigo = produto[0]
    margem_bruta = ((produto[2] / produto[1]) - 1) * 100
    print(f'O produto de código {codigo} tem uma Margem Bruta de lucro de {margem_bruta:.1f}%')

"""
Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
um string e o preço é real. Acrescente o par código:preço em um dicionário. O laço termina quando
for fornecido um string vazio para o código. Ao final, exibir código e preço, um produto em cada linha.
"""

def ler_real(msg):
    while True:
        try:
            valor = float(input(msg))
            break
        except ValueError:
            print('Informe um valor numérico.')
    return valor


produtos = {}

while True:
    codigo = input('Código do produto (não digite nada para encerrar): ').strip()
    if not codigo:
        break
    preco = ler_real('Preço do produto: R$')
    produtos[codigo] = preco

print('\nProdutos cadastrados:')
for codigo, preco in produtos.items(): print(f'\tCódigo: {codigo} -> Preço: R${preco:.2f}')

"""
Altere a solução do exercício resolvido 10.1 para fazer a iteração com o método .items()
"""

# Já tinha feito assim

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

"""
No comércio, o conceito de Margem Bruta é uma porcentagem que é aplicada ao preço de custo
para se obter o preço de venda. Uma loja tem como política comercial aplicar uma margem bruta de
45% quando o preço de custo de um produto é menor ou igual a R$ 100,00. Se o produto custa mais
que isso a margem bruta é de 35%. Escreva um programa que leia o preço de custo do produto e
mostre na tela qual o seu preço de venda, com duas casas decimais.
"""

custo = float(input('Preço de custo: R$'))

if custo <= 100.00:
    margem = 0.45
else:
    margem = 0.35

preco_de_venda = custo + (custo * margem)

print(f'Preço de venda: R${preco_de_venda:.2f}')

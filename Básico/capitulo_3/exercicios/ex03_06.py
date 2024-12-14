# leitura de dados
vendedor_1 = input('Vendedor 1: ')
vendas_1 = float(input('Vendas 1: '))
vendedor_2 = input('Vendedor 2: ')
vendas_2 = float(input('Vendas 2: '))
vendedor_3 = input('Vendedor 3: ')
vendas_3 = float(input('Vendas 3: '))

# cálculo de comissões
comissao_1 = vendas_1 * 0.06
comissao_2 = vendas_2 * 0.06
comissao_3 = vendas_3 * 0.06

# totais
total_1 = 1200.00 + comissao_1
total_2 = 1200.00 + comissao_2
total_3 = 1200.00 + comissao_3

# saídas
print(f'O vendedor {vendedor_1} vendeu R${vendas_1:.2f} e faz jus a um pagamento de R${total_1:.2f}')
print(f'O vendedor {vendedor_2} vendeu R${vendas_2:.2f} e faz jus a um pagamento de R${total_2:.2f}')
print(f'O vendedor {vendedor_3} vendeu R${vendas_3:.2f} e faz jus a um pagamento de R${total_3:.2f}')

"""
Exercício 5
Crie um programa que simule a entrada de dados de uma lista de produtos. O programa deve:
    1. Solicitar ao usuário que insira o nome de um produto e o preço correspondente.
    2. Armazenar essas informações em um dicionário onde as chaves são os nomes dos produtos e os valores são os preços.
    3. Continuar pedindo ao usuário até que ele digite "sair".
    4. Usar try-except para garantir que o preço digitado seja um número válido. Se o usuário inserir um valor inválido,
    exiba uma mensagem apropriada e peça novamente.
    5. Após a entrada de dados, exiba a lista de produtos e preços.
"""

products = {}

while True:
    name = input('Informe o nome do produto (ou "sair" para encerrar): ').strip()
    if name.lower() == 'sair':
        break
    while True:
        try:
            price = float(input('Informe o preço do produto: R$'))
            break
        except ValueError:
            print('Por favor, insira apenas números reais para o preço.')
    products[name] = price

print('\nPRODUTOS CADASTRADOS:')
for product, price in products.items():
    print(f'-> {product}: R${price:.2f}')

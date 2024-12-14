"""
Uma indústria metalúrgica adota um código de produto com o seguinte formato TMMM, onde T indica
o uso do produto, sendo 1 para residencial; 2 para industrial e MMM indica qual é o produto.
Escreva um programa que permaneça em laço até que seja digitado 0. Em cada repetição leia duas
informações:
a) O código do produto;
b) A quantidade vendida desse produto
O programa deve totalizar separadamente e exibir na tela as quantidades de produtos residenciais e
industriais vendidos. Se o dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido" e a
quantidade deve ser ignorada.
"""

residencial = industrial = 0

while True:
    codigo = input('Informe o código (TMMM) do produto (ou "0" para encerrar): ')

    if codigo == '0':
        break

    codigo_invalido = codigo[0] != '1' and codigo[0] != '2' or len(codigo) != 4 or not codigo.isdigit()

    if codigo_invalido:
        print('Código inválido. Tente novamente.')
        continue

    quantidade = int(input('Informe a quantidade: '))
    
    if codigo[0] == 1:
        residencial += quantidade
    else:
        industrial += quantidade

print(f'Quantidades vendidas por tipo:\n{residencial=}\n{industrial=}')

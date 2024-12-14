"""
Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
Dólar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
quer comprar e calcule o valor em reais necessários.
"""

moeda = input('Qual moeda deseja comprar? (D para Dólar | E para Euro | L para Libra Esterlina): ')
while moeda.upper() != 'D' and moeda.upper() != 'E' and moeda.upper() != 'L':
    print('Você informou uma opção inválida. Tente novamente.')
    moeda = input('Qual moeda deseja comprar? (D para Dólar | E para Euro | L para Libra Esterlina): ')
valor = float(input('Qual o valor desejado? $'))

if moeda.upper() == 'D':
    real = valor * 4.89
elif moeda.upper() == 'E':
    real = valor * 5.26
else:
    real = valor * 6.17

print(f'Serão necessários: R${real:.2f}')

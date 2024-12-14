"""
Uma empresa financeira concede empréstimos a pessoas físicas quando o valor da parcela é menor
que 8% do salário da pessoa. Escreva um programa que leia dois números reais: o valor do salário e
o valor da parcela e informe se o empréstimo será concedido ou não.
"""

salario = float(input('Salário: R$'))
parcela = float(input('Valor da parcela: R$'))

if parcela < salario * 0.08:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')

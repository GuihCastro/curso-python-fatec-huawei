"""
Escreva um programa que leia o nome de um aluno e as notas obtidas em três avaliações. A média
final é a média aritmética das três notas e a pessoa estará aprovada se essa média for maior ou igual
a 7.0. Mostre na tela o nome, a média e a situação que será "Aprovado" ou "Reprovado".
"""

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
nota_3 = float(input('Terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

print(f'Média: {media:.1f}')

if media >= 7:
    print('APROVADO!')
else:
    print('REPROVADO!')

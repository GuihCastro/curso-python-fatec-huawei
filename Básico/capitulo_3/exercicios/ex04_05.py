"""
Classificação indicativa é um conceito que se aplica à faixa etária para a qual uma obra audiovisual
se recomenda ou não. Suponha que um filme em cartaz no cinema tenha a Classificação de 16 anos.
Escreva um programa que leia a idade de uma pessoa e mostre se está de acordo ou não com a
classificação.
"""

idade = int(input('Idade: '))

if idade < 16:
    print(f'Com {idade} anos não é indicado assistir ao filme')
else:
    print(f'{idade} anos está dentro da classificação indicativa do filme')

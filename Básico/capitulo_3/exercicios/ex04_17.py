"""
Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o
primeiro colocado não tenha mais do que 50% dos votos. Escreva um programa que leia o nome do
município, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se
haverá segundo turno ou não.
"""

municipio = input('Nome do município: ')
eleitores = int(input('Quantidade de eleitores: '))
votos = int(input('Quantidade de votos do candidato mais votado: '))

if eleitores > 200000 and votos < eleitores * 0.5:
    print(f'No município de {municipio} haverá segundo turno')
else:
    print(f'No município de {municipio} não haverá segundo turno')

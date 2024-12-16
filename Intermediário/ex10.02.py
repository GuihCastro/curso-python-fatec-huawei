"""
Escreva um programa que permaneça em laço lendo do teclado números inteiros entre 1 e 9. Outros
valores devem ser ignorados. Esse laço termina quando for digitado zero ou qualquer valor negativo.
O objetivo deste programa é contar quantas vezes cada valor entre 1 e 9 foi digitado.
Ao término do laço de leitura o programa deve mostrar quais valores foram digitados e quantas vezes
cada um. Obrigatoriamente use um dicionário.
"""

from my_libs.custom_input import ler_int


valores = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

while True:
    valor = ler_int('Informe um número inteiro (0 ou menos para interromper): ')
    if valor <= 0: break
    if 1 <= valor <= 9: valores[valor] += 1

print(f'Foram digitados {len(valores)} valores entre 1 e 9, sendo:')
for chave, valor in valores.items(): print(f'\tValor {chave}: {valor} vez(es)')

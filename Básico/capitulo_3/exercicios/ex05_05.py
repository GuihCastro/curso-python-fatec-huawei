"""
Escreva um programa que permaneça em laço enquanto um valor inteiro lido for diferente de zero.
Totalize e conte os valores digitados, exceto o zero, e apresente esses valores na tela. Totalizar é
somar os valores.
"""

valor = int(input('Digite um valor: '))
soma = quantidade = 0

while valor != 0:
    soma += valor
    quantidade += 1
    valor = int(input('Digite outro valor (ou "0" para parar): '))

print(f'{soma = }\n{quantidade = }')

########

soma = qtde = 0
A = 1
while A != 0:
    A = int(input("Digite A: "))
    if A != 0:
        soma = soma + A
        qtde = qtde + 1

print(f'Soma dos valores = {soma}')
print(f'Quantidade = {qtde}')
print('Fim do Programa')

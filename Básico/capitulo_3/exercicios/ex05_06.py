"""
Reescreva o Exercício Resolvido 5.5 de modo a eliminar o comando if que foi acrescentado dentro
do laço while. Procure pensar em uma forma de eliminar esse condicional e ao mesmo tempo
manter o programa correto, totalizando e contando os valores diferentes de zero que forem
digitados.
Dica: a solução consiste em alterar a ordem dos comandos existentes dentro do laço while.
"""

valor = int(input('Digite um valor: '))
soma = quantidade = 0

while valor != 0:
    soma += valor
    quantidade += 1
    valor = int(input('Digite outro valor (ou "0" para parar): '))

print(f'{soma=}\n{quantidade=}')

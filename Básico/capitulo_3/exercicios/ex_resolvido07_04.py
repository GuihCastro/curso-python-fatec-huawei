"""
Escreva um programa que leia um número inteiro N. Em seguida leia N números inteiros carregando
os valores negativos em uma lista e os positivos em outra. Ao final exiba na tela cada uma das listas
juntamente como seu tamanho.
obs. Se o valor zero for fornecido ele deve ser incluído na lista de positivos.
"""

lista_positivos = []
lista_negativos = []

while True:
    try:
        n = int(input('Quantos números serão digitados? '))
        break
    except ValueError:
        print('Por favor, informe apenas números inteiros. Tente novamente.')

for _ in range(n):
    while True:
        try:
            num = int(input('Informe um número inteiro: '))
            break
        except ValueError:
            print('Por favor, informe apenas número inteiros. Tente novamente.')
    lista_positivos.append(num) if num >= 0 else lista_negativos.append(num)

print(f'Lista de números positivos, com {len(lista_positivos)} valores: {lista_positivos}')
print(f'Lista de números positivos, com {len(lista_negativos)} valores: {lista_negativos}')

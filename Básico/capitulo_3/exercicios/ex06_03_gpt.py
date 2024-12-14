"""
Exercício 3: Validando listas
Escreva um programa que peça ao usuário o índice de um elemento em uma lista pré-definida.
Exiba o elemento correspondente, mas use try-except para:
    -> Avisar o usuário caso o índice fornecido esteja fora dos limites da lista.
    -> Lidar com entradas inválidas (não numéricas).
Lista de exemplo: [10, 20, 30, 40, 50]
"""

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input('Informe o índice do valor da lista que deseja acessar (apenas números): '))
    print(f'O valor de índice {index} é: {numbers[index]}')
except ValueError:
    print('Por favor, informe apenas números.')
except IndexError:
    print(f'O índice informado não existe na lista. Tente novamente.')
except:
    print('Ocorreu um erro desconhecido.')

"""
Exercício 4: Forma completa do try-except
Crie um programa que:
    1. Leia um número do usuário e calcule o quadrado dele.
    2. Use try-except-else-finally para:
        -> Tratar entradas inválidas com uma mensagem específica no except.
        -> Exibir uma mensagem de sucesso no else caso nenhum erro ocorra.
        -> Exibir uma mensagem de encerramento no finally que sempre será executada.
"""

try:
    number = int(input('Informe um número para saber o seu quadrado: '))
    power = pow(number, 2)
except ValueError:
    print('Por favor, informe apenas números.')
else:
    print(f'O quadrado de {number} é {power}')
finally:
    print('Obrigado e volte sempre.')

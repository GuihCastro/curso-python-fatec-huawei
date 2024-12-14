"""
Exercício 1: Protegendo divisões
Implemente um programa que peça dois números ao usuário e calcule a divisão do primeiro pelo segundo.
Proteja o código usando try-except para evitar que erros interrompam a execução do programa.
Certifique-se de exibir uma mensagem amigável em caso de erro.
"""

try:
    first = int(input('Informe o primeiro número: '))
    second = int(input('Informe o segundo número: '))
    result = first / second
    print(f'O resultado da divisão de {first} por {second} é: {result:.1f}')
except:
    print('Ocorreu um erro. Por favor, tente novamente.')

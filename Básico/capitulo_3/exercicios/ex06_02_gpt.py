"""
Exercício 2: Lidando com múltiplas exceções
Modifique o programa do Exercício 1 para tratar:
    -> Divisão por zero com uma mensagem específica.
    -> Entrada inválida (como letras em vez de números) com outra mensagem específica.
    -> Outros erros desconhecidos com uma mensagem genérica.
"""

try:
    first = int(input('Informe o primeiro número: '))
    second = int(input('Informe o segundo número: '))
    result = first / second
    print(f'O resultado da divisão de {first} por {second} é: {result:.1f}')
except ZeroDivisionError:
    print('Não é possível dividir por 0. Tente novamente.')
except ValueError:
    print('Por favor, informe apenas números.')
except:
    print('Ocorreu um erro desconhecido. Por favor, tente novamente.')

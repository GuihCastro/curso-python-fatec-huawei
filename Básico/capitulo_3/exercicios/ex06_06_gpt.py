"""
Exercício 6: Tratamento de múltiplas entradas
Peça ao usuário que insira dois números separados por um espaço, como "10 20". Divida o primeiro número pelo segundo.
Use try-except para lidar com:
    -> Falha na separação dos dois números.
    -> Erros na conversão para inteiros.
    -> Divisão por zero.
"""

while True:
    try:
        numbers = input('Informe dois números (separados por um espaço): ').strip().split()
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        result = num1 / num2
        break
    except ValueError:
        print('Por favor, informe apenas números e um espaço entre eles. Tente novamente.')
    except IndexError:
        print('Por favor, você deve inserir um espaço entre os números. Tente novamente.')
    except ZeroDivisionError:
        print('O segundo número não pode ser zero. Tente novamente.')

print(f'O resultado da divisão de {num1} por {num2} é: {result:.1f}')

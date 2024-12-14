"""
Escreva um programa que obrigatoriamente leia um inteiro que esteja no intervalo fechado
[100, 200]. Se o valor fornecido estiver fora do intervalo o programa deve avisar que o valor é inválido
e permanecer no laço. Quando um valor válido for fornecido o programa deve informar que o valor
foi aceito e terminar.
"""

while True:
    number = int(input('Informe um número inteiro dentro do intervalo [100, 200]: '))
    if 100 <= number <= 200:
        print('Valor aceito!')
        break
    print('Valor inválido! Tente novamente.')

print('Fim do programa.')

num_1 = int(input('Primeiro número: '))
num_2 = int(input('Segundo número: '))

if num_1 < num_2:
    print(f'O menor entre eles é {num_1}')
elif num_2 < num_1:
    print(f'O menor entre eles é {num_2}')
else:
    print(f'Os dois números são iguais, com o valor {num_1}')

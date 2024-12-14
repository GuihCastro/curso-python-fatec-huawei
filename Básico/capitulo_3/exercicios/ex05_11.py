"""
Escreva um programa que permaneça em laço lendo cadeias de caracteres (strings). Para cada
cadeia digitada o programa deve exibir a cadeia seguida da quantidade de caracteres que ela
contém. O programa termina quando for digitado "FIM" (em letras maiúsculas).
"""

while True:
    palavra = input('Digite uma palavra ("FIM" para encerrar): ').upper()
    if palavra == 'FIM':
        break
    print(f'A palavra {palavra} tem {len(palavra)} letras.')

print('Fim do programa...')

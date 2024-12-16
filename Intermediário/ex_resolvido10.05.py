"""
Considere o seguinte conjunto de dados: Nome + (N1, N2, N3, N4). Nome representa o nome de um
aluno e deve ser usado como chave. N1, N2, N3, N4 representam as notas de provas desse aluno.
Escreva um programa que leia os dados de Q alunos e determine a situação de cada aluno. O critério
que garante a aprovação é que a média aritmética das 4 notas de prova seja maior ou igual 6,0. Q é
a quantidade de alunos e este valor deve ser lido do teclado no começo do programa.
Para cada aluno o nome deve ser lido em separado e suas notas de prova devem ser lidas juntas na
mesma linha, com um espaço em branco de separação.
Para cada aluno o programa deve mostras o Nome, as 4 notas de prova, a média final e a situação
(aprovado/reprovado). As notas devem ser exibidas com uma casa decimal.
"""

def ler_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Informe apenas valores numéricos.')


def ler_notas(msg):
    while True:
        try:
            notas = input(msg).split()
            nota1 = float(notas[0])
            nota2 = float(notas[1])
            nota3 = float(notas[2])
            nota4 = float(notas[3])
            return nota1, nota2, nota3, nota4
        except ValueError:
            print('Informe apenas valores numéricos.')
        except IndexError:
            print('Devem ser informados EXATAMENTE 4 notas, separadas por um espaço em cada.')


alunos = []
q = ler_int('Quantos alunos serão registrados? ')

for i in range(q):
    aluno = {}
    nome = input(f'Informe o nome do {i+1}º aluno: ').strip()
    n1, n2, n3, n4 = ler_notas(f'Informe as 4 notas do aluno {nome} (em uma única linha, separadas por espaços): ')
    media = round((n1+ n2 + n3 + n4) / 4, 1)
    situacao = 'APROVADO' if media >= 6.0 else 'REPROVADO'
    aluno[nome] = {
        'notas': (n1, n2, n3, n4),
        'média': media,
        'situação': situacao
    }
    print(f'Aluno {i+1}:')
    for chave, valor in aluno.items(): print(f'{chave}: {valor}')
    alunos.append(aluno)

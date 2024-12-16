"""
Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.
A chave deve o nome. O valor deve ser um dicionário aninhado contendo os demais dados. Se o
nome já existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.
Ao digitar um string vazio para o nome, o programa interrompe a leitura. Antes de encerrar o programa
apresente os dados em um formato de tabela.
"""

contatos = {}

while True:
    nome = input('Informe o nome do contato para cadastrar (ou não digite nada para encerrar): ').strip()
    if not nome: break
    if nome in contatos.keys():
        option = input('Já existe um contato com este nome. Deseja alterar o cadastro? [y/n]').strip().lower()
        deseja_alterar = True if option == 'y' else False
        if not deseja_alterar: break
    celular = input(f'Número de celular para o contato "{nome}": ')
    email = input(f'E-mail para o contato "{nome}": ')
    aniversario = input(f'Data de aniversário para o contato "{nome}": ')
    contatos[nome] = {
        'celular': celular,
        'e-mail': email,
        'aniversário': aniversario
    }

print(f'{'NOME':<30}{'CELULAR':<15}{'E-MAIL':<20}{'ANIVERSÁRIO':<15}\n{'-'*80}')
for nome, dados in contatos.items():
    print(f'{nome:<30}{dados['celular']:<15}{dados['e-mail']:<20}{dados['aniversário']:<15}')

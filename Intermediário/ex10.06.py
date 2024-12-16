"""
Escreva um programa para registrar os seguintes dados de uma frota de veículos de uma empresa:
Placa (string – chave – obrigatório todas as letras maiúsculas)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ficar em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa deve convertê-las para
maiúsculas com o método .upper().
Para cada veículo leia todos os dados e carregue em um dicionário. Se uma placa já existente for
digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração
em algum dado basta digitar o novo valor. Para os campos em que nada for digitado deve ser mantido
o valor já cadastrado.
Ao final do laço mostre os dados na tela com uma formatação legível.
Desafio Inclua no programa uma validação da placa, seguindo as seguintes regras:
a) Deve ter 7 caracteres
b) Os três primeiros devem ser letras
c) Os caracteres 4, 6 e 7 devem ser algarismos
d) O caractere 5 pode ser número (placa antiga) ou letra (nova placa padrão Mercosul)
"""

from my_libs.custom_input import ler_opcao, ler_float, ler_data, ler_placa

frota = {}

while True:
    placa = ler_placa('Digite a placa do veículo a ser cadastrado (ou "FIM" para encerrar): ')
    if placa == 'FIM': break
    if placa in frota.keys():
        print('Já existe um veículo cadastrado para a placa informada:')
        for chave, valor in frota[placa].items(): print(f'{chave}: {valor}')
        alterar = input('Deseja alterar algum dado deste veículo? [s/n]: ').strip().lower()
        if alterar == 's':
            match ler_opcao('marca', 'modelo', 'tipo', 'km', 'data'):
                case 'marca': frota[placa]['marca'] = input('Informe a nova marca: ').strip()
                case 'modelo': frota[placa]['modelo'] = input('Informe o novo modelo: ').strip()
                case 'tipo': frota[placa]['tipo'] = input('Informe o novo tipo: ').strip()
                case 'km': frota[placa]['km'] = ler_float('Informe a nova quilometragem: ')
                case 'data': frota[placa]['data'] = ler_data('Informe a nova data da compra')
        continue
    frota[placa] = {
        'marca': input('Informe a marca do veículo: ').strip(),
        'modelo': input('Informe o modelo do veículo: ').strip(),
        'tipo': input('Informe o tipo do veículo (caminhão, furgão, automóvel, motocicleta, etc): ').strip(),
        'km': ler_float('Informe a quilometragem do veículo: '),
        'data': ler_data('Informe a data da compra do veículo (no formato AAAAMMDD): ')
    }

for placa in frota:
    print(f'{placa}')
    for chave, valor in frota[placa].items(): print(f'\t{chave}: {valor}')

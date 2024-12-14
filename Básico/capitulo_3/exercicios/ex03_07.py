investimento = float(input('Investimento: R$'))
custos = float(input('Custos: R$'))
receita = float(input('Receita: R$'))

roi = ((receita - (custos + investimento)) / (custos + investimento)) * 100

print(f'{roi = :.1f}%')

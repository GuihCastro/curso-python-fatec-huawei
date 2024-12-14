"""
Altere o programa do Exercício Proposto 7.8 acrescentando uma validação adicional para garantir
que a data fornecida seja válida. Por exemplo: a entrada 20242255 é válida segundo os critérios
estabelecidos no enunciado 7.8. Porém, 55/22/2024 não é uma data válida.
Neste exercício você deve garantir que a data seja válida (incluindo anos bissextos – para identificar
se um ano é bissexto veja o Exercício Proposto 4.8).
"""

while True:
    entrada = input('Forneça uma data no formato "aaaammdd": ')

    if entrada.isdigit() and len(entrada) == 8:
        dia = entrada[6:]
        mes = entrada[4:6]
        ano = entrada[:4]
        mes_valido = 1 <= int(mes) <= 12
        if not mes_valido:
            print('Mês inválido, burro.')
            break
        dia_valido = False
        ano_bissexto = int(ano) % 4 == 0 and int(ano) % 100 != 0 or int(ano) % 400 == 0

        if ano_bissexto:
            match mes:
                case '01' | '03' | '05' | '07' | '08' | '10' | '12':
                    dia_valido = 1 <= int(dia) <= 31
                    if not dia_valido:
                        print('Dia inválido, burro.')
                        break
                case '04' | '06' | '09' | '11':
                    dia_valido = 1 <= int(dia) <= 30
                    if not dia_valido:
                        print('Dia inválido, burro.')
                        break
                case '02':
                    dia_valido = 1 <= int(dia) <= 29
                    if not dia_valido:
                        print('Erro: Fevereiro pode ter no máximo 28 dias (não bissexto) ou 29 dias (bissexto).')
                        break
        else:
            match mes:
                case '01' | '03' | '05' | '07' | '08' | '10' | '12':
                    dia_valido = 1 <= int(dia) <= 31
                    if not dia_valido:
                        print('Dia inválido, burro.')
                        break
                case '04' | '06' | '09' | '11':
                    dia_valido = 1 <= int(dia) <= 30
                    if not dia_valido:
                        print('Dia inválido, burro.')
                        break
                case '02':
                    dia_valido = 1 <= int(dia) <= 28
                    if not dia_valido:
                        print('Erro: Fevereiro pode ter no máximo 28 dias (não bissexto) ou 29 dias (bissexto).')
                        break

        if mes_valido and dia_valido:
            print(f'A data informada foi: {dia}/{mes}/{ano}')
            break

        print('A data informada é inválida. Tente novamente.')
    else:
        print('Por favor, insira APENAS 8 valores numéricos. Tente novamente.')

segundos = int(input('Tempo (em segundos): '))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60

print(f'{horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)')

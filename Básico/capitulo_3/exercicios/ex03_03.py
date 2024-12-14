A = float(input('Número A: '))
B = float(input('Número B: '))
C = float(input('Número C: '))

R1 = A + B + C
R2 = A * B * C
R3 = 2 * (A + B) - C
R4 = (A + B + C) / 3
R5 = (2 * B + 3 * C) / (5 * A)
R6 = pow(A, 2) + pow(B, 2)

print(f'{R1 = :.3f}', end=' ')
print(f'{R2 = :.3f}', end=' ')
print(f'{R3 = :.3f}', end=' ')
print(f'{R4 = :.3f}', end=' ')
print(f'{R5 = :.3f}', end=' ')
print(f'{R6 = :.3f}')

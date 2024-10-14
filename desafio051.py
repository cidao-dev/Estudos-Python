primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(primeiro, 10, razão):
    print(f'{c}', end= ' -> ')
print('ACABOU')
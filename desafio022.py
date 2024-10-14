print('DESAFIO 022 DO CURSO EM VÍDEO DE PYTHON')

nome = str(input('Digite seu nome completo: '))
space = nome.count('')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome possui {len(nome.replace(" ", ""))} letras')
dividido = nome.split()
print(f'{nome} possui {dividido[0], len(dividido[0])}')

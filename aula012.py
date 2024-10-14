nome = str(input('Qual é o seu nome? '))
if nome == 'Rodrigo': #Uma condição simples
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Mario' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
else:                                       #Com as duas condições de if e else, se torna uma condição composta.
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {nome}!')
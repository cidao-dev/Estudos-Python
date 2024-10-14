print('SORTEIO DE ALUNO PARA APAGAR O QUADRO')

aluno1 = input('Digite o nome do 1º aluno a ser sorteado: ')
aluno2 = input('Digite o nome do 2º aluno a ser sorteado: ')
aluno3 = input('Digite o nome do 3º aluno a ser sorteado: ')
aluno4 = input('Digite o nome do 4º aluno a ser sorteado: ')

lista_alunos = ['aluno1', 'aluno2', 'aluno3', 'aluno4']
aluno = random.choice(lista_alunos)

print(f'O aluno sorteado é o(a): {aluno}')

print('DESAFIO 036 CURSO EM VÍDEO GUANBABARA - PYTHON')

casa = float(input('Qual o valor da casa? '))
vezes = float(input('Quantas vezes quer pagar? '))
salario = float(input('Qual sua renda mensal? '))

prestacao = vezes * 12

prestacao_mensal = casa / prestacao


if prestacao >= prestacao_mensal:
    print(f'Se o emprestimo for aprovado, sua parcela será de R${prestacao_mensal:.2f}.')
else:
    print(f'Seu emprestomo foi recusado. O valor da parcela mensal é de R${prestacao_mensal:.2f} ultrapassou 30% de sua renda mensal que é de R${salario}.')





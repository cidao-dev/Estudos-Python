print('APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO PARA COMPRA DE CASA')

# Entrada de dados
valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar o empréstimo? '))

# Cálculo da quantidade total de parcelas
parcelas = anos * 12

# Cálculo do valor da parcela
prestacao_mensal = valor_casa / parcelas

# Verificação se a prestação mensal é menor ou igual a 30% do salário
limite = salario * 0.30

print(f'Valor da prestação mensal: R$ {prestacao_mensal:.2f}')

if prestacao_mensal <= limite:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado. A prestação excede 30% do seu salário.')



print('BEM-VINDO À CALCULADORA')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
operacao = input('Qual operação você deseja utilizar: (+, -, *, /): ')

if operacao == '+':
    resultado = num1 + num2
    print(f'O resultado é: {resultado}')

elif operacao == '_':
    resultado = num1 - num2
    print(f'O resultado é: {resultado}')


elif operacao == '*':
    resultado = num1 * num2
    print(f'O resultado é: {resultado}')


elif operacao == '/':
    resultado = num1 / num2
    print(f'O resultado é: {resultado}')


else:

    print('Operação inválida')
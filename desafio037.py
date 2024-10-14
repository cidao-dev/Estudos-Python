def converter_numero(numero, base):
    if base == 1:
        return bin(numero)[2:]  # Remove o prefixo '0b'
    elif base == 2:
        return oct(numero)[2:]  # Remove o prefixo '0o'
    elif base == 3:
        return hex(numero)[2:]  # Remove o prefixo '0x'
    else:
        return None

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return

    print("Escolha a base de conversão:")
    print("1 - Binário")
    print("2 - Octal")
    print("3 - Hexadecimal")

    try:
        base = int(input("Digite o número da base desejada: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro para a base.")
        return

    if base in [1, 2, 3]:
        resultado = converter_numero(numero, base)
        if resultado is not None:
            print(f"O número {numero} convertido para a base escolhida é: {resultado}")
        else:
            print("Base de conversão inválida.")
    else:
        print("Opção de base inválida. Por favor, escolha entre 1, 2 ou 3.")

if __name__ == "__main__":
    main()
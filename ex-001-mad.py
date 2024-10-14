# Contador de acessos ao site X com menu de opções
def carregar_contador():
    try:
        with open("contador_acessos.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def salvar_contador(contador):
    with open("contador_acessos.txt", "w") as file:
        file.write(str(contador))

def registrar_acesso():
    contador = carregar_contador()
    contador += 1
    salvar_contador(contador)
    print(f"Acesso registrado! Total de acessos: {contador}")

def exibir_acessos():
    contador = carregar_contador()
    print(f"Total de acessos até agora: {contador}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Registrar um novo acesso")
        print("2. Ver total de acessos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_acesso()
        elif opcao == '2':
            exibir_acessos()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()

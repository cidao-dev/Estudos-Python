# Contador de acessos ao site X
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
    print(f"Total de acessos: {contador}")

def main():
    print("Simulando acesso ao site X...")
    registrar_acesso()

if __name__ == "__main__":
    main()

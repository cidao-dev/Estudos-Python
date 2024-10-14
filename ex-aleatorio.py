# Gerenciador de Tarefas Simples
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso.")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            print("\nTarefas Pendentes:")
            for idx, tarefa in enumerate(self.tarefas, 1):
                print(f"{idx}. {tarefa}")

    def remover_tarefa(self, indice):
        try:
            tarefa_removida = self.tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso.")
        except IndexError:
            print("Índice inválido. Tente novamente.")


def menu():
    print("\n--- Menu ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    return input("Escolha uma opção: ")


def main():
    gerenciador = GerenciadorDeTarefas()

    while True:
        opcao = menu()

        if opcao == '1':
            tarefa = input("Digite a tarefa: ")
            gerenciador.adicionar_tarefa(tarefa)

        elif opcao == '2':
            gerenciador.listar_tarefas()

        elif opcao == '3':
            gerenciador.listar_tarefas()
            indice = int(input("Digite o número da tarefa a remover: "))
            gerenciador.remover_tarefa(indice)

        elif opcao == '4':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()

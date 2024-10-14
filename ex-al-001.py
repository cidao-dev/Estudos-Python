# Gerenciador de Concursos e Editais
class Concurso:
    def __init__(self, nome, edital):
        self.nome = nome
        self.edital = edital

class GerenciadorDeConcursos:
    def __init__(self):
        self.concursos = []

    def adicionar_concurso(self, nome, edital):
        self.concursos.append(Concurso(nome, edital))

    def listar_concursos(self):
        for concurso in self.concursos:
            print(f"Concurso: {concurso.nome}, Edital: {concurso.edital}")

    def buscar_por_edital(self, edital):
        for concurso in self.concursos:
            if edital in concurso.edital:
                print(f"Encontrado: {concurso.nome} ({concurso.edital})")

gerenciador = GerenciadorDeConcursos()
gerenciador.adicionar_concurso("Concurso Prefeitura", "2024-01")
gerenciador.adicionar_concurso("Concurso Polícia", "2023-05")
gerenciador.listar_concursos()
gerenciador.buscar_por_edital("2023")

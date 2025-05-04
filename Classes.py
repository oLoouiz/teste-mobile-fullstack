import json

#Classe de construção da tarefa
class Tarefa:
    def __init__(self, titulo, dataEntrega=None, prioridade=""):
        self.titulo = titulo
        self.dataEntrega = dataEntrega
        self.prioridade = prioridade
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return{
            "titulo": self.titulo,
            "dataEntrega": self.dataEntrega,
            "prioridade": self.prioridade,
            "concluida": self.concluida
        }

    def __str__(self):
        status = "✅" if self.concluida else "❌"
        return f"{status} {self.titulo} | Prioridade: {self.prioridade or 'Não definida'} | Data: {self.dataEntrega or 'Não definida'}"

    @classmethod
    def fromDict(cls, dados):
        tarefa = cls(
            titulo=dados["titulo"],
            dataEntrega=dados.get("dataEntrega"),
            prioridade=dados.get("prioridade", "")
        )
        tarefa.concluida = dados.get("concluida", False)
        return tarefa



#Classe de implentação das Funções
class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionarTarefa(self, tarefa):
            self.tarefas.append(tarefa)

    def listarTarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            status = "✅" if tarefa.concluida else "❌"
            print(f"[{i}] {status} {tarefa.titulo} | Prioridade: {tarefa.prioridade} Entrega: | {tarefa.dataEntrega or 'Não definida'}")

    def removerTarefa(self, indice: int):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)

    def concluirTarefa(self, indice: int):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()








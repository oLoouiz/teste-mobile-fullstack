import json
from Classes import Tarefa

def salvarTarefas(arquivo, tarefas):
    with open(arquivo, "w", encoding ="utf-8") as f:
        json.dump([tarefa.to_dict() for tarefa in tarefas], f, indent= 4, ensure_ascii= False)

def carregarTarefas(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [Tarefa.fromDict(d) for d in dados]
    except FileNotFoundError:
        return []


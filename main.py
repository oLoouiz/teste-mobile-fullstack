from Classes import Tarefa
from Classes import ToDoList
from Save.Persistencia import salvarTarefas, carregarTarefas
from Save.log import salvarLog
import os

ArquivoTarefas = "Save/tarefas.json"

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibirMenu():
    print("\n===== To Do List =====")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Remover Tarefa")
    print("5 - Encerrar")
    print("\n")

def main():
    lista = ToDoList()
    lista.tarefas = carregarTarefas(ArquivoTarefas)

    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                limpar_console()
                titulo = input("Digite o Título da Tarefa: ")
                data = input("Digite a data de entrega (opcional): ") or None
                prioridade = input("Digite a prioridade da tarefa (Baixa, Média, Alta) ") or "Baixa"
                tarefa = Tarefa(titulo, data, prioridade)
                lista.adicionarTarefa(tarefa)
                salvarTarefas(ArquivoTarefas, lista.tarefas)
                limpar_console()
                salvarLog(f"✅ Tarefa Adicionada: {tarefa}")
                print(f"✅ Tarefa '{tarefa.titulo}' adicionada!")

            case "2":
                limpar_console()
                print("\n📰 Lista de Tarefas")
                lista.listarTarefas()

            case "3":
                limpar_console()
                if len(lista.tarefas) == 0:
                    print("⚠ Não há tarefas para concluir.")
                else:
                    print("\n📝 Lista de Tarefas para Concluir:")
                    lista.listarTarefas()
                    try:
                        indice = int(input("Número da tarefa para concluir: ")) - 1
                        if 0 <= indice < len(lista.tarefas):  # Verifica se o índice é válido
                            lista.concluirTarefa(indice)
                            salvarTarefas(ArquivoTarefas, lista.tarefas)
                            limpar_console()
                            tarefaConcluida = lista.tarefas[indice]
                            salvarLog(f"✅ Tarefa Concluída: {tarefaConcluida}")
                            print(f"✅ Tarefa '{tarefaConcluida.titulo}' marcada como Concluída!")

                        else:
                            print("⚠ Índice inválido.")
                    except ValueError:
                        print("⚠ Digite um número válido.")

            case "4":
                limpar_console()
                if len(lista.tarefas) == 0:
                    print("⚠ Não há tarefas para remover.")
                else:
                    print("\n🗑 Lista de Tarefas para Remover:")
                    lista.listarTarefas()
                    try:
                        indice = int(input("Número da tarefa para remover: ")) - 1
                        if 0 <= indice < len(lista.tarefas):  # Verifica se o índice é válido
                            tarefaRemovida = lista.tarefas[indice]
                            lista.removerTarefa(indice)
                            salvarTarefas(ArquivoTarefas, lista.tarefas)
                            salvarLog(f"🗑 Tarefa Removida: {tarefaRemovida}")
                            print(f"🗑 Tarefa '{tarefaRemovida.titulo}' removida!")
                        else:
                            print("⚠ Índice inválido.")
                    except ValueError:
                        print("⚠ Digite um número válido.")

            case "5":
                salvarTarefas(ArquivoTarefas, lista.tarefas)
                print("💾 Tarefas salvas.")
                break

            case _:
                print("❌ Opção Inválida")

main()

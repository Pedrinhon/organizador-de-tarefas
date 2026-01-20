import time



def remover_tf(tarefas, ver_tf, salvar_tarefas):
    if len(tarefas) != 0:
        ver_tf(tarefas)

        try:
            numero = int(input("Digite o número da tarefa que deseja remover: "))

            # Remove a tarefa pelo índice
            tarefa_removida = tarefas.pop(numero - 1)

            # Salva alteração
            salvar_tarefas()

            print(f"A tarefa '{tarefa_removida['nome']}' foi removida com sucesso!")
            time.sleep(2)

        except (ValueError, IndexError):
            print("Número inválido!")
            time.sleep(2)
    else:
        print("A lista está vazia!")
        time.sleep(2)

import time

def concluir_tf(tarefas, ver_tf, salvar_tarefas):
    if len(tarefas) != 0:
        ver_tf(tarefas)

        try:
            numero = int(input("Digite o número da tarefa concluída: "))

            # Marca como concluída
            tarefas[numero - 1]["concluida"] = True

            # Salva alteração
            salvar_tarefas()

            print("Tarefa marcada como concluída!")
            time.sleep(2)

        except (ValueError, IndexError):
            print("Número inválido!")
            time.sleep(2)
    else:
        print("A lista está vazia!")
        time.sleep(2)

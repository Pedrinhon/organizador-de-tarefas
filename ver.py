import time


def ver_tf(tarefas):
    if len(tarefas) != 0:
        for i, tarefa in enumerate(tarefas, start=1):
            # Mostra X se estiver concluída
            status = "X" if tarefa["concluida"] else " "
            print(f"{i} - [{status}] {tarefa['nome']}")
            time.sleep(1)
    else:
        print("Você não listou nenhuma tarefa ainda!")
        time.sleep(2)

import time

def adicionar_tf(tarefas, salvar_tarefas):
    nome = input("Digite uma tarefa que quer adicionar: ")

    # Cria a tarefa como dicionário
    tarefa = {
        "nome": nome,
        "concluida": False
    }

    # Adiciona na lista
    tarefas.append(tarefa)

    # Salva no arquivo
    salvar_tarefas()

    print(f"A tarefa '{nome}' foi adicionada à lista!")
    time.sleep(2)

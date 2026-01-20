import time
from adicionar import adicionar_tf
from ver import ver_tf
from remover import remover_tf
from concluir import concluir_tf

# ==================================================
# LISTA GLOBAL DE TAREFAS
# Cada tarefa é um dicionário:
# {"nome": str, "concluida": bool}
# ==================================================
tarefas = []


# ==================================================
# MENU PRINCIPAL
# ==================================================
def mostrar_menu():
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Adicionar uma tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover uma tarefa")
    print("4 - Marcar tarefa como concluída")
    print("0 - Sair")

# ==================================================
# SALVAR TAREFAS EM ARQUIVO .TXT
# ==================================================
def salvar_tarefas():
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            # Formato: nome;True ou False
            linha = f"{tarefa['nome']};{tarefa['concluida']}\n"
            arquivo.write(linha)


# ==================================================
# CARREGAR TAREFAS DO ARQUIVO .TXT
# ==================================================
def carregar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, concluida = linha.strip().split(";")

                tarefas.append({
                    "nome": nome,
                    "concluida": concluida == "True"
                })
    except FileNotFoundError:
        # Se o arquivo não existir, começa com lista vazia
        pass


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================
carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tf(tarefas, salvar_tarefas)

    elif opcao == "2":
        ver_tf(tarefas)

    elif opcao == "3":
        remover_tf(tarefas, ver_tf, salvar_tarefas)

    elif opcao == "4":
        concluir_tf(tarefas, ver_tf, salvar_tarefas)
        
    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")

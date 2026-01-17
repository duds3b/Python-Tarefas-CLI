tarefas = []

def adicionar_tarefa():
    titulo = input("Digite a tarefa: ").strip()
    if titulo == "":
        print("Tarefa vazia não pode.")
        return

    tarefa = {
        "titulo": titulo,
        "feita": False
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa ainda.")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for i in range(len(tarefas)):
        status = "OK" if tarefas[i]["feita"] else "PENDENTE"
        print(f"{i+1}) [{status}] {tarefas[i]['titulo']}")

def marcar_concluida():
    listar_tarefas()
    if len(tarefas) == 0:
        return

    try:
        num = int(input("Número da tarefa pra concluir: "))
        indice = num - 1
        tarefas[indice]["feita"] = True
        print("Fechou. Marcada como concluída.")
    except:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) == 0:
        return

    try:
        num = int(input("Número da tarefa pra remover: "))
        indice = num - 1
        removida = tarefas.pop(indice)
        print("Removida:", removida["titulo"])
    except:
        print("Número inválido.")

while True:
    print("\n=== MENU ===")
    print("1) Adicionar tarefa")
    print("2) Listar tarefas")
    print("3) Marcar como concluída")
    print("4) Remover tarefa")
    print("0) Sair")

    op = input("Escolha: ").strip()

    if op == "1":
        adicionar_tarefa()
    elif op == "2":
        listar_tarefas()
    elif op == "3":
        marcar_concluida()
    elif op == "4":
        remover_tarefa()
    elif op == "0":
        print("Falou.")
        break
    else:
        print("Opção inválida.")

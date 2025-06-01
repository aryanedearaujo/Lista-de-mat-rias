lista_estudos = []
continuar = True

def exibir_menu():
    print("\n📘 MENU - Lista de Estudos")
    print("1 - Adicionar matéria")
    print("2 - Listar matérias")
    print("3 - Deletar matéria")
    print("4 - Exibir menu novamente")
    print("5 - Sair")

def adicionar_materia():
    materia = input("Digite a matéria pendente: ")
    lista_estudos.append(materia)
    print("✅ Matéria adicionada com sucesso!")

def listar_materias():
    print("📚 Matérias pendentes:")
    tamanho = len(lista_estudos)
    if tamanho == 0:
        print("Nenhuma matéria cadastrada ainda.")
    else:
        i = 0
        while i < tamanho:
            print(str(i + 1) + ". " + lista_estudos[i])
            i = i + 1

def deletar_materia():
    tamanho = len(lista_estudos)
    if tamanho == 0:
        print("Não há matérias para remover.")
    else:
        listar_materias()
        numero = input("Digite o número da matéria que deseja remover: ")
        indice = int(numero) - 1
        if indice >= 0 and indice < tamanho:
            removida = lista_estudos.pop(indice)
            print("🗑️ Matéria '" + removida + "' removida com sucesso.")
        else:
            print("Número inválido. Tente novamente.")

# Mostra o menu no início
exibir_menu()

while continuar:
    opcao = input("\nO que deseja fazer?: ")

    if opcao == "1":
        adicionar_materia()

    elif opcao == "2":
        listar_materias()

    elif opcao == "3":
        deletar_materia()

    elif opcao == "4":
        exibir_menu()

    elif opcao == "5":
        continuar = False
        print("👋 Encerrando o programa. Bons estudos!")

    else:
        print("❌ Opção inválida! Digite novamente.")


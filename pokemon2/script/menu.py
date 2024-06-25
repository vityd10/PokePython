# Menu

# Função para exibir o menu inicial e retornar a escolha do usuário
def menu_inicial():
    print("Bem vindo ao jogo Pokemon 2.0")
    print("1 - Novo jogo")
    print("2 - Carregar jogo")
    print("3 - Sair")
    escolha = input()
    if escolha == "1":
        return "New"
    elif escolha == "2":
        return "Load"
    elif escolha == "3":
        return "Quit"
    else:
        print("Escolha uma opção válida")
        menu_inicial()

# Primeiro menu após carregar o jogo
def lobby_inicial():
    opcoes = ["Ir para as Rotas", "Ver Treinador", "Salvar", "Sair"]
    print("Menu de escolhas")
    mostrar_escolhas(opcoes)
    escolha = input()
    match escolha:
        case "1":
            return f"Rotas"
        case "2":
            return f"Treinador"
        case "3":
            return f"Salvar"
        case "4":
            return f"Sair"
        case _:
            print("Escolha uma opção válida")
            lobby_inicial()


# Função para imprimir as opções de escolha
def mostrar_escolhas(escolhas):
        for escolha in escolhas:
             print(f"{escolhas.index(escolha) + 1}- {escolha}")


# Função para sair do jogo
def sair_do_jogo():
    opcao = input('''\nSair para:
1 - Voltar
2 - Voltar para o Menu Inicial 
3 - Sair do Jogo\n''')
    if opcao == "1":
        return "Voltar"
    elif opcao == "2":
        return "Inicio"
    elif opcao == "3":
        exit()
    else:
        print("Escolha uma opção válida")
        sair_do_jogo()

# Menu de Rotas
def menu_rotas(rotas):
    print("Menu de Rotas\nEscolha a rota:")
    i = 1
    for rota in rotas:
        print(i, "-", rota["nome"])
        i += 1
    escolha = int(input("Escolha uma rota: "))
    if escolha > len(rotas):
        print("Escolha uma opção válida")
        menu_rotas(rotas)
    escolha = rotas[escolha - 1]
    return escolha


def capturar_pokemon(pokemon):
    escolha = input("Deseja capturar "+ pokemon +"? (s/n) ")
    return escolha

def capturou(captura):
    if True in captura:
        print("Você capturou", captura[1])
    else:
        print("Você não capturou", captura[1])

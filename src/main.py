from menus.Clientes import menu_clientes
from menus.Menu import sair_do_programa, continuar_sistema
from menus.Guinchos import menu_guinchos
from menus.Motoristas import menu_motoristas

# Menu principal
def menu_principal(opcoes):
    print("\nMenu Principal:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

def opcoes():
    return int(input("Escolha uma opção: "))

while True:
    try:
        menu_principal(['Clientes', 'Guinchos', 'Motoristas', 'Sair do sistema'])
        opc1 = opcoes()

        match opc1:
            case 1:
                menu_clientes(['Adicionar cliente', 'Modificar dados de cliente', 'Listar clientes', 'Deletar Cliente', 'Sair do sistema'])
            case 2:
                menu_guinchos(['Adicionar guincho', 'Modificar dados do guincho', 'Listar guinchos', 'Deletar guincho', 'Sair do sistema'])
            case 3:
                menu_motoristas(['Adicionar motorista', 'Modificar dados do motorista', 'Listar motoristas', 'Deletar motorista', 'Sair do sistema'])
            case 4:
                sair_do_programa()
            case _:
                print("Opção inválida. Por favor, digite opção numérica válida.")
                continue

        continuar_sistema()

    except ValueError:
        print("\033[31mOpção inexistente. Por favor, digitar opção numérica válida. Ex: (1 - 7).\033[m")
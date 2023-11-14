from banco.conexao import executar_query, executar_select
from menus.Menu import continuar_sistema, sair_do_programa
from datetime import datetime

def listar_guinchos():
    try:
        query_listar_guinchos = """
            SELECT ID_GUINCHO, NM_MARCA, NM_MODELO, NMR_ANO, IDNT_PLACA, NM_COR, NM_CHASSI
            FROM T_ACG_GUINCHO
            WHERE DT_DELETADO IS NULL
        """
        guinchos = executar_select(query_listar_guinchos)

        if guinchos:
            print("Guinchos:")
            for guincho in guinchos:
                for nome_coluna, valor in zip(["ID_GUINCHO", "NM_MARCA", "NM_MODELO", "NMR_ANO", "IDNT_PLACA", "NM_COR", "NM_CHASSI"], guincho):
                    print(f"{nome_coluna}: {valor}")
                print("------")
        else:
            print("Nenhum guincho encontrado.")

    except Exception as ex:
        print(f"Erro ao listar guinchos: {ex}")


def adicionar_guincho():
    try:
        nm_marca = input("Digite a marca do guincho: ")
        nm_modelo = input("Digite o modelo do guincho: ")
        nmr_ano = input("Digite o ano do guincho: ")
        idnt_placa = input("Digite a placa do guincho: ")
        nm_cor = input("Digite a cor do guincho: ")
        nm_chassi = input("Digite o chassi do guincho: ")

        data_atual = datetime.now().strftime('%Y-%m-%d')


        listar_tipos_guincho()
        tipo = int(input("Selecione qual o tipo de guincho: "))
        query_adicionar_guinho = f"INSERT INTO T_ACG_GUINCHO (NM_MARCA, NM_MODELO, NMR_ANO, IDNT_PLACA, NM_COR, NM_CHASSI, DT_CRIADO, DT_ATUALIZADO, ID_TIPO) VALUES ('{nm_marca}', '{nm_modelo}', '{nmr_ano}', '{idnt_placa}', '{nm_cor}', '{nm_chassi}', TO_DATE('{data_atual}', 'YYYY-MM-DD'), TO_DATE('{data_atual}', 'YYYY-MM-DD'), {tipo})"

        executar_query(query_adicionar_guinho)
        print("Guincho adicionado com sucesso.")

    except Exception as ex:
        print(f"Erro ao adicionar guincho: {ex}")

def listar_tipos_guincho():
    try:
        query_listar_tipos = "SELECT ID_TIPO, NM_TIPO FROM T_ACG_TIPO_GUINCHO"
        tipos_guincho = executar_select(query_listar_tipos)
        if tipos_guincho:
            print("Tipos de Guincho:")
            for tipo in tipos_guincho:
                id_tipo, nm_tipo = tipo
                print(f"{id_tipo} - {nm_tipo}")
        else:
            print("Nenhum tipo de guincho encontrado.")

    except Exception as ex:
        print(f"Erro ao listar tipos de guincho: {ex}")

def modificar_guincho():
    try:
        # Solicitar o ID do guincho que deseja modificar
        id_guincho = int(input("Digite o ID do guincho que deseja modificar: "))

        # Solicitar novas informações do guincho
        nm_marca = input("Digite a nova marca do guincho: ")
        nm_modelo = input("Digite o novo modelo do guincho: ")
        nmr_ano = input("Digite o novo ano do guincho: ")
        idnt_placa = input("Digite a nova placa do guincho: ")
        nm_cor = input("Digite a nova cor do guincho: ")
        nm_chassi = input("Digite o novo chassi do guincho: ")

        data_atual = datetime.now().strftime('%Y-%m-%d')

        # Listar tipos de guincho para seleção
        listar_tipos_guincho()
        tipo = int(input("Selecione o novo tipo de guincho: "))

        # Criar a query de modificação
        query_modificar_guincho = f"""
            UPDATE T_ACG_GUINCHO
            SET NM_MARCA = '{nm_marca}',
                NM_MODELO = '{nm_modelo}',
                NMR_ANO = '{nmr_ano}',
                IDNT_PLACA = '{idnt_placa}',
                NM_COR = '{nm_cor}',
                NM_CHASSI = '{nm_chassi}',
                DT_ATUALIZADO = TO_DATE('{data_atual}', 'YYYY-MM-DD'),
                ID_TIPO = {tipo}
            WHERE ID_GUINCHO = {id_guincho}
        """

        # Executar a query de modificação
        executar_query(query_modificar_guincho)

        print("Guincho modificado com sucesso.")

    except Exception as ex:
        print(f"Erro ao modificar guincho: {ex}")

def deletar_guincho():
    try:
        # Solicitar o ID do guincho que deseja deletar
        id_guincho = int(input("Digite o ID do guincho que deseja deletar: "))

        data_atual = datetime.now().strftime('%Y-%m-%d')

        # Criar a query de deleção marcando a coluna DT_DELETADO
        query_deletar_guincho = f"""
            UPDATE T_ACG_GUINCHO
            SET DT_DELETADO = TO_DATE('{data_atual}', 'YYYY-MM-DD')
            WHERE ID_GUINCHO = {id_guincho}
        """

        # Executar a query de deleção
        executar_query(query_deletar_guincho)

        print("Guincho deletado com sucesso.")

    except Exception as ex:
        print(f"Erro ao deletar guincho: {ex}")

          
def obter_opcao():
    return int(input("Escolha uma opção: "))
   
def menu_guinchos(opcoes):
    while True:
        print("\nMenu Guinchos:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        opc2 = obter_opcao()

        if opc2 == 1:
            adicionar_guincho()
        elif opc2 == 2:
            modificar_guincho()
        elif opc2 == 3:
            listar_guinchos()
        elif opc2 == 4:
            deletar_guincho()
        elif opc2 == 5:
            sair_do_programa()
        else:
            print("Opção inválida. Por favor, digite opção numérica válida.")
            continuar_sistema()

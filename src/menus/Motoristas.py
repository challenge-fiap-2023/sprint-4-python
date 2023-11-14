from banco.conexao import executar_query, executar_select
from menus.Menu import continuar_sistema, sair_do_programa
from datetime import datetime

def obter_opcao():
    return int(input("Escolha uma opção: "))

def adicionar_motorista():
    try:
        # Solicitar informações do motorista
        nm_motorista = input("Digite o nome do motorista: ")
        nm_sobrenome = input("Digite o sobrenome do motorista: ")
        nmr_cpf = input("Digite o CPF do motorista: ")
        nmr_rg = input("Digite o RG do motorista (opcional): ")
        nmr_cnh = input("Digite o número da CNH do motorista: ")
        dt_nascimento = input("Digite a data de nascimento do motorista (YYYY-MM-DD): ")
        nmr_telefone = input("Digite o telefone do motorista (opcional): ")
        nmr_celular = input("Digite o celular do motorista (opcional): ")
        end_email = input("Digite o email do motorista: ")
        url_foto = input("Digite a URL da foto do motorista (opcional): ")

        data_atual = datetime.now().strftime('%Y-%m-%d')

        # Criar a query para adicionar o motorista
        query_adicionar_motorista = f"""
            INSERT INTO T_ACG_MOTORISTAS (
                NM_MOTORISTA, NM_SOBRENOME, NMR_CPF, NMR_RG, NMR_CNH, DT_NASCIMENTO,
                NMR_TELEFONE, NMR_CELULAR, END_EMAIL, URL_FOTO, DT_CRIADO, DT_ATUALIZADO
            ) VALUES (
                '{nm_motorista}', '{nm_sobrenome}', '{nmr_cpf}', '{nmr_rg}', '{nmr_cnh}', TO_DATE('{dt_nascimento}', 'YYYY-MM-DD'),
                '{nmr_telefone}', '{nmr_celular}', '{end_email}', '{url_foto}', TO_DATE('{data_atual}', 'YYYY-MM-DD'), TO_DATE('{data_atual}', 'YYYY-MM-DD')
            )
        """

        # Executar a query para adicionar o motorista
        executar_query(query_adicionar_motorista)

        print("Motorista adicionado com sucesso.")

    except Exception as ex:
        print(f"Erro ao adicionar motorista: {ex}")

def listar_motoristas():
    try:
        query_listar_motoristas = """
            SELECT ID_MOTORISTA, NM_MOTORISTA, NM_SOBRENOME, NMR_CPF, NMR_RG, NMR_CNH,
                   DT_NASCIMENTO, NMR_TELEFONE, NMR_CELULAR, END_EMAIL, URL_FOTO
            FROM T_ACG_MOTORISTAS
            WHERE DT_DELETADO IS NULL
        """
        motoristas = executar_select(query_listar_motoristas)

        if motoristas:
            print("Motoristas:")
            for motorista in motoristas:
                for nome_coluna, valor in zip(
                    ["ID_MOTORISTA", "NM_MOTORISTA", "NM_SOBRENOME", "NMR_CPF", "NMR_RG", "NMR_CNH",
                     "DT_NASCIMENTO", "NMR_TELEFONE", "NMR_CELULAR", "END_EMAIL", "URL_FOTO"], motorista):
                    print(f"{nome_coluna}: {valor}")
                print("------")
        else:
            print("Nenhum motorista encontrado.")

    except Exception as ex:
        print(f"Erro ao listar motoristas: {ex}")

def modificar_motorista():
    try:
        id_motorista = int(input("Digite o ID do motorista que deseja modificar: "))
        motorista = obter_dados_motorista(id_motorista)

        if motorista:
            print("Dados atuais do motorista:")
            for nome_coluna, valor in zip(
                ["ID_MOTORISTA", "NM_MOTORISTA", "NM_SOBRENOME", "NMR_CPF", "NMR_RG", "NMR_CNH",
                 "DT_NASCIMENTO", "NMR_TELEFONE", "NMR_CELULAR", "END_EMAIL", "URL_FOTO"], motorista):
                print(f"{nome_coluna}: {valor}")

            # Solicitar informações atualizadas do motorista
            nm_motorista = input("Digite o novo nome do motorista: ")
            nm_sobrenome = input("Digite o novo sobrenome do motorista: ")
            # Adicione aqui os inputs para outras colunas que deseja modificar

            # Montar e executar a query de modificação
            query_modificar_motorista = f"""
                UPDATE T_ACG_MOTORISTAS
                SET NM_MOTORISTA = '{nm_motorista}', NM_SOBRENOME = '{nm_sobrenome}'
                -- Adicione outras colunas e valores conforme necessário
                WHERE ID_MOTORISTA = {id_motorista}
            """
            executar_query(query_modificar_motorista)
            print("Motorista modificado com sucesso.")
        else:
            print("Motorista não encontrado.")

    except Exception as ex:
        print(f"Erro ao modificar motorista: {ex}")

def deletar_motorista():
    try:
        # Solicitar o ID do motorista que deseja deletar
        id_motorista = int(input("Digite o ID do motorista que deseja deletar: "))

        data_atual = datetime.now().strftime('%Y-%m-%d')

        # Criar a query de deleção marcando a coluna DT_DELETADO
        query_deletar_motorista = f"""
            UPDATE T_ACG_MOTORISTAS
            SET DT_DELETADO = TO_DATE('{data_atual}', 'YYYY-MM-DD')
            WHERE ID_MOTORISTA = {id_motorista}
        """

        # Executar a query de deleção
        executar_query(query_deletar_motorista)

        print("Motorista deletado com sucesso.")

    except Exception as ex:
        print(f"Erro ao deletar motorista: {ex}")

def menu_motoristas(opcoes):
    while True:
        print("\nMenu Motoristas:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        opc2 = obter_opcao()

        if opc2 == 1:
            adicionar_motorista()
        elif opc2 == 2:
            modificar_motorista()
        elif opc2 == 3:
            listar_motoristas()
        elif opc2 == 4:
            deletar_motorista()
        elif opc2 == 5:
            sair_do_programa()
        else:
            print("Opção inválida. Por favor, digite opção numérica válida.")
            continuar_sistema()

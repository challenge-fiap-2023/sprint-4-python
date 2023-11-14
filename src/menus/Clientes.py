from menus.Menu import continuar_sistema, sair_do_programa
from banco.conexao import executar_query, executar_select
import random
import string
from datetime import datetime

def adicionar_cliente():
    tipo = int(input("Qual tipo do cliente? 0 - Físico | 1 - Jurídico: "))
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    celular = input("Digite o celular do cliente: ")
    data_atual = datetime.now().strftime('%Y-%m-%d')

    # Inserir na tabela T_ACG_CLIENTE
    query_cliente = f"INSERT INTO T_ACG_CLIENTE (TP_CLIENTE, END_EMAIL, NMR_TELEFONE, DS_SENHA, NMR_CELULAR, DT_CRIADO, DT_ATUALIZADO) VALUES ({tipo}, '{email}', '{telefone}', '{senha_aleatoria()}', '{celular}', TO_DATE('{data_atual}', 'YYYY-MM-DD'), TO_DATE('{data_atual}', 'YYYY-MM-DD'))"

    try:
        # Executar a query principal
        executar_query(query_cliente)

        # Lidar com informações específicas de cada tipo de cliente
        if tipo == 0:
            adicionar_cliente_fisico(email, data_atual)
        elif tipo == 1:
            adicionar_cliente_juridico(email, data_atual)

        print("Cliente adicionado com sucesso.")
    except Exception as ex:
        print(f"Erro ao adicionar cliente: {ex}")

def adicionar_cliente_fisico(email, data_atual):
    nm_fisico = input("Digite o nome do cliente físico: ")
    nm_sobrenome = input("Digite o sobrenome do cliente físico: ")
    nmr_cpf = input("Digite o CPF do cliente físico: ")
    dt_nascimento = input("Digite a data de nascimento do cliente físico (YYYY-MM-DD): ")
    nm_sexo = input("Digite o sexo do cliente físico: ")
    nm_rg = input("Digite o RG do cliente físico: ")

    # Subconsulta para obter o ID_CLIENTE com base no email
    subquery = f"(SELECT MAX(ID_CLIENTE) FROM T_ACG_CLIENTE WHERE END_EMAIL = '{email}')"

    # Query para inserir na tabela T_ACG_CLIENTE_FISICO
    query_cliente_fisico = f"INSERT INTO T_ACG_CLIENTE_FISICO (NM_FISICO, NM_SOBRENOME, NMR_CPF, DT_NASCIMENTO, NM_SEXO, DT_CRIADO, DT_ATUALIZADO, ID_CLIENTE, NMR_RG) VALUES ('{nm_fisico}', '{nm_sobrenome}', '{nmr_cpf}', TO_DATE('{dt_nascimento}', 'YYYY-MM-DD'), '{nm_sexo}', TO_DATE('{data_atual}', 'YYYY-MM-DD'), TO_DATE('{data_atual}', 'YYYY-MM-DD'), {subquery}, '{nm_rg}')"

    # Executar a query específica para cliente físico
    executar_query(query_cliente_fisico)

def adicionar_cliente_juridico(email, data_atual):
    nm_razao_social = input("Digite a razão social do cliente jurídico: ")
    nmr_cnpj = input("Digite o CNPJ do cliente jurídico: ")
    nm_fantasia = input("Digite o nome fantasia do cliente jurídico: ")
    insc_estadual = input("Digite a inscrição estadual do cliente jurídico: ")

    # Subconsulta para obter o ID_CLIENTE com base no email
    subquery = f"(SELECT MAX(ID_CLIENTE) FROM T_ACG_CLIENTE WHERE END_EMAIL = '{email}')"

    # Query para inserir na tabela T_ACG_CLIENTE_JURIDICO
    query_cliente_juridico = f"INSERT INTO T_ACG_CLIENTE_JURIDICO (NM_RAZAO_SOCIAL, NMR_CNPJ, NM_FANTASIA, INSC_ESTADUAL, DT_CRIADO, DT_ATUALIZADO, DT_DELETADO, ID_CLIENTE) VALUES ('{nm_razao_social}', '{nmr_cnpj}', '{nm_fantasia}', '{insc_estadual}', TO_DATE('{data_atual}', 'YYYY-MM-DD'), TO_DATE('{data_atual}', 'YYYY-MM-DD'), NULL, {subquery})"

    # Executar a query específica para cliente jurídico
    executar_query(query_cliente_juridico)
        
        
def senha_aleatoria():
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(6))
    return senha

def modificar_cliente():
    id_cliente = int(input("Digite o ID do cliente que deseja modificar: "))
    tipo_cliente = obter_tipo_cliente(id_cliente)
    print(tipo_cliente)

    if tipo_cliente == 0:
        modificar_cliente_fisico(id_cliente)
    elif tipo_cliente == 1:
        modificar_cliente_juridico(id_cliente)
    else:
        print("Cliente não encontrado.")

def modificar_cliente_fisico(id_cliente):
    # Obter dados atuais do cliente físico
    query_obter_cliente = f"SELECT NM_FISICO, NM_SOBRENOME, NMR_CPF, DT_NASCIMENTO, NM_SEXO, NMR_RG FROM T_ACG_CLIENTE_FISICO WHERE ID_CLIENTE = {id_cliente}"
    dados_atuais = executar_select(query_obter_cliente)

    if dados_atuais:
        nm_fisico_atual = dados_atuais[0][0]
        nm_sobrenome_atual = dados_atuais[0][1]
        nmr_cpf_atual = dados_atuais[0][2]
        dt_nascimento_atual = dados_atuais[0][3]
        nm_sexo_atual = dados_atuais[0][4]
        nm_rg_atual = dados_atuais[0][5]

        # Solicitar ao usuário os novos dados
        nm_fisico_novo = input(f"Atual: {nm_fisico_atual}. Novo Nome Físico: ")
        nm_sobrenome_novo = input(f"Atual: {nm_sobrenome_atual}. Novo Sobrenome: ")
        nmr_cpf_novo = input(f"Atual: {nmr_cpf_atual}. Novo CPF: ")
        dt_nascimento_novo = input(f"Atual: {dt_nascimento_atual}. Nova Data de Nascimento (YYYY-MM-DD): ")
        nm_sexo_novo = input(f"Atual: {nm_sexo_atual}. Novo Sexo: ")
        nm_rg_novo = input(f"Atual: {nm_rg_atual}. Novo RG: ")

        # Atualizar os dados no banco de dados
        query_atualizar_cliente_fisico = f"""
            UPDATE T_ACG_CLIENTE_FISICO
            SET NM_FISICO = '{nm_fisico_novo}',
                NM_SOBRENOME = '{nm_sobrenome_novo}',
                NMR_CPF = '{nmr_cpf_novo}',
                DT_NASCIMENTO = TO_DATE('{dt_nascimento_novo}', 'YYYY-MM-DD'),
                NM_SEXO = '{nm_sexo_novo}',
                NMR_RG = '{nm_rg_novo}'
            WHERE ID_CLIENTE = {id_cliente}
        """
        executar_query(query_atualizar_cliente_fisico)
        print("Cliente físico atualizado com sucesso.")
    else:
        print("Cliente físico não encontrado.")

def modificar_cliente_juridico(id_cliente):
    # Lógica para modificar cliente jurídico
    pass

def obter_tipo_cliente(id_cliente):
    query = f"SELECT TP_CLIENTE FROM T_ACG_CLIENTE WHERE ID_CLIENTE = {id_cliente}"
    resultado = executar_select(query)

    if resultado:
        # Acessa o valor da primeira linha e da primeira coluna
        tipo_cliente = resultado[0][0]
        return tipo_cliente
    else:
        return None
    
def formatar_data(data):
    return data.strftime('%Y-%m-%d')  # Ajuste o formato conforme necessário


def listar_clientes():
    try:
        # Listar clientes físicos não excluídos
        query_listar_clientes_fisicos = """
            SELECT ID_CLIENTE, NM_FISICO, NM_SOBRENOME, NMR_CPF, DT_NASCIMENTO, NM_SEXO, NMR_RG
            FROM T_ACG_CLIENTE_FISICO
            WHERE DT_DELETADO IS NULL
        """
        clientes_fisicos = executar_select(query_listar_clientes_fisicos)

        if clientes_fisicos:
            print("Clientes Físicos:")
            for cliente in clientes_fisicos:
                for nome_coluna, valor in zip(["ID_CLIENTE", "NM_FISICO", "NM_SOBRENOME", "NMR_CPF", "DT_NASCIMENTO", "NM_SEXO", "NMR_RG"], cliente):
                    if nome_coluna == "DT_NASCIMENTO":
                        valor = formatar_data(valor)
                    print(f"{nome_coluna}: {valor}")
                print("------")
        else:
            print("Nenhum cliente físico encontrado.")

        # Listar clientes jurídicos não excluídos
        query_listar_clientes_juridicos = """
            SELECT ID_CLIENTE, NM_RAZAO_SOCIAL, NMR_CNPJ, NM_FANTASIA, INSC_ESTADUAL
            FROM T_ACG_CLIENTE_JURIDICO
            WHERE DT_DELETADO IS NULL
        """
        clientes_juridicos = executar_select(query_listar_clientes_juridicos)

        if clientes_juridicos:
            print("\nClientes Jurídicos:")
            for cliente in clientes_juridicos:
                for nome_coluna, valor in zip(["ID_CLIENTE", "NM_RAZAO_SOCIAL", "NMR_CNPJ", "NM_FANTASIA", "INSC_ESTADUAL"], cliente):
                    print(f"{nome_coluna}: {valor}")
                print("------")
        else:
            print("Nenhum cliente jurídico encontrado.")

    except Exception as ex:
        print(f"Erro ao listar clientes: {ex}")

def deletar_cliente():
    id_cliente = int(input("Digite o ID do cliente que deseja deletar: "))
    tipo_cliente = obter_tipo_cliente(id_cliente)

    if tipo_cliente == 0:
        deletar_cliente_fisico(id_cliente)
    elif tipo_cliente == 1:
        deletar_cliente_juridico(id_cliente)
    else:
        print("Cliente não encontrado.")

def deletar_cliente_fisico(id_cliente):
    try:
        # Marcar cliente físico como excluído
        query_deletar_cliente_fisico = f"""
            UPDATE T_ACG_CLIENTE_FISICO
            SET DT_DELETADO = SYSDATE
            WHERE ID_CLIENTE = {id_cliente}
        """
        executar_query(query_deletar_cliente_fisico)
        print("Cliente físico deletado com sucesso.")
    except Exception as ex:
        print(f"Erro ao deletar cliente físico: {ex}")

def deletar_cliente_juridico(id_cliente):
    try:
        query_deletar_cliente_juridico = f"""
            UPDATE T_ACG_CLIENTE_JURIDICO
            SET DT_DELETADO = SYSDATE
            WHERE ID_CLIENTE = {id_cliente}
        """
        executar_query(query_deletar_cliente_juridico)
        print("Cliente jurídico deletado com sucesso.")
    except Exception as ex:
        print(f"Erro ao deletar cliente jurídico: {ex}")
        
def obter_opcao():
    return int(input("Escolha uma opção: "))

def menu_clientes(opcoes):
    while True:
        print("\nMenu Clientes:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        opc2 = obter_opcao()

        if opc2 == 1:
            adicionar_cliente()
        elif opc2 == 2:
            modificar_cliente()
        elif opc2 == 3:
            listar_clientes()
        elif opc2 == 4:
            deletar_cliente()
        elif opc2 == 5:
            sair_do_programa()
        else:
            print("Opção inválida. Por favor, digite opção numérica válida.")
            continuar_sistema()

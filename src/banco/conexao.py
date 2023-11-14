import oracledb

def conectar_banco():
    try:
        connection = oracledb.connect(
            user="rm97617",
            password="110505",
            service_name="orcl",
            host="oracle.fiap.com.br",
            port=1521
        )
        print(connection.version)
        return connection
    except Exception as ex:
        print(ex)
        return None

def executar_query(query):
    connection = conectar_banco()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()  # Commit para efetivar a inserção
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
            print("Conexão finalizada.")

def executar_select(query):
    connection = conectar_banco()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            print(f"Erro durante a execução da consulta: {ex.args}")
        finally:
            connection.close()
            print("Conexão finalizada.")
    return None

from src.database.conexao import get_conexao


class Equipamento_repository:

    def __init__(self):
        self.equipamentos = []

    def adicionar_equipamento(self, equipamento):
        conexao = None
        cursor = None

        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            INSERT INTO equipamentos
            (id_cliente, marca, modelo, numero_serie, tipo)
            VALUES (%s, %s, %s, %s, %s)
            """

            valores = (
                equipamento.get_id_cliente(),
                equipamento.get_marca(),
                equipamento.get_modelo(),
                equipamento.get_numero_serie(),
                equipamento.get_tipo()
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Equipamento adicionado com sucesso!")

        except Exception as erro:
            print("Erro ao guardar equipamento!")
            print(erro)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def listar(self):
        conexao = None
        cursor = None

        try:
            conexao = get_conexao()
            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT id_equipamento,
                       id_cliente,
                       marca,
                       modelo,
                       numero_serie,
                       tipo
                FROM equipamentos
                ORDER BY id_equipamento
            """

            cursor.execute(sql)
            equipamentos = cursor.fetchall()

            return equipamentos

        except Exception as erro:
            print(f"Erro ao listar equipamentos: {erro}")
            return []

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir(self, id_equipamento):

        conexao = None
        cursor = None

        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            UPDATE equipamentos
            SET status = 0,
                deleted_at = NOW()
            WHERE id_equipamento = %s AND status = 1
            """

            cursor.execute(sql, (id_equipamento,))
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhum equipamento encontrado com esse ID.")
            else:
                print("Equipamento eliminado com sucesso!")

        except Exception as erro:
            print("Erro ao eliminar equipamento!")
            print(erro)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizar(self, id_equipamento, id_cliente, marca, modelo, numero_serie, tipo):
        conexao = None
        cursor = None

        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            UPDATE equipamentos
            SET id_cliente = %s,
                marca = %s,
                modelo = %s,
                numero_serie = %s,
                tipo = %s
            WHERE id_equipamento = %s
            """

            valores = (
                id_cliente,
                marca,
                modelo,
                numero_serie,
                tipo,
                id_equipamento
            )

            cursor.execute(sql, valores)
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhum equipamento encontrado com esse ID!")
            else:
                print("Equipamento atualizado com sucesso!")

        except Exception as erro:
            print("Erro ao atualizar equipamento!")
            print(erro)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
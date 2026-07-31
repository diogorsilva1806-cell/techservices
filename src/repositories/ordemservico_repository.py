from src.database.conexao import get_conexao


class OrdemServico_repository:

    def __init__(self):
        self.ordens_servico = []

    def adicionar_ordem_servico(self, ordem_servico):

        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            INSERT INTO ordens_servico
            (id_equipamento, defeito, diagnostico, solucao, prioridade, status, valor_total)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                ordem_servico.get_id_equipamento(),
                ordem_servico.get_defeito(),
                ordem_servico.get_diagnostico(),
                ordem_servico.get_solucao(),
                ordem_servico.get_prioridade(),
                ordem_servico.get_status(),
                ordem_servico.get_valor_total()
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Ordem de serviço adicionada com sucesso!")

        except Exception as erro:
            print("Erro ao guardar ordem de serviço!")
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
                SELECT id_ordem,
                       id_equipamento,
                       defeito,
                       diagnostico,
                       solucao,
                       prioridade,
                       status,
                       valor_total
                FROM ordens_servico
                ORDER BY id_ordem
            """

            cursor.execute(sql)
            ordens = cursor.fetchall()

            return ordens

        except Exception as erro:
            print(f"Erro ao listar ordens de serviço: {erro}")
            return []

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir(self, id_ordem):

        conexao = None
        cursor = None

        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            UPDATE ordens_servico
            SET status = 0,
                deleted_at = NOW()
            WHERE id_ordem = %s AND status = 1
            """

            cursor.execute(sql, (id_ordem,))
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhuma ordem de serviço encontrada com esse ID.")
            else:
                print("Ordem de serviço eliminada com sucesso!")

        except Exception as erro:
            print("Erro ao eliminar ordem de serviço!")
            print(erro)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizar(self, id_ordem, id_equipamento, defeito, diagnostico,
                  solucao, prioridade, status, valor_total):

        conexao = None
        cursor = None

        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            UPDATE ordens_servico
            SET id_equipamento = %s,
                defeito = %s,
                diagnostico = %s,
                solucao = %s,
                prioridade = %s,
                status = %s,
                valor_total = %s
            WHERE id_ordem = %s
            """

            valores = (
                id_equipamento,
                defeito,
                diagnostico,
                solucao,
                prioridade,
                status,
                valor_total,
                id_ordem
            )

            cursor.execute(sql, valores)
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhuma ordem de serviço encontrada com esse ID!")
            else:
                print("Ordem de serviço atualizada com sucesso!")

        except Exception as erro:
            print("Erro ao atualizar ordem de serviço!")
            print(erro)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
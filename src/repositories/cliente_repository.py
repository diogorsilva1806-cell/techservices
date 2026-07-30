from src.database.conexao import get_conexao



class Cliente_repository:

    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            INSERT INTO clientes (nome, email, telefone, status)
            VALUES (%s, %s, %s, %s)
            """

            valores = (
                cliente.get_nome(),
                cliente.get_email(),
                cliente.get_telefone(),
                cliente.get_status()
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Cliente adicionado com sucesso!")

        except Exception as erro:
            print("Erro ao guardar cliente!")
            print(erro)

        finally:
            cursor.close()
            conexao.close()

    def listar(self):
        try:
            conexao = get_conexao()
            cursor = conexao.cursor(dictionary=True)

            sql = """
                    SELECT id_cliente, nome, email, telefone, status,
                           created_at, updated_at, deleted_at
                    FROM clientes
                    WHERE status = 1
                    ORDER BY id_cliente
                """
            cursor.execute(sql)
            clientes = cursor.fetchall()

            # 2. Retornar a lista de clientes
            return clientes

        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            return []

        finally:
            # 3. Garantir que a conexão fecha SEMPRE, mesmo que ocorra um erro
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir(self, id_cliente):
        """
        Exclusão lógica: marca o cliente como inativo (status = 0) e
        regista deleted_at, sem apagar o registo da base de dados.
        """
        conexao = None
        cursor = None
        try:
            conexao = get_conexao()
            cursor = conexao.cursor()

            sql = """
            UPDATE clientes
            SET status = 0,
                deleted_at = NOW()
            WHERE id_cliente = %s AND status = 1
            """

            cursor.execute(sql, (id_cliente,))
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhum cliente encontrado com esse ID.")
            else:
                print("Cliente eliminado com sucesso!")

        except Exception as erro:
            print("Erro ao eliminar cliente!")
            print(erro)

        finally:
            if cursor:
                cursor.close()
            if conexao:
               conexao.close()
    def atualizar(self, id_cliente, novo_nome, novo_email, novo_telefone):
                    """
                    Atualiza os dados de um cliente existente e regista updated_at.
                    """
                    conexao = None
                    cursor = None
                    try:
                        conexao = get_conexao()
                        cursor = conexao.cursor()

                        sql = """
                        UPDATE clientes
                        SET nome = %s,
                            email = %s,
                            telefone = %s,
                            updated_at = NOW()
                        WHERE id_cliente = %s AND status = 1
                        """
                        valores = (novo_nome, novo_email, novo_telefone, id_cliente)

                        cursor.execute(sql, valores)
                        conexao.commit()

                        if cursor.rowcount == 0:
                            print("Nenhum cliente encontrado com esse ID!")
                        else:
                            print("Cliente atualizado com sucesso!")

                    except Exception as erro:
                        print("Erro ao atualizar cliente!")
                        print(erro)

                    finally:
                        if cursor is not None:
                            cursor.close()
                        if conexao is not None:
                            conexao.close()

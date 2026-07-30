class Cliente:


            def __init__(self, id_cliente,  nome, email, telefone, status):
                self.__id_cliente = id_cliente
                self.__nome = nome
                self.__email = email
                self.__telefone = telefone
                self.__status = status

            # Getters
            def get_id_cliente(self):
                return self.__id_cliente

            def get_nome(self):
                return self.__nome

            def get_email(self):
                return self.__email

            def get_telefone(self):
                return self.__telefone

            def get_status(self):
                return self.__status

            # Setters
            def set_id_cliente(self, novo_id_cliente):
                self.__id_cliente = novo_id_cliente

            def set_nome(self, novo_nome):
                self.__nome = novo_nome

            def set_email(self, novo_email):
                self.__email = novo_email

            def set_telefone(self, novo_telefone):
                self.__telefone = novo_telefone

            def set_status(self, novo_status):
                    self.__status = novo_status

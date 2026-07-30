class Equipamento:

    def __init__(self, id_equipamento, id_cliente, marca, modelo, numero_serie, tipo):
        self.__id_equipamento = id_equipamento
        self.__id_cliente = id_cliente
        self.__marca = marca
        self.__modelo = modelo
        self.__numero_serie = numero_serie
        self.__tipo = tipo

    # Getters
    def get_id_equipamento(self):
        return self.__id_equipamento

    def get_id_cliente(self):
        return self.__id_cliente

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_numero_serie(self):
        return self.__numero_serie

    def get_tipo(self):
        return self.__tipo

    # Setters
    def set_id_equipamento(self, novo_id):
        self.__id_equipamento = novo_id

    def set_id_cliente(self, novo_id_cliente):
        self.__id_cliente = novo_id_cliente

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_numero_serie(self, novo_numero_serie):
        self.__numero_serie = novo_numero_serie

    def set_tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    def mostrar_dados(self):
        print(f"ID Equipamento: {self.__id_equipamento}")
        print(f"ID Cliente: {self.__id_cliente}")
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Número de Série: {self.__numero_serie}")
        print(f"Tipo: {self.__tipo}")
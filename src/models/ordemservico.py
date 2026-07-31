import datetime


class OrdemServico:

    def __init__(self, id_ordem, id_equipamento, defeito, diagnostico=None,
                 solucao=None, prioridade='Média', status='Aberto',
                 valor_total=0.00, data_abertura=None):
        self.__id_ordem = id_ordem
        self.__id_equipamento = id_equipamento
        self.__defeito = defeito
        self.__diagnostico = diagnostico
        self.__solucao = solucao
        self.__prioridade = prioridade
        self.__status = status
        self.__valor_total = valor_total
        self.__data_abertura = data_abertura if data_abertura else datetime.datetime.now()

    # Getters
    def get_id_ordem(self):
        return self.__id_ordem

    def get_id_equipamento(self):
        return self.__id_equipamento

    def get_defeito(self):
        return self.__defeito

    def get_diagnostico(self):
        return self.__diagnostico

    def get_solucao(self):
        return self.__solucao

    def get_prioridade(self):
        return self.__prioridade

    def get_status(self):
        return self.__status

    def get_valor_total(self):
        return self.__valor_total

    def get_data_abertura(self):
        return self.__data_abertura

    # Setters
    def set_id_ordem(self, id_ordem):
        self.__id_ordem = id_ordem

    def set_id_equipamento(self, id_equipamento):
        self.__id_equipamento = id_equipamento

    def set_defeito(self, defeito):
        self.__defeito = defeito

    def set_diagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def set_solucao(self, solucao):
        self.__solucao = solucao

    def set_prioridade(self, prioridade):
        self.__prioridade = prioridade

    def set_status(self, status):
        self.__status = status

    def set_valor_total(self, valor_total):
        self.__valor_total = valor_total

    # Metodo de atualização de status (regista a transição de estado da ordem)
    def atualizar_status(self, novo_status):
        self.__status = novo_status

    def mostrar_dados(self):
        print("==== Dados Ordem de Serviço ====")
        print(f"ID: {self.__id_ordem}")
        print(f"Equipamento: {self.__id_equipamento}")
        print(f"Status: {self.__status}")
        print(f"Prioridade: {self.__prioridade}")
        print(f"Defeito: {self.__defeito}")
        print(f"Diagnóstico: {self.__diagnostico}")
        print(f"Solução: {self.__solucao}")
        print(f"Valor Total: {self.__valor_total}")
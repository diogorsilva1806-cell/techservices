from src.repositories.cliente_repository import Cliente_repository
from src.models.cliente import Cliente

from src.repositories.equipamento_repository import Equipamento_repository
from src.models.equipamento import Equipamento

from src.repositories.ordemservico_repository import OrdemServico_repository
from src.models.ordemservico import OrdemServico


cliente_repository = Cliente_repository()
equipamento_repository = Equipamento_repository()
ordemservico_repository = OrdemServico_repository()

while True:

    print("\n========== SISTEMA ==========")
    print("1 - Adicionar Cliente")
    print("2 - Listar Clientes")
    print("3 - Excluir Cliente")
    print("4 - Editar Cliente")
    print("5 - Inserir Equipamento")
    print("6 - Listar Equipamentos")
    print("7 - Excluir Equipamento")
    print("8 - Editar Equipamento")
    print("9 - Abrir Ordem de Serviço")
    print("10 - Listar Ordens de Serviço")
    print("11 - Listar Ordens por Equipamento")
    print("12 - Editar Ordem de Serviço")
    print("13 - Atualizar Status da Ordem")
    print("14 - Excluir Ordem de Serviço")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # ===================== CLIENTES =====================

    if opcao == "1":

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        status = input("Status: ")

        cliente = Cliente(
            None,
            nome,
            telefone,
            email,
            status
        )

        cliente_repository.adicionar_cliente(cliente)

    elif opcao == "2":

        clientes = cliente_repository.listar()

        print("\n----- CLIENTES -----")

        if not clientes:
            print("Nenhum cliente encontrado.")

        else:

            for c in clientes:

                print(
                    f"ID: {c.get('id_cliente')} | "
                    f"Nome: {c.get('nome')} | "
                    f"Telefone: {c.get('telefone')} | "
                    f"Email: {c.get('email')} | "
                    f"Status: {c.get('status')}"
                )

    elif opcao == "3":

        id_cliente = int(input("ID do cliente: "))
        cliente_repository.excluir(id_cliente)

    elif opcao == "4":

        id_cliente = int(input("ID do cliente: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        telefone = input("Novo telefone: ")

        cliente_repository.atualizar(
            id_cliente,
            nome,
            email,
            telefone
        )

    # ===================== EQUIPAMENTOS =====================

    elif opcao == "5":

        id_cliente = int(input("ID do cliente: "))
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        numero_serie = input("Número de série: ")
        tipo = input("Tipo: ")

        equipamento = Equipamento(
            None,
            id_cliente,
            marca,
            modelo,
            numero_serie,
            tipo
        )

        equipamento_repository.adicionar_equipamento(equipamento)

    elif opcao == "6":

        equipamentos = equipamento_repository.listar()

        print("\n----- EQUIPAMENTOS -----")

        if not equipamentos:
            print("Nenhum equipamento encontrado.")

        else:

            for e in equipamentos:

                print(
                    f"ID: {e.get('id_equipamento')} | "
                    f"Cliente: {e.get('id_cliente')} | "
                    f"Marca: {e.get('marca')} | "
                    f"Modelo: {e.get('modelo')} | "
                    f"Série: {e.get('numero_serie')} | "
                    f"Tipo: {e.get('tipo')}"
                )

    elif opcao == "7":

        id_equipamento = int(input("ID do equipamento: "))
        equipamento_repository.excluir(id_equipamento)

    elif opcao == "8":

        id_equipamento = int(input("ID do equipamento: "))
        id_cliente = int(input("Novo ID Cliente: "))
        marca = input("Nova marca: ")
        modelo = input("Novo modelo: ")
        numero_serie = input("Novo número de série: ")
        tipo = input("Novo tipo: ")

        equipamento_repository.atualizar(
            id_equipamento,
            id_cliente,
            marca,
            modelo,
            numero_serie,
            tipo
        )

    # ===================== ORDENS DE SERVIÇO =====================

    elif opcao == "9":

        id_equipamento = int(input("ID do equipamento: "))
        defeito = input("Defeito: ")
        diagnostico = input("Diagnóstico: ")
        solucao = input("Solução: ")

        prioridade = input(
            "Prioridade (Baixa/Média/Alta): "
        ) or "Média"

        status = input(
            "Status (Aberto/Em Diagnóstico/Concluído): "
        ) or "Aberto"

        valor_total = input("Valor Total: ")

        if valor_total == "":
            valor_total = 0
        else:
            valor_total = float(valor_total)

        ordem = OrdemServico(
            None,
            id_equipamento,
            defeito,
            diagnostico,
            solucao,
            prioridade,
            status,
            valor_total
        )

        ordemservico_repository.adicionar_ordem_servico(ordem)

    elif opcao == "10":

        ordens = ordemservico_repository.listar()

        print("\n----- ORDENS DE SERVIÇO -----")

        if not ordens:

            print("Nenhuma ordem encontrada.")

        else:

            for o in ordens:

                print(
                    f"""
ID: {o['id_ordem']}
Equipamento: {o['id_equipamento']}
Defeito: {o['defeito']}
Diagnóstico: {o['diagnostico']}
Solução: {o['solucao']}
Prioridade: {o['prioridade']}
Status: {o['status']}
Valor Total: {o['valor_total']}
--------------------------------------------
"""
                )

    elif opcao == "11":

        id_equipamento = int(
            input("ID do equipamento: ")
        )

        ordens = ordemservico_repository.listar_por_equipamento(
            id_equipamento
        )

        if not ordens:

            print("Nenhuma ordem encontrada.")

        else:

            for o in ordens:

                print(
                    f"""
ID: {o['id_ordem']}
Defeito: {o['defeito']}
Diagnóstico: {o['diagnostico']}
Solução: {o['solucao']}
Prioridade: {o['prioridade']}
Status: {o['status']}
Valor Total: {o['valor_total']}
--------------------------------------------
"""
                )

    elif opcao == "12":

        id_ordem = int(input("ID da Ordem: "))

        ordem = ordemservico_repository.buscar_por_id(id_ordem)

        if ordem is None:

            print("Ordem não encontrada.")

        else:

            id_equipamento = int(
                input(
                    f"ID Equipamento [{ordem['id_equipamento']}]: "
                )
                or ordem["id_equipamento"]
            )

            defeito = input(
                f"Defeito [{ordem['defeito']}]: "
            ) or ordem["defeito"]

            diagnostico = input(
                f"Diagnóstico [{ordem['diagnostico']}]: "
            ) or ordem["diagnostico"]

            solucao = input(
                f"Solução [{ordem['solucao']}]: "
            ) or ordem["solucao"]

            prioridade = input(
                f"Prioridade [{ordem['prioridade']}]: "
            ) or ordem["prioridade"]

            status = input(
                f"Status [{ordem['status']}]: "
            ) or ordem["status"]

            valor_total = input(
                f"Valor Total [{ordem['valor_total']}]: "
            )

            if valor_total == "":
                valor_total = ordem["valor_total"]
            else:
                valor_total = float(valor_total)

            ordemservico_repository.atualizar(
                id_ordem,
                id_equipamento,
                defeito,
                diagnostico,
                solucao,
                prioridade,
                status,
                valor_total
            )

    elif opcao == "13":

        id_ordem = int(input("ID da Ordem: "))
        status = input("Novo Status: ")

        ordemservico_repository.atualizar_status(
            id_ordem,
            status
        )

    elif opcao == "14":

        id_ordem = int(input("ID da Ordem: "))
        ordemservico_repository.excluir(id_ordem)

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida.")
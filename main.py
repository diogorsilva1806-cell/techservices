from src.repositories.cliente_repository import Cliente_repository
from src.models.cliente import Cliente

from src.repositories.equipamento_repository import Equipamento_repository
from src.models.equipamento import Equipamento

Cliente_repository = Cliente_repository()
Equipamento_repository = Equipamento_repository()

while True:

    print("\n===== SISTEMA =====")

    print("1 - Adicionar Cliente")
    print("2 - Listar Clientes")
    print("3 - Eliminar Cliente")
    print("4 - Editar Cliente")
    print("5 - Adicionar Equipamento")
    print("6 - Listar Equipamentos")
    print("7 - Eliminar Equipamento")
    print("8 - Editar Equipamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Insira o nome do cliente: ")
        telefone = input("Insira o telefone do cliente: ")
        email = input("Insira o email do cliente: ")
        status = input("Insira o status do cliente: ")

        cliente = Cliente(None, nome, telefone, email, status)
        Cliente_repository.adicionar_cliente(cliente)

    elif opcao == "2":

        clientes = Cliente_repository.listar()

        print("\n--- Lista de Clientes ---")

        if not clientes:

            print("Nenhum cliente foi encontrado!")

        else:

            for c in clientes:
                print(
                    f"ID: {c.get('id_cliente')} | Nome: {c.get('nome')} | Tel: {c.get('telefone')} | Email: {c.get('email')} | Status: {c.get('status')}"
                )

    elif opcao == "3":

        id_cliente = int(input("ID do cliente a eliminar: "))
        Cliente_repository.excluir(id_cliente)
        print("Cliente excluido com sucesso!")

    elif opcao == "4":

        id_cliente = int(input("ID do cliente a atualizar: "))
        novo_nome = input("Novo nome: ")
        novo_email = input("Novo email: ")
        novo_telefone = input("Novo telefone: ")

        Cliente_repository.atualizar(
            id_cliente,
            novo_nome,
            novo_email,
            novo_telefone
        )

    elif opcao == "5":

        id_cliente = int(input("Insira o ID do cliente: "))
        marca = input("Insira a marca do equipamento: ")
        modelo = input("Insira o modelo do equipamento: ")
        numero_serie = input("Insira o número de série: ")
        tipo = input("Insira o tipo do equipamento: ")

        equipamento1 = Equipamento(
            None,
            id_cliente,
            marca,
            modelo,
            numero_serie,
            tipo
        )

        Equipamento_repository.adicionar_equipamento(equipamento1)

    elif opcao == "6":

        equipamentos = Equipamento_repository.listar()

        print("\n--- Lista de Equipamentos ---")

        if not equipamentos:

            print("Nenhum equipamento foi encontrado!")

        else:

            for e in equipamentos:
                print(
                    f"ID: {e.get('id_equipamento')} | "
                    f"ID Cliente: {e.get('id_cliente')} | "
                    f"Marca: {e.get('marca')} | "
                    f"Modelo: {e.get('modelo')} | "
                    f"Número de Série: {e.get('numero_serie')} | "
                    f"Tipo: {e.get('tipo')}"
                )

    elif opcao == "7":

        id_equipamento = int(input("ID do equipamento a eliminar: "))
        Equipamento_repository.excluir(id_equipamento)
        print("Equipamento excluido com sucesso!")

    elif opcao == "8":

        id_equipamento = int(input("ID do equipamento a atualizar: "))
        id_cliente = int(input("Novo ID do cliente: "))
        nova_marca = input("Nova marca: ")
        novo_modelo = input("Novo modelo: ")
        novo_numero_serie = input("Novo número de série: ")
        novo_tipo = input("Novo tipo: ")

        Equipamento_repository.atualizar(
            id_equipamento,
            id_cliente,
            nova_marca,
            novo_modelo,
            novo_numero_serie,
            novo_tipo
        )

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida!")
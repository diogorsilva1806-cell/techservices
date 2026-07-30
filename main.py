from src.repositories.cliente_repository import Cliente_repository
Cliente_repository = Cliente_repository()
from src.models.cliente import Cliente

while True:

    print("\n===== SISTEMA =====")

    print("1 - Adicionar Cliente")
    print("2 - Listar Clientes")
    print("3 - Eliminar Cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Insira o nome do cliente: ")
        telefone = input("Insira o telefone do cliente: ")
        email = input("Insira o email do cliente: ")
        status = input("Insira o status do cliente: ")

        cliente = Cliente(id, nome, telefone, email, status)
        Cliente_repository.adicionar_cliente(cliente)


    elif opcao == "2":

        clientes = Cliente_repository.listar()

        print("\n--- Lista de Clientes ---")

        if not clientes:

            print("Nenhum cliente foi encontrado!")

        else:

            for c in clientes:
                print(

                    f"ID: {c.get('id_cliente')} | Nome: {c.get('nome')} | Tel: {c.get('telefone')} | Email: {c.get('email')} | Status: {c.get('status')}")

    elif opcao == "3":
        id_cliente = int(input("ID do cliente a eliminar: "))
        Cliente_repository.excluir(id_cliente)
        print("Cliente excluido com sucesso!")


    elif opcao == "0":
        print("Sistema encerrado.")

        break


    else:

        print("Opção inválida!")


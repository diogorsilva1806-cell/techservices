from src.database.conexao import get_conexao

def main():
    try:
        conexao = get_conexao()
        print("Conexão estabelecida com sucesso!")
        conexao.close()
        print("Conexão fechada. ")
    except Exception as erro:
        print("Erro ao conectar ao MySQL!")
        print(erro)


if __name__ == "__main__":
    main()
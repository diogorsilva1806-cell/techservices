import mysql.connector

def get_conexao():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="techservice_db",
        autocommit=False
    )

    return conexao
from mysql.connector import Error, connect

class ConexaoBanco:
    def get_connection(self):
        connection = None
        try:
            connection = connect(
                host="localhost",
                user="root",
                password='1234',
                database="jogo_python_terminal")
        except Error as e:
            print(f"Erro ao conectar! {e}")
            connection.close()
        return connection
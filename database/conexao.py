import mysql.connector


class conexao:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def conectadb(self):

        HOST = self.host  # 'scantoradb' #enter the oracle db host url
        DATABASE = self.database
        USERNAME = self.user  # 'usu_central' #enter your username
        PASSWORD = self.password  # 'toraqas' #enter your password
        try:
            con = mysql.connector.connect(
                host=HOST,
                database=DATABASE,
                user=USERNAME,
                passwd=PASSWORD
            )
            print("Conexão com o banco realizada com sucesso!.")
            return con

        except:
            print("Erro ao logar no banco de dados.")
            exit()

    def getPaginas(self, con):
        cur = con.cursor()
        query = 'select * from log_api'
        cur.execute(query)
        result = cur.fetchall()
        return result

    def getPaginas(self, con):
        cur = con.cursor()
        query = 'insert into log_api(data_req,payload,status_retorno,payload_retorno)values()'
        cur.execute(query)
        result = cur.fetchall()
        return result

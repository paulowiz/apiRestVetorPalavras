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

    def getLog(self, con):
        cur = con.cursor()
        query = "SELECT * FROM LOG_API ORDER BY LOG_SEQ DESC"
        cur.execute(query)
        result = cur.fetchall()
        return result

    def insereLog(self, con,LOG_METODO,LOG_ENDPOINT,LOG_ENVIO,LOG_RETORNO,LOG_STF_COD):
        cur = con.cursor()
        query = """insert into LOG_API(LOG_DT,LOG_METODO,LOG_ENDPOINT,LOG_ENVIO,LOG_RETORNO,LOG_STF_COD)values(NOW(),'%s','%s',"%s","%s",%s)"""%(LOG_METODO,LOG_ENDPOINT,LOG_ENVIO,LOG_RETORNO,LOG_STF_COD)
        cur.execute(query)
        con.commit()
        return print('Dados inseridos com sucesso!')

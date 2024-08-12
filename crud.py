import psycopg2

#Métodos crud:


class AppBD:
    def __init__(self):
        print('Método Construtor')

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="Yuki3legs",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="postgres")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

    # -----------------------------------------------------------------------------
    # Selecionar todos os Produtos
    # -----------------------------------------------------------------------------
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = """select * from public."redspider" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)


        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

    # -----------------------------------------------------------------------------
    # Inserir Produto
    # -----------------------------------------------------------------------------
    def inserirDados(self, tatuador, cliente, whatsapp, descricao, valor):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public."redspider" 
          ("tatuador", "cliente", "whatsapp", "descricao", "valor") VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = (tatuador, cliente, whatsapp, descricao, valor)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com successo na tabela REDSPIDER")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir registro na tabela REDSPIDER", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------
    # Atualizar Produto
    # -----------------------------------------------------------------------------
    def atualizarDados(self, ident, tatuador, cliente, whatsapp, descricao, valor):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização ")
            sql_select_query = """select * from public."redspider" 
            where "id" = %s"""
            cursor.execute(sql_select_query, (ident,))
            record = cursor.fetchone()
            print(record)
            # Atualizar registro
            sql_update_query = """Update public."redspider" set "tatuador" = %s, "cliente" = %s, 
            "whatsapp" = %s, "descricao" = %s, "valor" = %s where "id" = %s"""
            cursor.execute(sql_update_query, (tatuador, cliente, whatsapp, descricao, valor, ident))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."redspider" 
            where "id" = %s"""
            cursor.execute(sql_select_query, (ident,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # -----------------------------------------------------------------------------
    # Excluir Produto
    # -----------------------------------------------------------------------------
    def excluirDados(self, id):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Atualizar registro
            sql_delete_query = """Delete from public."redspider" 
            where "id" = %s"""
            cursor.execute(sql_delete_query, (id,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
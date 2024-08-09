import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres",
                        password="Yuki3legs",
                        host="127.0.0.1", port="5432")
print("Conexão com banco de dados realizado com sucesso!")
cur = conn.cursor()
cur.execute(
    '''CREATE TABLE REDSPIDER (ID BIGSERIAL PRIMARY KEY NOT NULL, Tatuador TEXT NOT NULL, Cliente TEXT NOT NULL, Whatsapp CHAR(12), Descricao TEXT NOT NULL, valor REAL NOT NULL);''')
print("Tabela criada com sucesso!")
conn.commit()

cur.close()
conn.close()

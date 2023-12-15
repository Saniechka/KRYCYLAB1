import sqlite3

class SqlliteDB:

    @staticmethod
    def createDBTable():
        conn = sqlite3.connect('logi.db')
        cursor = conn.cursor()


        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS logs (
                log_id INTEGER PRIMARY KEY,
                source TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()
   
    @staticmethod
    def connectDB():
        conn =sqlite3.connect("logi.db")
        cursor=conn.cursor()
        return  conn, cursor

    @staticmethod   
    def disconnectDB(conn):
        conn.close()

    @staticmethod
    def insertData(log_source,description,date):
       
        conn,cursor =SqlliteDB.connectDB()
        cursor.execute('SELECT MAX(log_id) FROM logs')
       
        max_log_id= cursor.fetchone()[0] #fetchone[0]
        next_log_id = max_log_id + 1 if max_log_id is not None else 1
       
        cursor.execute('INSERT INTO logs VALUES (?, ?, ?, ?)', (next_log_id, log_source, description, date))
        conn.commit()
        SqlliteDB.disconnectDB(conn)
       
    @staticmethod
    def selectDataByID(log_id):
        conn, cursor=SqlliteDB.connectDB()
        cursor.execute('SELECT * FROM logs WHERE log_id = ?', (log_id,))
        result = cursor.fetchone()

        SqlliteDB.disconnectDB(conn)
        return result
    
    @staticmethod
    def selectDataBySource(source):
        conn, cursor=SqlliteDB.connectDB()
        cursor.execute('SELECT * FROM logs WHERE source = ?', (source,))
        result = cursor.fetchall()

        SqlliteDB.disconnectDB(conn)
        return result

    @staticmethod
    def selectLastLogs(limit):
        conn, cursor = SqlliteDB.connectDB()

        cursor.execute('SELECT * FROM logs ORDER BY log_id DESC LIMIT ?', (limit,))
        result = cursor.fetchmany(limit)  
        SqlliteDB.disconnectDB(conn)
        return list(reversed(result))
   
'''for row in result:
    print(row)'''




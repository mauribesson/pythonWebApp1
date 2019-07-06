import psycopg2

class Database: 
    def __init__(self):
        self.commect = psycopg2.connect(host="localhost", port="5432", database="PythonWebApp", user="postgres", password="12345678")
        self.cursor = self.commect.cursor() 

    def query(self, query=""):     
        self.cursor.execute(query)
        #result = self.cursor.fetchone()
        result = self.cursor.fetchall()
        #self.cursor.close()
        return result

        

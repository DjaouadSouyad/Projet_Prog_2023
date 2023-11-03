import sqlite3
from sqlite3 import Error

class Gestion_BD:
    
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """ Crée une connexion à une base de données SQLite """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
        return None

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()

    def ajouter_contact(self, last_name,first_name,phone_number, mail_adress):
        """
        Create a contact into the contact table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO contact(last_name,first_name,phone_number, mail_adress)
                VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (last_name,first_name,phone_number, mail_adress) )
        self.conn.commit()
        return cur.lastrowid
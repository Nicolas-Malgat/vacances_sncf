import mysql.connector

import os
from sql_constant import DROP_TABLE, INSERT_STATEMENT, CREATE_TABLE, PREFECTURE
from dotenv import load_dotenv

load_dotenv(verbose=True)

server = os.getenv("MYSQL_HOST")
username = os.getenv("MYSQL_ROOT")
password = os.getenv("MYSQL_ROOT_PASSWORD")
database = r"projet_vacances"

config = {
  'user': username,
  'password': password,
  'host': server,
  'database': database
}


class Connection:
    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

        print('Successfully connected to '+database+' database.')

    def __exit__(self):
        self.cnx.close()

    def insert_data(self, table, rows):
        """ Insère des données dans la table définie en paramètre

        format de rows:
        data = [
            ('Jane', date(2005, 2, 12)),
            ('Joe', date(2006, 5, 23)),
            ('John', date(2010, 10, 3)),
        ]

        Args:
            table (string): constant de table
            rows (list of tuple): list contenant des tuples
        """
        self.cursor.executemany(INSERT_STATEMENT[table], rows)
        self.cnx.commit()

    def create_table(self, table):
        """ Permet de créer une table à partir du nom donné en paramètre

        Args:
            table (string): nom de la table
        """
        self.cursor.execute(DROP_TABLE.format(table))
        self.cursor.execute(CREATE_TABLE[table])
        print('Created database.')


if __name__ == "__main__":
    connect = Connection()
    connect.create_table(PREFECTURE)

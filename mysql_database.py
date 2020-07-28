import mysql.connector

import os
import csv
from sql_constant import DROP_TABLE, INSERT_STATEMENT, CREATE_TABLE, table, SELECT_STATEMENT
from dotenv import load_dotenv
import classe

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


class connection:
    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

        print('Successfully connected to '+database+' database.')

    def __exit__(self):
        self.cnx.close()

    def commit(self):
        self.cnx.commit()

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

    def create_table(self, table):
        """ Permet de créer une table à partir du nom donné en paramètre

        Args:
            table (string): nom de la table
        """
        self.cursor.execute(DROP_TABLE.format(table))
        self.cursor.execute(CREATE_TABLE[table])
        print('Created database.')

    def get_data(self, table):
        self.cursor.execute(SELECT_STATEMENT[table])
        return self.cursor.fetchall()


if __name__ == "__main__":
    connect = connection()

    connect.create_table(table.prefecture.value)
    data = []

    with open('sql/cities.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(
                (row['region_admin_code'], row['numero_dpt'], row['nom_dpt'], row['prefecture'], row['nom_region'], row['longitude'], row['latitude'])
            )
    connect.insert_data(table.prefecture.value, data)

    # # READ
    # liste_prefecture = classe.prefecture.from_tuple(connect.get_data(table.prefecture.value))
    # for prefecture in liste_prefecture:
    #     print(prefecture.nom, '\t\t', prefecture.departement_code, '\t', prefecture.departement_nom)
    connect.commit()

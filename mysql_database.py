import mysql.connector
from mysql.connector.errors import IntegrityError

import os
import csv
from sql_constant import DROP_TABLE, INSERT_STATEMENT, CREATE_TABLE, table, SELECT_STATEMENT, LOAD_STATEMENT
from dotenv import load_dotenv
from sql_constant import table

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

    def insert_data(self, nom_table, rows):
        """ Insère des données dans la table définie en paramètre

        format de rows:
        data = [
            ('Jane', date(2005, 2, 12)),
            ('Joe', date(2006, 5, 23)),
            ('John', date(2010, 10, 3)),
        ]

        Args:
            nom_table (string): membre de l'enum table dans sql_constant
            rows (list of tuple): list contenant des tuples
        """
        try:
            self.cursor.executemany(INSERT_STATEMENT[nom_table], rows)
        except IntegrityError as e:

            # contrainte d'intégrités acceptables de violer
            if nom_table != table.gare.value and nom_table != table.route.value and nom_table != table.route_gare.value:
                raise Exception("Une contrainte d'intégrité non prévu a été levée", e)
            # else:
                # print("Contrainte d'intégrité non fatale dans ", nom_table, '\n', rows)

    def delete_table(self, table):
        result = self.cursor.execute(DROP_TABLE.format(table))
        print('Table ', table, ' deleted.')
        return result

    def create_table(self, table):
        """ Permet de créer une table à partir du nom donné en paramètre

        Args:
            table (string): nom de la table
        """
        self.cursor.execute(CREATE_TABLE[table])
        print('Table ', table, ' created.')

    def get_data(self, table):
        self.cursor.execute(SELECT_STATEMENT[table])
        return self.cursor.fetchall()

    def load_data(self, table, id):
        self.cursor.execute(LOAD_STATEMENT[table].format(id))
        return self.cursor.fetchall()

    def reset_tables(self):

        # contiennent des foreign keys
        self.delete_table(table.route_gare.value)
        self.delete_table(table.route_journey.value)
        self.delete_table(table.journey.value)

        self.delete_table(table.route.value)
        self.delete_table(table.gare.value)
        self.delete_table(table.voyage.value)

        print('\n')

        self.create_table(table.voyage.value)
        self.create_table(table.journey.value)
        self.create_table(table.route.value)
        self.create_table(table.gare.value)
        self.create_table(table.route_gare.value)
        self.create_table(table.route_journey.value)

        self.commit()

if __name__ == "__main__":
    connect = connection()

    # DROP TABLES
    connect.reset_tables()

    # # INSERT PREFECTURE
    # connect.create_table(table.prefecture.value)
    # data = []

    # with open('sql/cities.csv', newline='', encoding='utf-8') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         data.append(
    #             (row['region_admin_code'], row['numero_dpt'], row['nom_dpt'], row['prefecture'], row['nom_region'], row['longitude'], row['latitude'])
    #         )
    # connect.insert_data(table.prefecture.value, data)

    # # READ
    # liste_prefecture = classe.prefecture.from_tuple(connect.get_data(table.prefecture.value))
    # for prefecture in liste_prefecture:
    #     print(prefecture.nom, '\t\t', prefecture.departement_code, '\t', prefecture.departement_nom)
    # connect.commit()

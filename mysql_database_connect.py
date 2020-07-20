import mysql.connector

import os
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
  'database': database,
  'raise_on_warnings': True
}

class Connection:
    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

        print('Successfully connected to '+database+' database.')

    def create_database(self, sql_path):
        try:
            with open('sql/requestsTable.sql', 'r', encoding='utf-8') as sql_file:
                sql_content = sql_file.read()
                self.cursor.execute(sql_content, multi=True)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        print('Created database.')

if __name__ == "__main__":
    connect = Connection()
    connect.create_database('sql/requestsTable.sql')
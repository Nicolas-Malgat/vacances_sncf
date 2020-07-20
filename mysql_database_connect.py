import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

server = os.getenv("MYSQL_HOST")
username = os.getenv("MYSQL_ROOT")
password = os.getenv("MYSQL_ROOT_PASSWORD")

config = {
  'user': username,
  'password': password,
  'host': server,
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

print("ça fonctionne !")

cnx.close()
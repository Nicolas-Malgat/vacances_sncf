import csv
from mysql_database_connect import Connection
from sql_constant import PREFECTURE

if __name__ == "__main__":
    # encoding="utf-8" sert réélement à quelque chose, incroyable
    with open('sql/cities.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(
                (row['region_admin_code'], row['numero_dpt'], row['nom_dpt'], row['ville'], row['nom_region'], row['longitude'], row['latitude'])
            )

    connect = Connection()
    connect.insert_data(PREFECTURE, data)
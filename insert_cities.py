import csv
from mysql_database_connect import Connection
from sql_constant import table

if __name__ == "__main__":
    data = []

    with open('sql/cities.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(
                (row['region_admin_code'], row['numero_dpt'], row['nom_dpt'], row['prefecture'], row['nom_region'], row['longitude'], row['latitude'])
            )

    connect = Connection()
    connect.insert_data(table.prefecture.value, data)

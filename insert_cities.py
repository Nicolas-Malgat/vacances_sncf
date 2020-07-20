import csv
# encoding="utf-8" sert réélement à quelque chose, incroyable
with open('sql/cities.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['numero_dpt'], row['nom_dpt'], row['ville'], row['nom_region'], row['longitude'], row['latitude'], row['region_admin_code'])

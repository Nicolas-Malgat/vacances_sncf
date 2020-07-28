from sql_constant import table


class gare:

    def __init__(self, nom, id_gare, region_admin, longitude, latitude):
        self.nom = nom
        self.id_gare = id_gare
        self.region_admin = region_admin
        self.longitude = longitude
        self.latitude = latitude

    def enregistrer(self, connection):

        data = [(
            self.id_gare,
            self.region_admin,
            self.nom,
            self.longitude,
            self.latitude
        )]

        connection.insert_data(table.gare, data)

    @classmethod
    def from_json(cls, json):
        list_gare = []

        for gare in json['stop_areas']:
            if len(gare) == 8:
                list_gare.append(cls(
                    gare['label'],
                    gare['id'],
                    gare['administrative_regions'][0]['id'],
                    gare['coord']['lon'],
                    gare['coord']['lat']
                ))
        return list_gare

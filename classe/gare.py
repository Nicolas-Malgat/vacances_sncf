class gare:
    def __init__(self, nom, id_gare, region_admin, longitude, latitude):
        self.nom = nom
        self.id_gare = id_gare
        self.fk_region_admin = region_admin
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_json(cls, json):
        list_gare = []

        for gare in json['stop_points']:
            if len(gare) == 9:
                
                gares = cls(
                    gare['name'],
                    gare['id'],
                    gare['administrative_regions'][0]['id'],
                    gare['coord']['lon'],
                    gare['coord']['lat']
                )
                for gare in 
        return list_gare

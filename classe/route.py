from sql_constant import table


class route:

    def __init__(self, id, start_station_id, stop_station_id, duration, pollution):
        self.id = id
        self.start_station_id = start_station_id
        self.stop_station_id = stop_station_id
        self.duration = duration
        self.pollution = pollution
        self.depart = None
        self.arrivee = None

    def set_gare(self, liste_gare):
        for une_gare in liste_gare:
            if self.start_station_id == une_gare.id_gare:
                self.depart = une_gare
            if self.stop_station_id == une_gare.id_gare:
                self.arrivee = une_gare

        # CAS D'ERREUR
        if self.depart is None or self.arrivee is None:
            print('La route ', self.id, ' n\'a pas trouvé de gare avec les id\ndepart: ', self.start_station_id, ' ', self.depart, '\narrivee: ', self.stop_station_id, ' ', self.arrivee)

    def enregistrer(self, connection):

        data = []
        data.append((
            self.id,
            self.depart.id_gare,
            self.arrivee.id_gare
        ))

        connection.insert_data(table.route.value, data)

        # Insertion des gares suivi de l'insertion de la relation route_gare
        self.depart.enregistrer(connection)
        self.arrivee.enregistrer(connection)

        data_relation = [
            (self.id, self.depart.id_gare),
            (self.id, self.arrivee.id_gare),
        ]

        connection.insert_data(table.route_gare.value, data_relation)

    @classmethod
    def from_json(cls, json):
        list_route = []

        for route in json:
            # Vérification 
            
            if route['type'] != 'public_transport':
                if route['type'] != 'walking' and route['type'] != 'transfer' and route['type'] != 'crow_fly' and route['type'] != 'waiting':
                    print("type de transport disruptif: ", route['type'])
                continue

            id = None
            for link in route['links']:
                if link['type'] == 'route':
                    id = link['id']
                    break
            if not id:
                raise Exception('Aucun id trouvé pour la route ', route)

            list_route.append(cls(
                id,
                route['from']['stop_point']['stop_area']['id'],
                route['to']['stop_point']['stop_area']['id'],
                route['duration'],
                route['co2_emission']['value']
            ))
        return list_route

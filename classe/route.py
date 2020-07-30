from sql_constant import table
from classe.gare import gare


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

    def get_coordonnees(self, dictionnaire):
        
        dictionnaire.append(
            {'lat': float(self.depart.latitude), 'lng': float(self.depart.longitude)}
        )

    @classmethod
    def load(cls, connection, id_journey, liste_gare):

        tuple_route = connection.load_data(table.route.value, id_journey)

        liste_route = cls.from_tuple(tuple_route, liste_gare)

        for route in liste_route:
            route.set_gare(liste_gare)

        return liste_route

    @classmethod
    def from_tuple(cls, tuple, liste_gare):
        liste_route = []

        for element in tuple:
            liste_route.append(cls(
                element[0],
                element[1],
                element[2],
                None,
                None
            ))

        return liste_route

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

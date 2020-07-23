from classe.gare import gare
import sys


class route:
    def __init__(self, id, start_station_id, stop_station_id, duration, pollution):
        self.id = id
        self.start_station_id = start_station_id
        self.stop_station_id = stop_station_id
        self.duration = duration
        self.pollution = pollution
        self.depart = None
        self.arrivee = None

    @classmethod
    def from_json(cls, json):
        list_route = []

        for route in json:
            # Vérification de l'existence du stop_point de départ
            try:
                route['from']['stop_point']
                route['to']['stop_point']
            except KeyError:
                continue

            list_route.append(cls(
                route['id'],
                route['from']['stop_point']['stop_area']['id'],
                route['to']['stop_point']['stop_area']['id'],
                route['duration'],
                route['co2_emission']['value']
            ))
        return list_route

    def set_gare(self, liste_gare):
        for une_gare in liste_gare:
            if self.start_station_id == une_gare.id_gare:
                self.depart = une_gare
            elif self.stop_station_id == une_gare.id_gare:
                self.arrivee = une_gare
        if self.depart is None or self.arrivee is None:
            print('La route ', self.id, ' n\'a pas trouvé de gare avec les id\ndepart: ', self.start_station_id, '\narrivee: ', self.stop_station_id)

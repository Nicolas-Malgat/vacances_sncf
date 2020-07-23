from classe.route import route
import sys


class journey:
    def __init__(self, departure_date_time, arrival_date_time, requested_date_time, pollution, duration, list_route):
        self.arrival_date_time = arrival_date_time
        self.departure_date_time = departure_date_time
        self.requested_date_time = requested_date_time
        self.pollution = pollution
        self.duration = duration
        self.liste_route = list_route

    def set_gare(self, liste_gare):
        liste = self.liste_route

        for une_route in liste:
            une_route.set_gare(liste_gare)

        self.depart = liste[0].depart
        self.arrivee = liste[len(liste) - 1].arrivee

    @classmethod
    def from_json(cls, json):
        list_journey = []

        for a_journey in json['journeys']:
            list_route = route.from_json(a_journey['sections'])

            list_journey.append(cls(
                a_journey['departure_date_time'],
                a_journey['arrival_date_time'],
                a_journey['requested_date_time'],
                a_journey['co2_emission']['value'],
                a_journey['duration'],
                list_route
            ))

        return list_journey

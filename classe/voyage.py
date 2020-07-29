import uuid
from classe.gare import gare
from classe.journey import journey
from sql_constant import table
import json


class voyage:

    def __init__(self, id, liste_journey, requested_date_time, depart_gare, departure_date_time, arrivee_gare, arrival_date_time, duration, pollution):
        self.id = id
        self.liste_journey = liste_journey
        self.requested_date_time = requested_date_time
        self.depart = depart_gare
        self.departure_date_time = departure_date_time
        self.arrivee = arrivee_gare
        self.arrival_date_time = arrival_date_time
        self.duration = duration
        self.pollution = pollution

    @classmethod
    def from_list_journey(cls, liste_journey):
        pollution = 0
        duration = 0
        for journey in liste_journey:
            duration += journey.duration
            pollution += journey.pollution

        return cls(
            str(uuid.uuid4().int),
            liste_journey,
            liste_journey[0].requested_date_time,
            liste_journey[0].depart,
            liste_journey[0].departure_date_time,
            liste_journey[len(liste_journey) - 1].arrivee,
            liste_journey[0].arrival_date_time,
            duration,
            pollution
        )

    def enregistrer(self, connection):

        data = []
        data.append((
            self.id,
            self.requested_date_time,
            self.depart.id_gare,
            self.arrivee.id_gare,
            self.departure_date_time,
            self.arrival_date_time,
            self.duration,
            self.pollution
        ))

        connection.insert_data(table.voyage.value, data)

        ordre = 1
        for journey in self.liste_journey:
            journey.enregistrer(connection, self.id, ordre)
            ordre += 1

        connection.commit()

    def get_coordonnees(self):
        dict_coord = []
        
        for journey in self.liste_journey:
            journey.get_coordonnees(dict_coord)

        return json.dumps(dict_coord)


    @classmethod
    def load(cls, connection, id_voyage, liste_gare):

        if not id_voyage:
            id_voyage = connection.get_data(table.voyage.value)[0][0]

        tuple_voyage = connection.load_data(table.voyage.value, id_voyage)

        liste_journey = journey.load(connection, id_voyage, liste_gare)

        return cls.from_tuple(tuple_voyage, liste_gare, liste_journey)

    @classmethod
    def from_tuple(cls, tuple, liste_gare, liste_journey):
        liste_voyage = []

        for element in tuple:
            liste_voyage.append(cls(
                element[0],
                liste_journey,
                element[1],
                gare.find_by_id(liste_gare, element[2]),
                element[4],
                gare.find_by_id(liste_gare, element[3]),
                element[5],
                element[6],
                element[7]
            ))

        return liste_voyage
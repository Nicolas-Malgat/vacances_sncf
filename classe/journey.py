from classe.route import route
import uuid
from sql_constant import table


class journey:

    def __init__(self, id, departure_date_time, arrival_date_time, requested_date_time, pollution, duration, list_route):
        self.id = id
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

    def enregistrer(self, connection, voyage_id, ordre1):

        data = []
        data.append((
            self.id,
            self.duration,
            self.departure_date_time,
            self.arrival_date_time,
            self.requested_date_time,
            self.depart.id_gare,
            self.arrivee.id_gare,
            self.pollution,
            voyage_id,
            ordre1
        ))

        connection.insert_data(table.journey.value, data)

        # Insertion de route suivi de l'insertion de la relation route_journey
        data_relation = []
        ordre2 = 1
        for une_route in self.liste_route:
            une_route.enregistrer(connection)

            data_relation.append((
                une_route.id,
                self.id,
                ordre2
            ))
            ordre2 += 1

        connection.insert_data(table.route_journey.value, data_relation)

    def get_coordonnees(self, dictionnaire):

        for une_route in self.liste_route:
            une_route.get_coordonnees(dictionnaire)

        dictionnaire.append(
            {'lat': float(self.arrivee.latitude), 'lng': float(self.arrivee.longitude)}
        )

    @classmethod
    def from_json(cls, json):
        list_journey = []

        for a_journey in json['journeys']:
            list_route = route.from_json(a_journey['sections'])

            list_journey.append(cls(
                str(uuid.uuid4().int),
                a_journey['departure_date_time'],
                a_journey['arrival_date_time'],
                a_journey['requested_date_time'],
                a_journey['co2_emission']['value'],
                a_journey['duration'],
                list_route
            ))

        return list_journey

    @classmethod
    def load(cls, connection, id_voyage, liste_gare):

        list_tuple_journey = connection.load_data(table.journey.value, id_voyage)

        liste_journey = []
        for tuple_journey in list_tuple_journey:
            liste_route = route.load(connection, tuple_journey[0], liste_gare)
            liste_journey.append(cls.from_tuple(tuple_journey, liste_route))

        for journey in liste_journey:
            journey.set_gare(liste_gare)

        return liste_journey

    @classmethod
    def from_tuple(cls, element, liste_route):

        return (cls(
            element[0],
            element[2],
            element[3],
            element[4],
            element[7],
            element[1],
            liste_route
        ))

    @staticmethod
    def plus_vert_chemin(list_journey):
        """ Renvoie le chemin le moins polluant parmis la liste

        Args:
            list_journey (liste de journey): liste contenant des journey

        Returns:
            journey: objet de type journey
        """
        journey_vert = list_journey[0]

        for journey in list_journey:
            if journey.pollution < journey_vert.pollution:
                journey_vert = journey

        return journey_vert

    @staticmethod
    def plus_court_chemin(list_journey):
        """ Renvoie le chemin le plus court parmis la liste

        Args:
            list_journey (list of journey): liste contenant des journey

        Returns:
            journey: objet de type journey
        """

        journey_court = list_journey[0]

        for journey in list_journey:
            # s'il y a des soucis avec les dates, comparer avec dateutil.parser.isoparse()
            if journey.arrival_date_time < journey_court.arrival_date_time:
                journey_court = journey

        return journey_court

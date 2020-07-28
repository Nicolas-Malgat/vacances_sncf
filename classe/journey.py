from classe.route import route
import uuid


class journey:

    def __init__(self, departure_date_time, arrival_date_time, requested_date_time, pollution, duration, list_route):
        id = uuid.uuid4()
        self.id = id.int
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

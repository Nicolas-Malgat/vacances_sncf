import uuid


class voyage:

    def __init__(self, requested_date_time, liste_journey, depart_gare, departure_date_time, arrivee_gare, arrival_date_time, duration, pollution):
        id = uuid.uuid4()
        self.id = id.int
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
            liste_journey,
            liste_journey[0].requested_date_time,
            liste_journey[0].depart,
            liste_journey[0].departure_date_time,
            liste_journey[len(liste_journey - 1)].arrivee,
            liste_journey[0].arrival_date_time,
            duration,
            pollution
        )

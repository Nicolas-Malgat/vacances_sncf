class route:
    def __init__(self, id, start_station_id, stop_station_id, duration, co2):
        self.id = id
        self.start_station_id = start_station_id
        self.stop_station_id = stop_station_id
        self.duration = duration
        self.co2 = co2

    @classmethod
    def from_journey(cls, journey):
        lst_routes = []

        for route in journey['sections']:
            oneRoute = cls(
                route['id'],
                route['from']['stop_point']['id'],
                route['to']['stop_point']['id'],
                route['duration'],
                route['co2_emission']['value']
            )
            lst_routes.append(oneRoute)
        return lst_routes

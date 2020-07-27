from sncf_api import plus_court_chemin, get_journeys, plus_vert_chemin, get_gares
from mysql_database import connection
from sql_constant import PREFECTURE

import classe
from classe.prefecture import prefecture

from enum import Enum
import pprint


class type_voyage(Enum):
    ecologique = 0
    court = 1


class itineraire:

    def __init__(self, connection):
        self.conn = connection
        self.liste_prefecture = prefecture.from_tuple(self.conn.get_data(PREFECTURE))

        self.liste_voyage = []
        self.liste_des_gares = get_gares()

    def calcul_voyage(self, type_itineraire, prefecture_depart_id, date_de_depart):
        liste_prefecture = self.liste_prefecture

        # Initialisation des variables
        prefecture_depart = classe.prefecture.find_by_id(prefecture_depart_id)
        liste_journey_finale = []

        while liste_prefecture:

            liste_journey_temp = []
            min_journey = None

            # recuperation des journeys
            for pref in liste_prefecture:
                liste_journey_temp.append(
                    get_journeys(prefecture_depart, pref, date_de_depart)
                )

            # attribution des gares pour chaque journey et route
            for journey in liste_journey_temp:
                journey.set_gare(self.liste_des_gares)

            # CHOIX DU TYPE D'ITINERAIRE
            if type_itineraire == type_voyage.ecologique:
                min_journey = plus_vert_chemin(liste_journey_temp)
            if type_itineraire == type_voyage.court:
                min_journey = plus_court_chemin(liste_journey_temp)

            # preparation des varaible avant la prochaine iteration
            liste_journey_finale.append(min_journey)
            prefecture_depart = prefecture.find_by_gare(liste_prefecture, min_journey.arrivee)
            date_de_depart = min_journey.arrival_date_time

        return liste_journey_finale


if __name__ == '__main__':
    connect = connection()
    itineraire = itineraire(connect)
    liste_journey = itineraire.calcul_voyage(type_voyage.court, "admin:fr:59350", '20200727T080000')
    with open('liste_journey.txt', 'w', 'utf-8') as file:
        file.write(pprint.pprint(liste_journey))
    print('programme terminé !')

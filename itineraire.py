from sncf_api import sncf_api
from mysql_database import connection
from sql_constant import table
from classe.voyage import voyage

from classe.prefecture import prefecture

from enum import Enum


class type_voyage(Enum):
    ecologique = 0
    court = 1


class itineraire:

    def __init__(self, connection):
        self.conn = connection
        self.liste_prefecture = prefecture.load(self.conn)
        self.liste_prefecture = prefecture.from_tuple(self.conn.get_data(table.prefecture.value))

        self.liste_voyage = []
        self.liste_des_gares = sncf_api.get_gares()

    def calcul_voyage(self, type_itineraire, prefecture_depart_id, date_de_depart):

        liste_prefecture = self.liste_prefecture

        # Initialisation des variables
        prefecture_depart = prefecture.find_by_id(liste_prefecture, prefecture_depart_id)
        liste_prefecture.remove(prefecture_depart)
        liste_journey_finale = []

        while liste_prefecture:

            liste_journey_temp = []
            min_journey = None

            # recuperation des journeys
            for pref in liste_prefecture:
                journeys = sncf_api.get_journeys(prefecture_depart.region_admin, pref.region_admin, date_de_depart)

                if journeys:
                    for journey in journeys:
                        print("|", end='')
                        liste_journey_temp.append(journey)

            # Au cas où aucun trajet ne permet de compléter les visites des préfectures
            if not liste_journey_temp:
                prefectures = map(lambda x: x.nom, liste_prefecture)
                print(
                    'Auncune journey pour poursuivre l\'itinéraire, préfectures non visitées:\n',
                    '\n'.join(prefectures)
                )
                return liste_journey_finale

            # attribution des gares pour chaque journey et route
            for journey in liste_journey_temp:
                journey.set_gare(self.liste_des_gares)

            # CHOIX DU TYPE D'ITINERAIRE
            if type_itineraire == type_voyage.ecologique:
                min_journey = journey.plus_vert_chemin(liste_journey_temp)
            if type_itineraire == type_voyage.court:
                min_journey = journey.plus_court_chemin(liste_journey_temp)

            # preparation des varaible avant la prochaine iteration
            print('\nNouvelle iteration:\n')
            liste_journey_finale.append(min_journey)
            prefecture_depart = prefecture.find_by_gare(liste_prefecture, min_journey.arrivee)
            liste_prefecture.remove(prefecture_depart)
            date_de_depart = min_journey.arrival_date_time

        return liste_journey_finale

    def load_voyage(self):
        voyage1 = voyage.load(self.conn, None, self.liste_des_gares)[0]
        return voyage1


if __name__ == '__main__':
    connect = connection()
    itineraire = itineraire(connect)

    # construction d'un voyage
    liste_journey = itineraire.calcul_voyage(type_voyage.court, "admin:fr:59350", '20200727T080000')
    voyage1 = voyage.from_list_journey(liste_journey)
    voyage1.enregistrer(connect)

    print('programme terminé !')

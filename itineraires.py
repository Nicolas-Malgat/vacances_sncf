from sncf_api import plus_court_chemin, get_journeys, plus_vert_chemin, get_gares
import mysql_database
from sql_constant import PREFECTURE
import classe


def itineraire():
    conn = mysql_database.connection
    liste_prefecture = classe.prefecture.from_tuple(conn.get_data(PREFECTURE))
    liste_des_gares = get_gares()

    # Initialisation
    for pref in liste_prefecture:
        if pref.region_admin == 'admin:fr:63113':
            liste_prefecture.remove(pref)
            prefecture_depart = pref
    date_de_depart = '20200727T080000'
    liste_journey_finale = []

    while liste_prefecture:

        liste_journey_temp = []
        min_journey = None

        for prefecture in liste_prefecture:
            liste_journey_temp.append(get_journeys(prefecture_depart, prefecture, date_de_depart))

        min_journey = plus_court_chemin(liste_journey_temp)

        liste_journey_finale.append(min_journey)
        prefecture_depart = prefecture.find_by_gare(liste_prefecture, min_journey.arrivee)
        date_de_depart = min_journey.arrival_date_time


    print(len(liste_des_gares))
    i = 0
    # for ma_gare in liste_des_gares:
    #     print(ma_gare.nom + ' ' + ma_gare.fk_region_admin)
    #     i += 1
    #     if i == 20:
    #         break

    liste_des_journeys = sncf_api.get_journeys(
        'admin:fr:4112', 'admin:fr:93055', '20200727T080000')

    for a_journey in liste_des_journeys:
        a_journey.set_gare(liste_des_gares)

    for a_journey in liste_des_journeys:
        print(a_journey.depart.nom, '\t',
                a_journey.arrivee.nom, '\t', a_journey.duration)
        i += 1
        if i == 20:
            break

    journey.plus_court_chemin(liste_des_journeys)

    

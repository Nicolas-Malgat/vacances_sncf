import requests
import os
from classe.gare import gare
from classe.journey import journey


class sncf_api:
    __token_auth = os.getenv("TOKEN_AUTH")
    __path = r"https://api.sncf.com/v1/coverage/sncf"
    request_count = 0

    # STATIC
    @staticmethod
    def get_next_page(response):
        try:
            links = response.json()['links']
            for link in links:
                if link['type'] == 'next':
                    return link['href']
            return False
        except Exception:
            print('get_next_page a levé une exception !\n', response.json())
            return False

    @classmethod
    def make_request(cls, link):
        cls.request_count += 1
        if cls.request_count >= 4900:
            print('Limite de requêtes atteinte par ce processus')
        try:
            # print(link)
            return requests.get(link, auth=(cls.__token_auth, ''))
        except Exception as e:
            print("Erreur lors de la requête avec le lien: " + link)
            print(e.args)

    @classmethod
    def get_gares(cls):
        method_path = r"/stop_areas?count=1000"

        list_response = []
        next_page = cls.__path + method_path
        # toutes les requêtes
        while next_page:
            response = cls.make_request(next_page)
            list_response.append(response)
            next_page = cls.get_next_page(response)

        if list_response[0].status_code != 200:
            raise Exception("Aucune gare n'a pu être collectée, erreur fatale\n", list_response)

        list_gare_total = []
        # tous les objets
        for response in list_response:
            for list_gare in gare.from_json(response.json()):
                list_gare_total.append(list_gare)

        return list_gare_total

    @classmethod
    def get_journeys(cls, depart, arrivee, date):
        """ Renvoie une liste d'objets journey

        Args:
            depart (stirng): identifiant de type admin:fr:xxxxx
            arrivee (string): identifiant de tyype admin:fr:xxxxx
            date (string): date sous le format AAAAMMJJTHHMMSS

        Returns:
            liste de journey: tous les trajets possibles vers l'arrivée
        """
        method_path = '/journeys?from={}&to={}&datetime={}'
        method_path = method_path.format(depart, arrivee, date)
        path = cls.__path + method_path

        response = sncf_api.make_request(path)

        try:
            return journey.from_json(response.json())
        except KeyError:
            # print("\nErreur, aucun trajet pour la recherche\n", path)
            print("O", end='')
            return None
        except AttributeError:
            print('\nErreur, la requête suivante n\'a rien renvoyé', path)
            return None


if __name__ == "__main__":
    liste_des_gares = sncf_api.get_gares()

    print(len(liste_des_gares))
    i = 0
    # for ma_gare in liste_des_gares:
    #     print(ma_gare.nom + ' ' + ma_gare.fk_region_admin)
    #     i += 1
    #     if i == 20:
    #         break

    liste_des_journeys = sncf_api.get_journeys('admin:fr:4112', 'admin:fr:93055', '20200727T080000')

    for a_journey in liste_des_journeys:
        a_journey.set_gare(liste_des_gares)

    for a_journey in liste_des_journeys:
        print(a_journey.depart.nom, '\t', a_journey.arrivee.nom, '\t', a_journey.duration)
        i += 1
        if i == 20:
            break

    journey.plus_court_chemin(liste_des_journeys)

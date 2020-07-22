import requests
import os
from classe.gare import gare


class sncf_api:
    __token_auth = os.getenv("TOKEN_AUTH")
    __path = r"https://api.sncf.com/v1/coverage/sncf"

    # STATIC
    @staticmethod
    def get_next_page(response):
        try:
            link = response.json()['links'][9]
            if link['type'] == 'next':
                return link['href']
            return False
        except Exception:
            os.error('get_next_page a levé une exception !\n' + response.json()['links'])
            return False

    @classmethod
    def make_request(cls, link):
        try:
            print(link)
            return requests.get(link, auth=(cls.__token_auth, ''))
        except Exception as e:
            print("Erreur lors de la requête avec le lien: " + link)
            print(e.args)

    @classmethod
    def get_gares(cls):
        method_path = r"/stop_areas?count=1000"

        list_response = []
        next_page = cls.__path + method_path
        while next_page:
            response = cls.make_request(next_page)
            list_response.append(response)
            next_page = cls.get_next_page(response)

        list_gare_total = []
        for response in list_response:
            for list_gare in gare.from_json(response.json()):
                list_gare_total.append(list_gare)

        return list_gare_total


if __name__ == "__main__":
    liste_des_gares = sncf_api.get_gares()

    print(len(liste_des_gares))
    print('gares récoltées:')
    i = 0
    for ma_gare in liste_des_gares:
        print(ma_gare.nom + ' ' + ma_gare.fk_region_admin)
        i += 1
        if i == 20:
            break

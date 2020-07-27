class prefecture:

    def __init__(self, region_admin, departement_code, departement_nom, nom, region_nom, longitude, latitude):
        self.region_admin = region_admin
        self.departement_code = departement_code
        self.departement_nom = departement_nom
        self.nom = nom
        self.region_nom = region_nom
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_tuple(cls, tuple):
        liste_prefecture = []

        for pref in tuple:
            liste_prefecture.append(cls(
                pref[0],
                pref[1],
                pref[2],
                pref[3],
                pref[4],
                pref[5],
                pref[6],
            ))

        return liste_prefecture

    @staticmethod
    def find_by_gare(liste_prefecture, gare_arrivee):
        for prefecture in liste_prefecture:
            if prefecture.region_admin == gare_arrivee.region_admin:
                return prefecture

        print('ERREUR la région administrative: ', gare_arrivee.region_admin, ' n\'a pas été trouvée dans la liste des préfectures\n', liste_prefecture)
        return False

    @staticmethod
    def find_by_id(liste_prefecture, id):
        for pref in liste_prefecture:
            if pref.region_admin == id:
                return pref
        raise Exception("l'id ", id, " n'a pas été trouvé lors de la recherche prefecture.find_by_id")

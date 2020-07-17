import requests
import pprint
import json
import os
from dotenv import load_dotenv

#token_auth='votre token ici, recu dans votre boite mail'
load_dotenv(verbose=True)
token_auth = os.getenv("TOKEN_AUTH")



url_avec_params = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'

try:
    r = requests.get(url_avec_params,auth=(token_auth,''))
    if r.status_code != 200:
        raise Exception("La requête possède un code différent de 200: %s" % r.status_code)
    print('Chargement des stop areas réussi !')
except Exception as e:
    print(e)
    exit

with open('stop_areas.json',"w") as file:
    file.write(json.dumps(r.json(), indent=2))
print('Ecriture de stop_areas.json terminée')

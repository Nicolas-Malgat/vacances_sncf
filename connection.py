import requests
import pprint

#token_auth='votre token ici, recu dans votre boite mail'
token_auth = 'fed8709b-28c3-4300-9a06-90dea3c52e1c'

url_avec_params = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'

r=requests.get(url_avec_params,auth=(token_auth,''))

pprint.pprint(r.json())
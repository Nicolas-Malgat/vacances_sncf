import requests
import pprint
import json
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
token_auth = os.getenv("TOKEN_AUTH")

def get_json(url):
    """ Get the JSON content from an URL
    """
    try:
        json_element = requests.get(url,auth=(token_auth,''))
        if json_element.status_code != 200:
            raise Exception("La requête possède un code réponse différent de 200: %s" % json_element.status_code)
        else:
            print('Chargement réussi.')
    except Exception as e:
        print(e)
        exit

    json_dict = json.loads(json_element.text)

    return json_dict

def get_journeys(json):
    """Get the journeys from a json element.

    Args:
        json ([dict])

    Returns:
        [dict]: [0, 1, ...]
    """
    journeys=json['journeys']
    return journeys

def get_journey_infos(journey):
    """Get informations from a journey in a collection of journeys. 

    Args:
        journeys (dict): collection of journeys
        number (int): number of the journey like '0', '1'...

    Returns:
        [dict]:[arrival_date_time, departure_date_time, requested_date_time, duration, co2_emission, sections, calendars]
    """
    co2_emission=journey['co2_emission']
    journey_infos={}
    journey_infos['arrival_date_time']=journey['arrival_date_time']
    journey_infos['departure_date_time']=journey['departure_date_time']
    journey_infos['requested_date_time']=journey['requested_date_time']
    journey_infos['duration']=journey['duration']
    journey_infos['co2_emission']=co2_emission['value']
    journey_infos['sections']=journey['sections']
    journey_infos['calendars']=journey['calendars']
    return journey_infos

def get_routes(journey):
    """Returns the routes and the number of routes from a journey.

    Args:
        journey (dict)

    Returns:
        [dict]: [0, 1, 2...]
    """
    routes=journey['sections']
    return routes

def get_route_infos(journey, route):
    """Returns informations about a route.

    Args:
        journey (dict)
        route (int): number of the route like '0', '1'...

    Returns:
        [dict]: [id, arrival_date_time, departure_date_time, mode, type, duration, stop_date_time, from, to]
    """
    sections=get_journey_infos(journey)['sections']
    route_infos={}
    route_infos=sections[route]
    return route_infos


def get_stop_point(journey, route, from_to):
    """
    Args:
        journey (dict)
        route (int): number of the route like '0', '1'...
        from_to (str): 'from' or 'to'
    
    Returns:
        [dict]: [id, name, lat, lon, stop_area]
    """
    get_from_to=get_route_infos(journey, route)[from_to]
    spoint=get_from_to['stop_point']
    coord=spoint['coord']
    stop_point={}
    stop_point['id']=spoint['id']
    stop_point['name']=spoint['name']
    stop_point['lat']=coord['lat']
    stop_point['lon']=coord['lon']
    stop_point['stop_area']=spoint['stop_area']
    return stop_point

def get_timezone(json):
    """
    Args:
        json ([dict])
    Returns:
        [str]: timezone
    """
    select_context=json['context']
    timezone=select_context['timezone']
    return timezone



# --------------------------------------

if __name__ == '__main__':
    querry='https://api.navitia.io/v1/coverage/sncf/journeys?from=admin%3Afr%3A57463&to=admin%3Afr%3A63113&'

    metz_clermont=get_json(querry)
    mc_journey=get_journeys(metz_clermont)[0]

    # Affiche le CO2 de la journey 0
    co2=get_journey_infos(mc_journey)['co2_emission']
    print('emissions co2 : ', co2)

    # Affiche la timezone.
    timezone=get_timezone(metz_clermont)
    print('timezone du trajet : ', timezone)

    #Affiche la durée de la route 2
    duree=get_route_infos(mc_journey, 2)['duration']
    print('durée de la route 2 : ', duree)

    #Affiche la latitude et la longitude du stop_point de départ de la route 2
    lat=get_stop_point(mc_journey, 2, 'from')['lat']
    lon=get_stop_point(mc_journey, 2, 'from')['lon']
    nom=get_stop_point(mc_journey, 2, 'from')['name']
    print('au point de départ ', nom, ' les coordonnées sont ', lat, '; ', lon)




"""
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
"""
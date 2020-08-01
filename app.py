from bottle import route, run, static_file, template, request
from mysql_database import connection
from itineraire import itineraire
from bottle import response
from json import dumps


@route('/duree')
@route('/')
@route('/index')
def map():
    return template('map')

# AJAX
@route('/get_coordonnees', method='GET')
def get_coordonnees():
    request.GET['type_trajet']
    try:
        connect = connection()
        itineraire1 = itineraire(connect)
        voyage = itineraire1.load_voyage()
        response.content_type = 'application/json'
        ma_reponse = {
            "duree": voyage.duration,
            "pollution": voyage.pollution,
            "coord": voyage.get_coordonnees()
        }
        return dumps(ma_reponse)
    except Exception as e:
        print(e)
        return 'Echec lors de la récupérations des coordonnées'

# RESSOURCES
@route('/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return static_file(filename, root='javascript')

@route('/css/<filename:re:.*\.css>')
def send_stylesheet(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080)

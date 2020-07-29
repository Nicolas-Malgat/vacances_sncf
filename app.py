from bottle import route, run, static_file, template
from mysql_database import connection
from itineraire import itineraire


@route('/')
@route('/index')
def map():
    return template('map')

# AJAX
@route('/get_coordonnees', method='GET')
def get_coordonnees():
    try:
        print('passage dans get_coordonnees')
        connect = connection()
        itineraire1 = itineraire(connect)
        voyage = itineraire1.load_voyage()
        return voyage.get_coordonnees()
    except Exception:
        return 'Echec lors de la récupérations des coordonnées'

# RESSOURCES
@route('/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return static_file(filename, root='javascript')

@route('/css/<filename:re:.*\.css>')
def send_stylesheet(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080)

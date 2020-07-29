from bottle import route, run, static_file, template


@route('/')
@route('/index')
def map():
    return template('map')

@route('/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return static_file(filename, root='javascript')


@route('/css/<filename:re:.*\.css>')
def send_stylesheet(filename):
    return static_file(filename, root='css')

# AJAX
@route('/get_coordonnees', method='GET')
def get_coordonnees():
    try:    
        connect = connection()
        itineraire = itineraire(connect)
        voyage = itineraire.load_voyage()
        return voyage.get_coordonnees()
    except:
        return 'Echec lors de la récupérations des coordonnées'

run(host='localhost', port=8080)

from bottle import route, run, template

@route('/')
@route('/index')
def index():
    return "Hello world !"

run(host='localhost', port=8080)
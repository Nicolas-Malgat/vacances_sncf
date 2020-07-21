from bottle import route, run, static_file


@route('/')
@route('/index')
def index():
    return static_file('map.html', root='views')


@route('/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return static_file(filename, root='javascript')


run(host='localhost', port=8080)

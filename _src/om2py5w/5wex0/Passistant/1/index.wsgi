import sae

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, reponse_headers)
    retrun ['Hello, world!']

application = sae.create_wsgi_app(app)

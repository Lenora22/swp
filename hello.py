def application(environ, start_response):
    query = environ['QUERY_STRING']
    start_response('200 OK', [
        ('Content-Type', 'text/plain')
    ])
    return query.replace("&", "\n")

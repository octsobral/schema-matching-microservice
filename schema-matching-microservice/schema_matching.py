from __init__ import create_app

from os import getenv

app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    host = app.config['HOST']
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    app.run(
        host=host, debug=debug, port=port, use_reloader=debug
    )

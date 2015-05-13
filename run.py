#!/usr/bin/env python
from app import create_app

def run(app=None):
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])


if __name__ == '__main__':
    app = create_app('config')
    run(app)


#!/usr/bin/env python
from app import create_app

app = create_app('config')
app.run( host = '127.0.0.1' )

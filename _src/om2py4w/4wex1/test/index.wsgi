#!/usr/bin/env python
# encoding: utf-8

from bottle import Bottle, run

import sae

app = Bottle()


@app.route('/')
def hello():
    return "Hello, world -bottle"

application = sae.create_wsgi_app(app)

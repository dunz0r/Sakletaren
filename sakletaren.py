#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""
A silly app for finding stuff
"""

# {{{ Libraries and global settings

from flask import Flask

app = Flask(__name__)
# }}}
# {{{ pages
@app.route('/')
def index():
    return "Index page"

@app.route('/size')
def sakSize():
    return 'def size'

@app.route('/colour')
def sakColour():
    return 'def colour'

@app.route('/weight')
def sakColour():
    return 'def weight'


@app.route('/importance')
def sakColour():
    return 'def importance'

@app.route('/importance')
def sakColour():
    return 'def importance'


# }}}
if __name__ == '__main__':
    app.debug = True
    app.run()

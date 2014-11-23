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
class sak():
    @app.route('/')
    def index():
        return "Index page"

    @app.route('/size')
    def Size():
        return 'def size'

    @app.route('/colour')
    def Colour():
        return 'def colour'

    @app.route('/weight')
    def Weight():
        return 'def weight'

    @app.route('/importance')
    def Importance():
        return 'def importance'

    @app.route('/electronic')
    def Electronic():
        return 'def electronic'

    @app.route('/lastseen')
    def LastSeen():
        return 'def sakLastSeen'

    @app.route('/outin')
    def OutIn():
        return 'def outIn'

    @app.route('/material')
    def Material():
        return 'def sakMaterial'

# }}}
if __name__ == '__main__':
    app.debug = True
    app.run()

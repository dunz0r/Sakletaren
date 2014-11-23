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

from flask import Flask, render_template, request
from wtforms import Form, BooleanField, TextField, TextAreaField, SelectField

app = Flask(__name__)
# }}}
# {{{ pages
class pages():
    @app.route('/', methods = ['GET', 'POST'])
    def index():
        form = sizeForm(request.form)
        if request.method == 'POST' and form.validate():
            sak['size'] = form.size
        return render_template('first.html', form=form)

    @app.route('/size')
    def Size():
        return render_template('size.html')

    @app.route('/colour')
    def Colour():
        return render_template('colour.html')

    @app.route('/weight')
    def Weight():
        return render_template('weight.html')

    @app.route('/importance')
    def Importance():
        return render_template('importance.html')

    @app.route('/electronic')
    def Electronic():
        return render_template('electronic.html')

    @app.route('/lastseen')
    def LastSeen():
        return render_template('lastseen.html')

    @app.route('/outin')
    def OutIn():
        return render_template('outin.html')

    @app.route('/material')
    def Material():
        return render_template('material.html')

# }}}
# {{{ forms
class sizeForm(Form):
    sizeChoices = [('1', 'Liten'), ('2','Lagom'), ('3','Ganska stor'), ('3', 'Sjukt stor')]
    size = SelectField(u'Storlek', choices=sizeChoices)
# }}}
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

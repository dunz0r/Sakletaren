#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv2 license.

"""
A silly app for finding stuff
"""
# {{{ Libraries and global settings

from flask import Flask, render_template, request, redirect
from wtforms import Form, BooleanField, TextField, TextAreaField, SelectField

app = Flask(__name__)
sak = {}
# }}}

# {{{ pages
class pages():
    @app.route('/', methods = ['GET', 'POST'])
    def Size():
        form = sizeForm(request.form)
        if request.method == 'POST':
            sak['size'] = form.size
            return redirect('/colour')
        return render_template('first.html', form=form)

    @app.route('/colour', methods = ['GET', 'POST'])
    def Colour():
        form = colourForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.colour
            return redirect('/weight')
        return render_template('colour.html', form=form)

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

class colourForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

class importanceForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

class electronicForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

class lastSeenForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

class outInForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

class materialForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

# }}}
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

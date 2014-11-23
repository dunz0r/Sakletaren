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
        return render_template('template.html', form=form)

    @app.route('/colour', methods = ['GET', 'POST'])
    def Colour():
        form = colourForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.colour
            return redirect('/weight')
        return render_template('template.html', form=form)

    @app.route('/importance', methods = ['GET', 'POST'])
    def Importance():
        form = importanceForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.importance
            return redirect('/electronic')
        return render_template('template.html', form=form)

    @app.route('/electronic', methods = ['GET', 'POST'])
    def Electronic():
        form = electronicForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.electronic
            return redirect('/lastseen')
        return render_template('template.html', form=form)


    @app.route('/lastseen', methods = ['GET', 'POST'])
    def LastSeen():
        form = lastSeenForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.lastSeen
            return redirect('/outin')
        return render_template('template.html', form=form)

    @app.route('/outin', methods = ['GET', 'POST'])
    def OutIn():
        form = outInForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.outIn
            return redirect('/material')
        return render_template('template.html', form=form)

    @app.route('/material', methods = ['GET', 'POST'])
    def Material():
        form = materialForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.material
            return redirect('/found')
        return render_template('template.html', form=form)
    
    @app.route('found'), methods = ['GET', 'POST']
    def Found():
        # TODO return funny result

# }}}

# {{{ forms
class sizeForm(Form):
    sizeChoices = [('1', 'Liten'), ('2','Lagom'), ('3','Ganska stor'), ('3', 'Sjukt stor')]
    size = SelectField(u'Storlek', choices=sizeChoices)

class colourForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Färg', choices=colourChoices)

class importanceForm(Form):
    importanceChoices = [('1', u'Jag bryr mig inte'), ('2', u'Jag gillar den lite'), ('3', u'Det är det käraste jag äger'), ('4', u'Utan den här så dör jag')]
    importance = SelectField(u'Hur viktig är den för dig?', choices=importanceChoices)

class electronicForm(Form):
    electronicChoices = [('1', u'Nej'), ('2', u'Kanske')]
    electronic = BooleanField(u'Är den elektronisk?', choices=electronicChoices)

class lastSeenForm(Form):
    lastSeenChoices = [('1', u'Igår'), ('2', u'Förra måndagen'), ('3', u'Förut')]
    lastSeen = SelectField(u'När såg du den senast?', choices = lastSeenChoices)

class outInForm(Form):
    outInChoices = [('1', u'Ute'), ('2', u'Inne')]
    outIn = BooleanField(u'Hade du den ute eller inne?', choices=outInChoices)

class materialForm(Form):
    materialChoices = [('1', u'Cederträ'), ('2', u'Betong'), ('3', u'Plast'), ('4', u'Fryst kaffe'), ('5', u'Kolfiber'), ('6', u'Titan'), ('7', 'Ull')]
    material = SelectField(u'Vilket material är saken?', choices=colourChoices)

# }}}
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

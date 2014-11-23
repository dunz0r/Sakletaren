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
from wtforms import Form, SelectField
import logging
from PIL import Image, ImageDraw
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# }}}

sak = ''
# {{{ pages
class pages():
    @app.route('/', methods = ['GET', 'POST'])
    def Size():
        global sak
        redir = '/colour'
        route = '/'
        form = sizeForm(request.form)
        if request.method == 'POST':
            sak = sak + form.size.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.size, label=form.size.label)

    @app.route('/colour', methods = ['GET', 'POST'])
    def Colour():
        global sak
        route = '/colour'
        redir = '/importance'
        form = colourForm(request.form)
        if request.method == 'POST':
            sak = sak + form.colour.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.colour, label=form.colour.label)

    @app.route('/importance', methods = ['GET', 'POST'])
    def Importance():
        global sak
        route = 'importance'
        redir = '/electronic'
        form = importanceForm(request.form)
        if request.method == 'POST':
            sak = sak + form.importance.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.importance, label=form.importance.label)

    @app.route('/electronic', methods = ['GET', 'POST'])
    def Electronic():
        global sak
        route = '/electronic'
        redir = '/lastseen'
        form = electronicForm(request.form)
        if request.method == 'POST':
            sak = sak + form.electronic.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.electronic, label=form.electronic.label)


    @app.route('/lastseen', methods = ['GET', 'POST'])
    def LastSeen():
        global sak
        route = '/lastseen'
        redir = '/outin'
        form = lastSeenForm(request.form)
        if request.method == 'POST':
            sak = sak + form.lastSeen.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.lastSeen, label=form.lastSeen.label)

    @app.route('/outin', methods = ['GET', 'POST'])
    def OutIn():
        global sak
        route = '/outin'
        redir = '/material'
        form = outInForm(request.form)
        if request.method == 'POST':
            sak = sak + form.outIn.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.outIn, label=form.outIn.label)

    @app.route('/material', methods = ['GET', 'POST'])
    def Material():
        global sak
        route = '/material'
        redir = '/found'
        form = materialForm(request.form)
        if request.method == 'POST':
            app.logger.info(form.material)
            sak = sak + form.material.data
            return redirect(redir)
        return render_template('template.html', form=form, redir=route, field=form.material, label=form.material.label)

    @app.route('/image', methods = ['GET', 'POST'])
    @app.route('/found', methods = ['GET', 'POST'])
    def Found():
        global sak
        app.logger.info(unicode(sak))
        return render_template('found.html', thing=sak, label=u'Jag vet vart den är, den är;')
        # TODO return funny result

# }}}

# {{{ forms
class sizeForm(Form):
    sizeChoices = [('1', 'Liten'), ('2','Lagom'), ('3','Ganska stor'), ('3', 'Sjukt stor')]
    size = SelectField(u'Hur stor är saken?', choices=sizeChoices)

class colourForm(Form):
    colourChoices = [('1', u'Bränd Umbra'), ('2', u'Nattsvart'), ('3', u'Skogsgrön'), ('4', u'Turkos'), ('5', u'Scharlakansröd'), ('6', u'Lila'), ('7', 'Gammelrosa')]
    colour = SelectField(u'Vilken färg har saken?', choices=colourChoices)

class importanceForm(Form):
    importanceChoices = [('1', u'Jag bryr mig inte'), ('2', u'Jag gillar den lite'), ('3', u'Det är det käraste jag äger'), ('4', u'Utan den här så dör jag')]
    importance = SelectField(u'Hur viktig är den för dig?', choices=importanceChoices)

class electronicForm(Form):
    electronicChoices = [('1', u'Nej'), ('2', u'Kanske')]
    electronic = SelectField(u'Är den elektronisk?', choices=electronicChoices)

class lastSeenForm(Form):
    lastSeenChoices = [('1', u'Igår'), ('2', u'Förra måndagen'), ('3', u'Förut')]
    lastSeen = SelectField(u'När såg du den senast?', choices = lastSeenChoices)

class outInForm(Form):
    outInChoices = [('1', u'Ute'), ('2', u'Inne')]
    outIn = SelectField(u'Hade du den ute eller inne?', choices=outInChoices)

class materialForm(Form):
    materialChoices = [('1', u'Cederträ'), ('2', u'Betong'), ('3', u'Plast'), ('4', u'Fryst kaffe'), ('5', u'Kolfiber'), ('6', u'Titan'), ('7', 'Ull')]
    material = SelectField(u'I vilket material är saken?', choices=materialChoices)

# }}}
if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.debug = True
    app.run(host='0.0.0.0')

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
from wtforms import Form, RadioField, TextField, TextAreaField, SelectField

app = Flask(__name__)
sak = {}
# }}}

# {{{ pages
class pages():
    @app.route('/', methods = ['GET', 'POST'])
    def Size():
        redir = '/colour'
        form = sizeForm(request.form)
        if request.method == 'POST':
            sak['size'] = form.size
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.size, label=form.size.label)

    @app.route('/colour', methods = ['GET', 'POST'])
    def Colour():
        redir = '/importance'
        form = colourForm(request.form)
        if request.method == 'POST':
            sak['colour'] = form.colour
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.colour, label=form.colour.label)

    @app.route('/importance', methods = ['GET', 'POST'])
    def Importance():
        redir = '/electronic'
        form = importanceForm(request.form)
        if request.method == 'POST':
            sak['importance'] = form.importance
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.importance, label=form.importance.label)

    @app.route('/electronic', methods = ['GET', 'POST'])
    def Electronic():
        redir = '/lastseen'
        form = electronicForm(request.form)
        if request.method == 'POST':
            sak['electronic'] = form.electronic
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.electronic, label=form.electronic.label)


    @app.route('/lastseen', methods = ['GET', 'POST'])
    def LastSeen():
        redir = '/outin'
        form = lastSeenForm(request.form)
        if request.method == 'POST':
            sak['lastseen'] = form.lastSeen
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.lastSeen, label=form.lastSeen.label)

    @app.route('/outin', methods = ['GET', 'POST'])
    def OutIn():
        redir = '/material'
        form = outInForm(request.form)
        if request.method == 'POST':
            sak['outin'] = form.outIn
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.outIn, label=form.outIn.label)

    @app.route('/material', methods = ['GET', 'POST'])
    def Material():
        redir = '/found'
        form = materialForm(request.form)
        if request.method == 'POST':
            sak['material'] = form.material
            return redirect(redir)
        return render_template('template.html', form=form, redir=redir, field=form.material, label=form.material.label)

    @app.route('/found', methods = ['GET', 'POST'])
    def Found():
        return render_template('found.html')
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
    electronic = RadioField(u'Är den elektronisk?', choices=electronicChoices)

class lastSeenForm(Form):
    lastSeenChoices = [('1', u'Igår'), ('2', u'Förra måndagen'), ('3', u'Förut')]
    lastSeen = SelectField(u'När såg du den senast?', choices = lastSeenChoices)

class outInForm(Form):
    outInChoices = [('1', u'Ute'), ('2', u'Inne')]
    outIn = RadioField(u'Hade du den ute eller inne?', choices=outInChoices)

class materialForm(Form):
    materialChoices = [('1', u'Cederträ'), ('2', u'Betong'), ('3', u'Plast'), ('4', u'Fryst kaffe'), ('5', u'Kolfiber'), ('6', u'Titan'), ('7', 'Ull')]
    material = SelectField(u'I vilket material är saken?', choices=materialChoices)

# }}}
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

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

@app.route('/')
def index():
    return "Sakletaren"

if __name__ == '__main__':
    app.run()

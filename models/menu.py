# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('voting', SPAN(4), 'dummies'),
                  _class="navbar-brand", callback=URL('default', 'index'),
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Check if you are registered'), False, 'http://www.sos.ca.gov/elections/registration-status/', []),
    (T('Where to vote'), False, 'http://www.sos.ca.gov/elections/polling-place', []),
    (T('Voter rights'), False, 'http://www.sos.ca.gov/elections/voter-bill-rights/', []),
    (T('Register to vote'), False, 'http://registertovote.ca.gov/', [])
]

if "auth" in locals():
    auth.wikimenu()

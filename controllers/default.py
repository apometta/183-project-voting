# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict()

#returns all election data along with user information if there is a user logged in
def get_data():
    national = []
    state_races = db(db.races.election_level == 0).select()
    state_measures = db(db.measures.election_level == 0).select()
    local_races = []
    local_measures = []
    current_user = auth.user.email if auth.user is not None else None
    if current_user is not None:
        userLocation = db(db.auth_user.id == auth.user_id).select(db.auth_user.city).first()
        local_races = db(db.races.locationName == userLocation).select()
        local_measures = db(db.measures.locationName == userLocation).select()
    return response.json(dict(
        current_user = current_user,
        national = national,
        state_races = state_races,
        state_measures = state_measures,
        local_races = local_races,
        local_measures = local_measures
    ))

#used to save a user's voting decisions
@auth.requires_login()
def update_votes():
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if (request.args(0) == 'profile' or request.args(0) == 'register') and request.post_vars.city:
        request.post_vars.city = request.vars.city = request.post_vars.city.lower()
        #check if the user is entering a valid city/county
        if db(db.races.locationName == request.vars.city).select().first() is None:
            request.post_vars.city = request.vars.city = ''
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()



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
    votes_races = []
    votes_measures = []
    current_user = auth.user.email if auth.user is not None else None
    if current_user is not None:
        userLocation = db(db.auth_user.id == auth.user_id).select(db.auth_user.city).first().city
        local_races = db((db.races.locationName == userLocation) & (db.races.election_level != 0)).select()
        local_measures = db((db.measures.locationName == userLocation) & (db.measures.election_level != 0)).select()
        votes_races = db(db.votes_races.user_email == current_user).select()
        votes_measures = db(db.votes_measures.user_email == current_user).select()
    return response.json(dict(
        current_user = current_user,
        national = national,
        state_races = state_races,
        state_measures = state_measures,
        local_races = local_races,
        local_measures = local_measures,
        votes_races = votes_races,
        votes_measures = votes_measures
    ))

#used to save a user's voting decisions
@auth.requires_login()
def update_votes():
    user_election_info = db(db.votes_races.user_email == auth.user.email).select().first()
    user_prop_info = db(db.votes_measures.user_email == auth.user.email).select().first()

    if user_election_info is not None:
        user_election_info.votes_json = request.vars.election_info
        user_election_info.update_record()
    else:
        db.votes_races.insert(
            user_email = auth.user.email,
            votes_json = request.vars.election_info
        )

    if user_prop_info is not None:
        user_prop_info.votes_json = request.vars.prop_info
        user_prop_info.update_record()
    else:
        db.votes_measures.insert(
            user_email = auth.user.email,
            votes_json = request.vars.prop_info
        )

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
            if db(db.measures.locationName == request.vars.city).select().first() is None:
                request.post_vars.city = request.vars.city = ''
    return dict(form=auth())

@auth.requires_login()
def print_page():
    import json
    voting_choices = {}
    election_votes = json.loads(db(db.votes_races.user_email == auth.user.email).select(db.votes_races.votes_json).first().votes_json)
    for idx, vote in enumerate(election_votes):
        if vote is not None:
            race = db(db.races.id == idx).select().first()
            vote = ''.join(vote)
            #voting_choices.append(race.office + ": " + vote)
            voting_choices[race.office] = vote

    measure_votes = json.loads(db(db.votes_measures.user_email == auth.user.email).select(db.votes_measures.votes_json).first().votes_json)
    for idx, vote in enumerate(measure_votes):
        if vote is not None:
            race = db(db.measures.id == idx).select().first()
            #voting_choices.append(race.letter + ": " + vote)
            voting_choices[race.letter] = vote

    return dict(voting_choices = voting_choices)

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



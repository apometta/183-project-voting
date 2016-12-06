import datetime

#user vote data
db.define_table('votes',
    Field('user_email'),
    Field('vote_topic'),
    Field('vote_selection'),
)

#CSD and school zone props might not be used if it is not feasible to determine which/if a person resides in one.
#if it is easier a dummy string like "statewide" or "California" can be used for county/locationName, just change
#the default to a string literal
db.define_table('measures',
    Field('election_level', default=0), #0 = state-wide, 1 = county, 2 = city, 3 = school zone, 4 = CSD
    #A county/locationName of None indicates it is a statewide measure
    Field('county', default=None), #county name.  needed in all props, even if it's a city prop
    Field('locationName', default=None), #name of county/city/school/CSD.
    Field('letter'), #e.g. prop E or prop Z.  can be numbers for statewide but still a string
    Field('topic'), #e.g. Governance: Organization, or something like that
    Field('question'), #"Shall the county of ...?"
)

#A "candidate" has the following information attatched to them: name (first and last), occupation, and perhaps party.
#A separate database isn't necessary to hold this imo, the candidates could just be a 2D array, i.e. the outer array
#('candidates') holds each candidate, and each candidate array hols name, occupation, party
db.define_table('races',
     Field('election_level', default=0), #same standard as in measures
     Field('county', default=None),
     Field('locationName', default=None),
     Field('office'), #e.g. City Council, Port Commisioner, etc.
     Field('vacancies', default=1), #number of candidates to be voted for, e.g. 4 city council members
     Field('name_list', 'list:string'), #list of candidate names
     Field('occupation_list', 'list:string') #list of candidate occupations
)

db.define_table('votes_races',
    Field('user_email'),
    Field('votes_json', 'text'), # Votes information, in json
)

db.define_table('votes_measures',
    Field('user_email'),
    Field('votes_json', 'text'), # Votes information, in json
)

import datetime

#workaround function.  the name_list and occupation_list fields are, by default, passed in as a string list of
#length 1, where the string is the actual list we wanted.  so we pass this into some dummy field, and set the default
#for what we want as the output of this function.  there's definitely a better way to do it but this works
def format_list_string(strlist):
    raw_str = strlist[0] #it is technically a list
    raw_str.replace("'", "")
    raw_str.replace("\"", "")
    raw_str.replace(", ", ",") #remove quotes, extra spaces
    return raw_str.split(",")

#function for properly formatting office name
def office_format(office_raw_str):
    office_str = office_raw_str
    for i in xrange(len(office_str)):
        if i == 0 or office_str[i - 1] == " ":
            office_str[i].capitalize()
    return office_str

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

import datetime

#user vote data
db.define_table('votes',
    Field('user_email'),
    Field('vote_topic'),
    Field('vote_selection'),
)
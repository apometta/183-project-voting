CMPS 183 - FINAL Project
authors: Sean Mendonca, smendonc@ucsc.edu
         Andrew H. Pometta, apometta@ucsc.edu
Class: CMPS 183, Fall quarter, 2016
Presented 6 December 2016
Project Name: Voting for Dummies
URL: http://apometta.pythonanywhere.com/

The aim of this project is to provide a basic, simple tool for voters to store
their prospective votes, view what they can vote on, and provide a quick and
easy resource center for other important voting links (registering to vote,
where to vote, etc).

The website can be accessed by navigating to apometta.pythonanywhere.com.
The top bar contains useful links to check whether a user is registered,
where they can vote, and what their rights are.  The statewide elections are
also shown.  For this site, 2014 election data is used due to its easy 
availability and storage.  In 2014, there were, on the general election
ballot, 6 statewide propositions (propositions 43-48) and a gubernatorial
election.

If a user logs in, or registers, they input their location name.  When they
do, they can see measures and races for their local county and city as well.
In addition, they have the ability to save their votes, and a button provides
a quick link to a basic page where they can print this information, to be
used as a pre-prepared cheat sheet during voting.

The database holds information acquired and reorganized from the California
Elections Data Archive (CEDA), although the statewide information was
hardcoded in.  Separate database tables are used to store measures
(propositions) and races (with candidates).  There are also two separate
tables for storing which measures and races users have stored their votes for.
Stored votes are, naturally, unique to each user, as well as their location.

USAGE NOTES:
* Despite asking for "city", either city our county works.  The only place that
  demands a differentiation, from an eyeball view of the spreadsheet, is
  San Luis Obispo, which had city propositions but no county named after it.
  You'll probably get an error if you put it in, since the county is unknown
  (in the best case, you just won't get county information).  Putting in
  legitimate cities that had no city measures/races and aren't the names of
  counties fails, since they are not in the database: just put in the county
  name instead.
* The print page is really basic, but it's only intention is to record the
  answers.  It could be a lot prettier, but the mantra of this entire, fairly
  ugly project is "it works".
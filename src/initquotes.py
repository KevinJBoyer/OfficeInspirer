#!/usr/bin/env python3


import logging
import pickle

from models.quotelist import QuoteList
from models.quote import Quote


fileName = "quotes.pck"
quotes = QuoteList()

"""
logging.debug("Loading quotes from <%s>." % fileName)

try:
	with open( fileName,'rb' ) as f:
		quotes = pickle.load( f )
		logging.debug("Loaded quotes successfully.")

except IOError:
	logging.warn("Unable to load <%s>." % fileName)
"""

"""
quotes.add( Quote( \
    "", \
    "" \
    ))
"""

quotes.add( Quote( \
    "By providing more opportunities for people to feel part of something bigger than themselves, we can more strongly stitch together the fabric of our nation.", \
    "MacKenzie Moritz" \
    ))

quotes.add( Quote( \
    "Service is the American way to change America.", \
    "Shirley Sagawa" \
    ))

quotes.add( Quote( \
    "Through a serious commitment to bridging our differences and restoring our confidence in solving big challenges together, America can reignite the energy needed to make our country what it can be.", \
    "General Stanley McChrystal" \
    ))

quotes.add( Quote( \
    "We need to think bigger to leverage the human capital represented by the half a million young adults who want to serve.", \
    "Shirley Sagawa" \
    ))

quotes.add( Quote( \
    "America needs a big idea that plays to its strength - and that strength is in the little platoons of civil society found in our schools, churches, community nonprofits, and the talents and compassion of millions of Americans who want to serve their country every year.", \
    "John Bridgeland" \
    ))

quotes.add( Quote( \
	"We have an urgent need to recruit this generation to become our community leaders and agents of change.", \
	"Rosa Moreno" \
	))


quotes.add( Quote( \
	"By making national service a part of the American way of life, we will create a common universal experience and build a stronger sense of citizenship while breaking down barriers of race, class, and religion.", \
	"Alan Khazei" \
))

logging.debug("Saving quotes to <%s>." % fileName)
try:
	with open( fileName,'wb' ) as f:
		pickle.dump(quotes , f)
		logging.debug("Saved quotes successfully.")

except: logging.warn("Couldn't save quotes to <%s>." % fileName)

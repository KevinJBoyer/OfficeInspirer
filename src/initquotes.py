#!/usr/bin/env python3


import pickle

from models.quotelist import QuoteList
from models.quote import Quote


fileName = "quotes.pck"



logging.debug("Loading quotes from <%s>." % fileName)

try:
	with open( fileName,'rb' ) as f:
		quotes = pickle.load( f )
		logging.debug("Loaded quotes successfully.")
		return quotes

except IOError:
	logging.warn("Unable to load <%s>." % fileName)
	quotes = QuoteList()

quotes.add( Quote( \
    "By providing more opportunities for people to feel part of something bigger than themselves, we can more strongly stitch together the fabric of our nation.", \
    "MacKenzie Moritz" \
    ))

logging.debug("Saving quotes to <%s>." % fileName)
try:
	with open( fileName,'wb' ) as f:
		pickle.dump(quotes , f)
		logging.debug("Saved quotes successfully.")

except: logging.warn("Couldn't save quotes to <%s>." % fileName)

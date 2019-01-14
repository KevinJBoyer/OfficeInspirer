#!/usr/bin/env python3

import logging
import pickle

#import aiy.audio
#import aiy.cloudspeech
#import aiy.voicehat
#import aiy.voice.tts

from models.id import Id
from models.quotelist import QuoteList
from models.quote import Quote


QUOTE_FILE     = "quotes.pck"

PREFIX         = ""
COMMAND_RANDOM = PREFIX + "say quote" #inspire me
COMMAND_GET_ID = PREFIX + "what was that"
COMMAND_ADD    = PREFIX + "add quote"
COMMAND_FORGET = PREFIX + "forget"
COMMAND_ABORT  = "never mind"


def listen( question = "" ):
	logging.debug("Listening. Asked <%s>." % question)

	response = input( question )

	logging.debug("Heard <%s>." % response)

	return response


def say( message ):
#	aiy.voice.tts.say(message)
	print (message)


def verify(question):

	gotItRight = False
	while not gotItRight:
		answer = listen(question + " ")

		verify = listen( \
			"I heard %s. Is that correct? You can say yes, no, or %s. " \
			 % (answer, COMMAND_ABORT))

		if verify == COMMAND_ABORT:
			logging.debug("Received abort command.")
			return COMMAND_ABORT

		gotItRight = (verify == "yes")

		if not gotItRight:
			logging.debug("Input <%s> refuted. Trying again." % answer)

	logging.debug("Successfully verified <%s>." % answer )

	return answer


def doRandom(quotes):
	logging.debug("Received doRandom command.")

	quote = quotes.getRandomQuote()

	logging.debug("Saying quote <%s>." % quote.getId() )
	say ( quote.say() )


def doGetId(quotes):
	logging.debug("Received doGetId command.")

	id = quotes.getLastSaid().getId()

	logging.debug("Retrieved last id <%s>." % id)
	say ("That was %s" % id)


def doAdd(quotes):
	logging.debug("Received doAdd command.")

	saying = verify("What is the quote?")
	if saying == COMMAND_ABORT: return

	author = verify("Who said it?")
	if author == COMMAND_ABORT: return

	newQuote = Quote( saying, author )

	logging.debug( "Adding quote <%s>." % newQuote )
	quotes.add( newQuote )


def doForget(quotes, input):
	logging.debug("Received doForget command.")

	targetId = Id( input.replace(COMMAND_FORGET + " ", "") )
	logging.debug("Removing quote with id <%s>." % targetId)

	say ("Removing quote <%s>." % targetId)
	quotes.delete(targetId)

	say ( quotes )

	return quotes


def load( fileName ):
	logging.debug("Loading quotes from <%s>." % fileName)

	try:
		with open( fileName,'rb' ) as f:
			quotes = pickle.load( f )
			logging.debug("Loaded quotes successfully.")
			return quotes

	except IOError:
		logging.warn("Unable to load <%s>." % fileName)
		return QuoteList()


def save( fileName, quotes ):
	logging.debug("Saving quotes to <%s>." % fileName)
	try:
		with open( fileName,'wb' ) as f:
			pickle.dump(quotes , f)
			logging.debug("Saved quotes successfully.")

	except: logging.warn("Couldn't save quotes to <%s>." % fileName)


def main():

	logging.basicConfig(level=logging.DEBUG)

	quotes = load( QUOTE_FILE )

	while True:
		input = listen()

		if input == COMMAND_RANDOM: doRandom(quotes)
		if input == COMMAND_GET_ID: doGetId(quotes)
		if input == COMMAND_ADD:    doAdd(quotes)
		if COMMAND_FORGET in input:
			quotes = doForget( quotes, input )

		save( QUOTE_FILE, quotes)



if __name__ == '__main__':
	main()

# QuoteCollector

An app for the [Google AIY Voice Kit](https://aiyprojects.withgoogle.com/voice/) that manages a collection of quotes entirely through a voice user interface, including adding, deleting, and randomly sharing quotes.

## Getting Started

Run initquotes.py to create an initial quotes.pck file populated with inspiring quotes on [universal national service](https://www.serviceyearalliance.org).

Then use either the command line UI (if on a computer) or the voice UI (if on an AIY Voice Kit device.)

Every quote has an associated three word ID (e.g., "study name end") to facilitate easy removal when using the voice interface.

## Voice UI

Press the main button, and the kit will start listening for your voice command.

Say a random quote:
```
inspire me
```

Get the ID of the last quote:
```
what was that
```

Add a new quote to the collection:
```
add quote
```

Remove a quote from the collection:
```
forget <ID>
```
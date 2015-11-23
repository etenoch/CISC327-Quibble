# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The Event file holds instances of type event. The event instance hold information relating to
# each event including the event name, number of tickets and the date of the event (YYMMDD).
from testing import *
class Event:

    # The constructor function takes in parameters such as the name of the event (string),
    # the number of tickets available (int) and the date in the format YYMMDD (int).
    def __init__(self, eventName, numTickets, date):
        logBranch(10,"Event",14); self.eventName = eventName.strip()
        self.numTickets = int(numTickets)
        self.date = date

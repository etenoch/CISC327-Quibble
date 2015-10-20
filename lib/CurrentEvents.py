# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The current event class assigns attributes to the current event object.

from Event import Event

class CurrentEvents:

    def __init__(self):
        self.events = {}

    def getEvent(self,eventName):
        if eventName in self.events:
            return self.events[eventName]
        else:
            return False

    def addEvent(self,event):
        self.events[event.eventName] = event

    def removeEvent(self,eventName):
        if eventName in self.events:
            del self.events[eventName]

    def fromFile(self,filename):
        with open(filename) as input_file:
            for i, line in enumerate(input_file):
                if line[:20].strip() != "END":
                    newEvent = Event(line[:20].strip(),int(line[21:]))
                    self.events[newEvent.eventName] = newEvent




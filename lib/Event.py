# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


class Event:

    def __init__(self, eventName, numTickets):
        self.eventName = eventName
        self.numTickets = numTickets
        self.numPendingTickets = 0

    def addTickets(self, numTickets):
        self.numPendingTickets += numTickets

    def removeTickets(self, numTickets):
        self.numTickets -= numTickets

    def deleteEvent(self):
        self.numTickets = 0
        self.numPendingTickets = 0



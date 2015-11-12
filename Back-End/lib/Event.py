

class Event:

    def __init__(self, eventName, numTickets, date):
        self.eventName = eventName.strip()
        self.numTickets = int(numTickets)
        self.date = date

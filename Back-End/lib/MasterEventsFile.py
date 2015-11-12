
from Event import *
from Transaction import *

class MasterEventsFile:

    def __init__(self):
        self.events = {}

    def addEvent(self,event):
        self.events[event.eventName] = event

    def processTransaction(self,transaction):
        if transaction.transactionType == Transaction.ADD:
            self.events[transaction.eventName].numTickets += int(transaction.numTickets)
        elif transaction.transactionType == Transaction.DELETE:
            del self.events[transaction.eventName]
        elif transaction.transactionType == Transaction.RETURN:
            self.events[transaction.eventName].numTickets += int(transaction.numTickets)
        elif transaction.transactionType == Transaction.CREATE:
            event = Event(transaction.eventName, transaction.numTickets, transaction.date)
            self.addEvent(event)
        elif transaction.transactionType == Transaction.SELL:
            self.events[transaction.eventName].numTickets -= int(transaction.numTickets)

    def createCurrentEventsFile(self,filename):
        file = open(filename,"w")
        for e in self.events:
            line = "%s %05d\n" % (self.events[e].eventName.ljust(20), self.events[e].numTickets)
            file.write(line)
        file.write("END                  00000")

    def toFile(self,filename):
        # sort
        file = open(filename, "w")
        for t in self.events:
            date = 0 if self.events[t].date == "" or self.events[t].date == 0 else int(self.events[t].date)
            line = "%06d %05d %s\n" % (date, self.events[t].numTickets, self.events[t].eventName.ljust(20))
            file.write(line)
        # file.write("00                      000000 00000")

    def fromFile(self, filename):
        with open(filename) as input_file:
            for i, line in enumerate(input_file):
                if line.strip() != "END":
                    date = line[:6]
                    numTickets = line[7:12]
                    name = line[13:].strip()
                    event = Event(name, numTickets, date)
                    self.addEvent(event)


# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The MasterEventsFile deals with adding a new instances of an event, processing
# each transaction as determined by its type, creating the output files, and writing
# output to a file.

from Event import *
from Transaction import *
import datetime

class MasterEventsFile:

    def __init__(self):
        self.events = {}

    # The addEvent function takes in an instance of type event and adds it the the master list.
    def addEvent(self,event):
        self.events[event.eventName] = event

    # The processTransaction file takes in an instance of type transaction. It than procceeds
    # accordingly depending on its indicated type.
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

    # The createCurrentEventsFile funaction takes in a output filename (string) and creates a new current events
    # file containing the details of an event with an ending statement.
    def createCurrentEventsFile(self,filename):
        file = open(filename,"w")
        for e in self.events:
            line = "%s %05d\n" % (self.events[e].eventName.ljust(20), self.events[e].numTickets)
            file.write(line)
        file.write("END                  00000")

    # The toFile function takes in a output filename (string) and writes to a new file master
    # events files adding all the event information.
    def toFile(self, filename):
        # sort
        sortedList = sorted(self.events.values(), key=lambda ev: self.dateToUnixTime(ev.date))

        file = open(filename, "w")
        for ev in sortedList:
            date = 0 if ev.date == "" or ev.date == 0 else int(ev.date)
            line = "%06d %05d %s\n" % (date, ev.numTickets, ev.eventName.ljust(20))
            file.write(line)
            # file.write("00                      000000 00000")

    # The fromFile function reads event input data from a input file and creates a new event
    # instance from the information obtained.
    def fromFile(self, filename):
        with open(filename) as input_file:
            for i, line in enumerate(input_file):
                if line.strip() != "END":
                    date = line[:6]
                    numTickets = line[7:12]
                    name = line[13:].strip()
                    event = Event(name, numTickets, date)
                    self.addEvent(event)

    # helper function to convert quibble date format to unix time for easy comparision
    def dateToUnixTime(self,date):
        return datetime.datetime.strptime(str(date), "%y%m%d").strftime("%s")


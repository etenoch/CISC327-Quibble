
from Event import *

class MasterEventsFile:

    def __init__(self):
        self.events = {}

    def addEvent(self,event):
        self.events.append(event)

    def processTransaction(self,transaction):
        # stub

    def createCurrentEventsFile(self,filename):
        file = open(filename,"w")
        for t in self.events:
            date = 0 if t.date=="" else int(t.date)
            line = "%s %05d\n" % (t.eventName.ljust(20),t.numTickets)
            file.write(line)
            file.write ("END")

    def toFile(self,filename):
        # sort
        file = open(filename,"w")
        for t in self.events:
            date = 0 if t.date=="" else int(t.date)
            line = "%06d %05d %s\n" % (date,t.numTickets,t.eventName.ljust(20))
            file.write(line)
        # file.write("00                      000000 00000")

    def fromFile(self,filename):
        with open(filename) as input_file:
            for i, line in enumerate(input_file):
                if line.strip() != "END":
                    date = line[:6]
                    numTickets = line[7:12]
                    name = line[13:]
                    event = Event(name, numTickets, date)
                    self.addEvent(event)


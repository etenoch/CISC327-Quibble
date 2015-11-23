# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The Transaction file is in charge of dealing with the transactions in the system. It creates
# instances of type transaction that holds relevant information on each transaction in the
# system.
from testing import *
class Transaction:

    SELL = 1
    RETURN = 2
    CREATE = 3
    ADD = 4
    DELETE = 5
    END = 0

    # The constructor stores information pertaining to each transaction. The function takes in
    # the event name (string) and the transaction type (int). It also creates a default
    # nubmer of ticket of 0 and a blank date.
    def __init__(self, eventName, transactionType, numTickets=0, date=""):
        self.eventName = eventName
        self.date = date
        self.transactionType = transactionType
        self.numTickets = numTickets

    # The newInstanceFromLine function parses through each transaction line taking in as type (string)
    # and returns the information into a type transaction instance.
    def newInstanceFromLine(transactionLine):
        ttype = int(transactionLine[:2])
        name = transactionLine[3:23].strip()
        date = transactionLine[24:30]
        numtickets = transactionLine[31:]

        if date and numtickets:
            return Transaction(name, ttype, int(numtickets), date)

    # newInstanceFromLine is a builder/factory method -> therefor make it a static method
    newInstanceFromLine = staticmethod(newInstanceFromLine)

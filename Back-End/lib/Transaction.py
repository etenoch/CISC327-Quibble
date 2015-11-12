


class Transaction:

    SELL = 1
    RETURN = 2
    CREATE = 3
    ADD = 4
    DELETE = 5
    END = 0

    def __init__(self, eventName, transactionType, numTickets=0, date=""):
        self.eventName = eventName
        self.date = date
        self.transactionType = transactionType
        self.numTickets = numTickets

    def newInstanceFromLine(transactionLine):
        ttype = int(transactionLine[:2])
        name = transactionLine[3:23].strip()
        date = transactionLine[24:30]
        numtickets = transactionLine[31:]

        if date and numtickets:
            return Transaction(name, ttype, int(numtickets), date)

    newInstanceFromLine = staticmethod(newInstanceFromLine)


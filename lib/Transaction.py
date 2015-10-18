# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


class Transaction:

    SELL = 1
    RETURN = 2
    CREATE = 3
    ADD = 4
    DELETE = 5
    END = 0

    def __init__(self, eventName, transactionType, date=0, numTickets=0):
        self.eventName = eventName
        self.date = date
        self.transactionType = transactionType
        self.numTickets = numTickets

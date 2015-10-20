# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


class DailyTransactions:

    def __init__(self):
        self.transactions = []

    def addTransaction(self,transaction):
        self.transactions.append(transaction)

    def toFile(self,filename):
        file = open(filename,"w")
        for t in self.transactions:
            date = 0 if t.date=="" else int(t.date)
            line = "%02d %s %06d %05d" % (t.transactionType, t.eventName.ljust(20),date,t.numTickets)
            file.write(line)
        print ""




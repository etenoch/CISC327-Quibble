# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The DailyTransactions file imports from Transaction. It is responsible for appending
# all the transactions to a master list, as well as it reads in a text file and parses
# though the data.

from Transaction import *

class DailyTransactions:

    def __init__(self):
        self.transactions = []

    # The addTransaction function takes in an instance of a transaction and appends it to a master
    # list.
    def addTransaction(self, transaction):
        self.transactions.append(transaction)


    # The fromFile function reads in data from a textfile (filename) and parses it by striping the blank
    # characters row by row into a workable format (transaction class).
    def fromFile(self, filename):
        with open(filename) as input_file:
            for i, line in enumerate(input_file):
                if line.strip()[:2] != "00":
                    transaction = Transaction.newInstanceFromLine(line.strip())
                    self.addTransaction(transaction)

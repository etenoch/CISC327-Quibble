
from Transaction import *

class DailyTransactions:

    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def fromFile(self, filename):
        with open(filename) as input_file:
            for i, line in enumerate(input_file):
                if line.strip()[:2] != "00":
                    transaction = Transaction.newInstanceFromLine(line.strip())
                    self.addTransaction(transaction)

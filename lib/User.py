# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

from lib.Transaction import Transaction

class User:

    def __init__(self, admin):
        self.admin = admin

    def validCommand(self, type):
        if self.admin:
            if (type == Transaction.SELL or
                    type == Transaction.RETURN or
                    type == Transaction.CREATE or
                    type == Transaction.ADD or
                    type == Transaction.DELETE):
                return True
        elif not self.admin:
            if type == Transaction.SELL or type == Transaction.RETURN:
                return True

        return False

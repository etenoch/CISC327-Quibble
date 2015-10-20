# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# Creating user class which checks is user has the right permissions #

from lib.Transaction import Transaction

class User:

    def __init__(self, admin):
        self.admin = admin

    def validCommand(self, type):
        if self.admin: # User is admin
            if (type == Transaction.SELL or
                        type == Transaction.RETURN or
                        type == Transaction.CREATE or
                        type == Transaction.ADD or
                        type == Transaction.DELETE):
                return True
        elif not self.admin: # Basic non admin user
            if type == Transaction.SELL or type == Transaction.RETURN:
                return True

        return False

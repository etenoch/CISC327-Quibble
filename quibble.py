# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


from lib.Event import Event
from lib.CurrentEvents import CurrentEvents
from lib.Transaction import Transaction
from lib.DailyTransactions import DailyTransactions
from lib.User import User

programloop = True

currentEvents = CurrentEvents()
currentEvents.fromFile("filepath")  # readin current events

dailyTransactions = DailyTransactions()

user = None

while programloop:
    command = raw_input().strip()

    if user is None:
        if command == "login":
            command = raw_input().strip()
            if command == "sales":
                user = User(False)
            elif command == "admin":
                user = User(True)
        else:
            print "throwerror"
    else:
        if command == "logout":
            programloop=False
            break
        elif command == "sell":
            if user.validCommand(Transaction.SELL):
                eventName = raw_input()
            else:
                print "throw error"
        elif command == "return":
            if user.validCommand(Transaction.RETURN):
                print "do stuff"
            else:
                print "throw error"
        elif command == "create":
            if user.validCommand(Transaction.CREATE):
                print "do stuff"
            else:
                print "throw error"
        elif command == "add":
            if user.validCommand(Transaction.ADD):
                print "do stuff"
            else:
                print "throw error"
        elif command == "delete":
            if user.validCommand(Transaction.DELETE):
                print "do stuff"
            else:
                print "throw error"
        else:
            print "throw error"

dailyTransactions.toFile("filepath")  # write output file

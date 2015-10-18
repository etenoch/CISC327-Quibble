# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


from lib.Event import Event
from lib.CurrentEvents import CurrentEvents
from lib.Transaction import Transaction
from lib.DailyTransactions import DailyTransactions
from lib.User import User

## initialize program ##
programloop = True

currentEvents = CurrentEvents()
currentEvents.fromFile("filepath")  # readin current events

dailyTransactions = DailyTransactions()

user = None


## Main Program Loop ##
while programloop:
    command = raw_input().strip()

    if user is None:  ## User hasn't logged in yet
        if command == "login":
            command = raw_input().strip()
            if command == "sales":
                user = User(False)
            elif command == "admin":
                user = User(True)
            else:
                print "throw error"  # only sales or admin allowed
        else:
            print "throw error"  # only login command allowed
    else:
        if command == "logout":
            programloop=False
            break
        elif command == "sell":
            if user.validCommand(Transaction.SELL):
                eventName = raw_input()
            else:
                print "throw error"  # permissions error
        elif command == "return":
            if user.validCommand(Transaction.RETURN):
                print "do stuff"
            else:
                print "throw error"  # permissions error
        elif command == "create":
            if user.validCommand(Transaction.CREATE):
                print "do stuff"
            else:
                print "throw error"  # permissions error
        elif command == "add":
            if user.validCommand(Transaction.ADD):
                print "do stuff"
            else:
                print "throw error"  # permissions error
        elif command == "delete":
            if user.validCommand(Transaction.DELETE):
                print "do stuff"
            else:
                print "throw error"  # permissions error
        else:
            print "throw error"  # invalid command


## Write transactions to file ##
dailyTransactions.toFile("filepath")  # write output file

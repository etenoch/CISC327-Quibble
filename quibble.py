# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


from lib.Event import Event
from lib.CurrentEvents import CurrentEvents
from lib.Transaction import Transaction
from lib.DailyTransactions import DailyTransactions
from lib.User import User

# initialize program #
programloop = True

currentEvents = CurrentEvents()
currentEvents.fromFile("currentEvents.txt")  # readin current events

dailyTransactions = DailyTransactions()

user = None


# Main Program Loop #
while programloop:
    command = raw_input().strip()

    if user is None:  # User hasn't logged in yet
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
                eventName = raw_input("Enter event name: ")
                if eventName.strip() in currentEvents.events: # event name valid
                    numTickets = raw_input("Enter num tickets: ")
                    if (not user.admin and numTickets <= 8) or ( numTickets <= currentEvents.getEvent(eventName).numTickets): # numtickets valid
                        dailyTransactions.addTransaction(Transaction(eventName, Transaction.SELL))  # sell ticket
                    else:
                        print "Error: Num tickets is invalid"
                else:
                    print "Error: Event name entered is invalid"
            else:
                print "throw error"  # permissions error
        elif command == "return":
            if user.validCommand(Transaction.RETURN):
                eventName = raw_input("Enter event name: ")
                if eventName.strip() in currentEvents.events: # event name valid
                    numTickets = raw_input("Enter num tickets: ")
                    if (not user.admin and numTickets <= 8) or (numTickets <= currentEvents.getEvent(eventName).numTickets): # numtickets valid
                        dailyTransactions.addTransaction(Transaction(eventName, Transaction.RETURN))  # Return ticket
                    else:
                        print "Error: Num tickets is invalid"
                else:
                    print "Error: Event name entered is invalid"
            else:
                    print "throw error"  # permissions error
        elif command == "create":
            if user.validCommand(Transaction.CREATE):
                eventName = raw_input("Enter event name: ")
                if not eventName.strip() in currentEvents.events and len(eventName)<=20: # event name valid
                    date = raw_input("Enter date (YYMMDD): ")
                    if Transaction.validDate(date): # date is valid
                        numTickets = raw_input("Enter num tickets: ")
                        if numTickets <= 99999:
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.CREATE,date,numTickets))  # create ticket
                        else:
                            print "Error: Number cannot be greater than 99999"
                    else:
                        print "Error: Input is invalid"
                else:
                    print "Error: Event name entered is invalid"
            else:
                    print "throw error"  # permissions error
        elif command == "add":
            if user.validCommand(Transaction.ADD):
                eventName = raw_input("Enter event name: ")
                if eventName.strip() in currentEvents.events: # event name valid
                    numTickets = raw_input("Enter num tickets: ")
                    if numTickets <= 99999:
                        dailyTransactions.addTransaction(Transaction(eventName, Transaction.ADD))  # add ticket
                    else:
                        print "Error: Number cannot be greater than 99999"
                else:
                    print "Error: Event name entered is invalid"
            else:
                    print "throw error"  # permissions error
        elif command == "delete":
            if user.validCommand(Transaction.DELETE):
                eventName = raw_input("Enter event name: ")
                if eventName.strip() in currentEvents.events: # event name valid
                    dailyTransactions.addTransaction(Transaction(eventName, Transaction.DELETE))  # delete ticket
                    currentEvents.removeEvent(eventName)
                else:
                    print "Error: Event name entered is invalid"
            else:
                print "throw error"  # permissions error
        else:
            print "throw error"  # invalid command


# Write transactions to file #
dailyTransactions.toFile("transactions.txt")  # write output file

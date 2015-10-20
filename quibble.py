# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


from lib.Event import Event
from lib.QuibbleError import QuibbleError
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
    try:

        command = raw_input().strip()

        if user is None:  # User hasn't logged in yet
            if command == "login":
                command = raw_input().strip()
                if command == "sales":
                    user = User(False)
                elif command == "admin":
                    user = User(True)
                else:
                    raise QuibbleError("an error occured")  # only sales or admin allowed
            else:
                raise QuibbleError("an error occured")  # only login command allowed
        else:
            if command == "logout":
                programloop=False
                break

            elif command == "sell":
                if user.validCommand(Transaction.SELL):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events: # event name valid
                        numTickets = int(raw_input("Enter num tickets: "))
                        if (not user.admin and numTickets <= 8) or ( numTickets <= currentEvents.getEvent(eventName).numTickets): # numtickets valid
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.SELL))  # sell ticket
                        else:
                            raise QuibbleError("Error: Num tickets is invalid")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            elif command == "return":
                if user.validCommand(Transaction.RETURN):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events: # event name valid
                        numTickets = int(raw_input("Enter num tickets: "))
                        if (not user.admin and numTickets <= 8) or (numTickets <= currentEvents.getEvent(eventName).numTickets): # numtickets valid
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.RETURN))  # Return ticket
                        else:
                            raise QuibbleError("Error: Num tickets is invalid")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                        raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            elif command == "create":
                if user.validCommand(Transaction.CREATE):
                    eventName = raw_input("Enter event name: ")
                    if not eventName.strip() in currentEvents.events and len(eventName)<=20: # event name valid
                        date = raw_input("Enter date (YYMMDD): ")
                        if Transaction.validDate(date): # date is valid
                            numTickets = int(raw_input("Enter num tickets: "))
                            if numTickets <= 99999:
                                dailyTransactions.addTransaction(Transaction(eventName, Transaction.CREATE,date,numTickets))  # create ticket
                            else:
                                raise QuibbleError("Error: Number cannot be greater than 99999")
                        else:
                            raise QuibbleError("Error: Input is invalid")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                        raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            elif command == "add":
                if user.validCommand(Transaction.ADD):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events: # event name valid
                        numTickets = int(raw_input("Enter num tickets: "))
                        if numTickets <= 99999:
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.ADD))  # add ticket
                        else:
                            raise QuibbleError("Error: Number cannot be greater than 99999")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                        raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            elif command == "delete":
                if user.validCommand(Transaction.DELETE):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events: # event name valid
                        dailyTransactions.addTransaction(Transaction(eventName, Transaction.DELETE))  # delete ticket
                        currentEvents.removeEvent(eventName)
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # permissions error
            else:
                raise QuibbleError("Error: Input is invalid")  # invalid command

    except QuibbleError as e:
        print e.value
        programloop = False
        break


# Write transactions to file #
dailyTransactions.toFile("transactions.txt")  # write output file

# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


# Helper Object Classes #

from lib.Event import Event
from lib.QuibbleError import QuibbleError
from lib.CurrentEvents import CurrentEvents
from lib.Transaction import Transaction
from lib.DailyTransactions import DailyTransactions
from lib.User import User

# Initialize Program #

programloop = True

currentEvents = CurrentEvents()
currentEvents.fromFile("test_currentEventsFile.txt") # Read in current events

dailyTransactions = DailyTransactions()

user = None


# Main Program Loop #
# The main program loop is in charge of verifying user input. Loop with terminate on error or when user ends session.

while programloop:
    try:

        command = raw_input().strip()

        if user is None: # User hasn't logged in yet
            if command == "login":
                command = raw_input().strip()
                if command == "sales":
                    user = User(False)
                elif command == "admin":
                    user = User(True)
                else:
                    raise QuibbleError("Error: an error occured") # Only sales or admin allowed
            else:
                raise QuibbleError("Error: an error occured") # Only login command allowed
        else:
            if command == "logout":
                programloop=False
                break

            # process sell command
            elif command == "sell":
                if user.validCommand(Transaction.SELL):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events: # Event name valid
                        numTickets = int(raw_input("Enter num tickets: "))  # Enter number of tickets
                        if (not user.admin and numTickets <= 8) or (numTickets <= currentEvents.getEvent(eventName).numTickets):  # Numtickets valid
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.SELL, numTickets)) # Sell ticket
                        else:
                            raise QuibbleError("Error: Num tickets is invalid") # Invalid ticket number
                    else:
                        raise QuibbleError("Error: Event name entered is invalid") # Invalid event
                else:
                    raise QuibbleError("Error: User does not have permission for this action") # Permissions error

            # process return command
            elif command == "return":
                if user.validCommand(Transaction.RETURN):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events: # Event name valid
                        numTickets = int(raw_input("Enter num tickets: ")) # Enter number of tickets
                        if (not user.admin and numTickets <= 8) or (numTickets <= currentEvents.getEvent(eventName).numTickets):  # numtickets valid
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.RETURN,numTickets))  # Return ticket
                        else:
                            raise QuibbleError("Error: Num tickets is invalid")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            # process create command
            elif command == "create":
                if user.validCommand(Transaction.CREATE):
                    eventName = raw_input("Enter event name: ")
                    if not eventName.strip() in currentEvents.events and len(eventName) <= 20:  # event name valid
                        date = raw_input("Enter date (YYMMDD): ")
                        if Transaction.validDate(date):  # date is valid
                            numTickets = int(raw_input("Enter num tickets: "))  # Enter number of tickets
                            if numTickets <= 99999:
                                dailyTransactions.addTransaction(Transaction(eventName, Transaction.CREATE,numTickets,date))  # create ticket
                            else:
                                raise QuibbleError("Error: Number cannot be greater than 99999")
                        else:
                            raise QuibbleError("Error: Input is invalid")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                    raise QuibbleError("Error: User does not have permission for this action") # Permissions error

            # process add command
            elif command == "add":
                if user.validCommand(Transaction.ADD):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events:  # Event name valid
                        numTickets = int(raw_input("Enter num tickets: "))
                        if numTickets <= 99999:
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.ADD,numTickets))  # Add ticket
                        else:
                            raise QuibbleError("Error: Number cannot be greater than 99999")  # Invalid number of tickets
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")  # Invalid event name
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            # process delete command
            elif command == "delete":
                if user.validCommand(Transaction.DELETE):
                    eventName = raw_input("Enter event name: ")
                    if eventName.strip() in currentEvents.events:  # Event name valid
                        dailyTransactions.addTransaction(Transaction(eventName, Transaction.DELETE))  # delete ticket
                        currentEvents.removeEvent(eventName)
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")  # Invalid event
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # Permissions error
            else:
                raise QuibbleError("Error: Input is invalid")  # Invalid command

    except QuibbleError as e:  # catch program error
        print e.value
        programloop = False  # quit program
        break


# Write transactions to file #

dailyTransactions.toFile("transactions.txt")  # write output file

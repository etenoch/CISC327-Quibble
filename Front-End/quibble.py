# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

from lib.QuibbleError import QuibbleError
from lib.CurrentEvents import CurrentEvents
from lib.Transaction import Transaction
from lib.DailyTransactions import DailyTransactions
from lib.User import User

import sys

# Initialize Program #
cmd_arguments = sys.argv
programloop = True

currentEvents = CurrentEvents()
currentEvents.fromFile(cmd_arguments[1])  # Read in current events

dailyTransactions = DailyTransactions()

user = None


# Main Program Loop #
# The main program loop is in charge of verifying user input. Loop with terminate on error or when user ends session.

while programloop:
    try:

        command = raw_input().strip()

        if user is None:  # User hasn't logged in yet
            if command == "logout":
                raise QuibbleError("Error: You are not logged in")
            if command == "login":
                command = raw_input().strip()
                if command == "sales":
                    user = User(False)
                elif command == "admin":
                    user = User(True)
                elif command == "logout":
                    programloop = False
                    break
                elif command == "login":
                    raise QuibbleError("Error: user is already logged in")
                elif not command:
                    raise QuibbleError("Error: No input entered")
                else:
                    raise QuibbleError("Error: Input is Invalid")  # Only sales or admin allowed
            elif not command:
                raise QuibbleError("Error: No input entered")
            else:
                raise QuibbleError("Error: Input is Invalid")  # Only login command allowed
        else:
            if command == "login":
                raise QuibbleError("Error: user is already logged in")
            elif command == "logout":
                programloop = False
                break
            elif not command:
                raise QuibbleError("Error: No input entered")

            # process sell command
            elif command == "sell":
                if user.validCommand(Transaction.SELL):
                    eventName = raw_input("Enter event name: \n")
                    if eventName.strip() in currentEvents.events: # Event name valid
                        raw = raw_input("Enter num tickets: \n")
                        numTickets = int(raw)  # Enter number of tickets
                        if (numTickets>=1) and ( (not user.admin and numTickets <= 8) or (user.admin and numTickets <= currentEvents.getEvent(eventName).numTickets) ):  # Numtickets valid
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
                    eventName = raw_input("Enter event name: \n")
                    if eventName.strip() in currentEvents.events: # Event name valid
                        numTickets = int(raw_input("Enter num tickets: \n")) # Enter number of tickets
                        theNumTickets = currentEvents.getEvent(eventName).numTickets if currentEvents.getEvent(eventName) else 0
                        if (numTickets >= 1) and ((not user.admin and numTickets <= 8) or (user.admin and numTickets <= 99999 - theNumTickets)):  # numtickets valid
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
                    eventName = raw_input("Enter event name: \n").strip()
                    if not eventName:
                        raise QuibbleError("Error: No input entered")
                    if not eventName in currentEvents.events and len(eventName) <= 20:  # event name valid
                        date = raw_input("Enter date (YYMMDD): \n").strip()
                        if not date:
                            raise QuibbleError("Error: No input entered")
                        if Transaction.validDate(date):  # date is valid
                            numTickets = int(raw_input("Enter num tickets: \n"))  # Enter number of tickets
                            if numTickets <= 99999 and numTickets > 0:
                                dailyTransactions.addTransaction(Transaction(eventName, Transaction.CREATE,numTickets,date))  # create ticket
                            else:
                                raise QuibbleError("Error: Number is invalid")
                        else:
                            raise QuibbleError("Error: Input is invalid")
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")
                else:
                    raise QuibbleError("Error: User does not have permission for this action") # Permissions error

            # process add command
            elif command == "add":
                if user.validCommand(Transaction.ADD):
                    eventName = raw_input("Enter event name: \n")
                    if eventName.strip() in currentEvents.events:  # Event name valid
                        numTickets = int(raw_input("Enter num tickets: \n"))
                        if numTickets>=1 and numTickets <= 99999:
                            dailyTransactions.addTransaction(Transaction(eventName, Transaction.ADD,numTickets))  # Add ticket
                        else:
                            raise QuibbleError("Error: Number is invalid")  # Invalid number of tickets
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")  # Invalid event name
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # permissions error

            # process delete command
            elif command == "delete":
                if user.validCommand(Transaction.DELETE):
                    eventName = raw_input("Enter event name: \n")
                    if eventName.strip() in currentEvents.events:  # Event name valid
                        dailyTransactions.addTransaction(Transaction(eventName, Transaction.DELETE))  # delete ticket
                        currentEvents.removeEvent(eventName)
                    else:
                        raise QuibbleError("Error: Event name entered is invalid")  # Invalid event
                else:
                    raise QuibbleError("Error: User does not have permission for this action")  # Permissions error
            else:
                raise QuibbleError("Error: Input is invalid")  # Invalid command

    except EOFError as e:
        print "Error: Input is invalid"
        programloop = False  # quit program
        break
    except ValueError as e:  # cannot parse as int
        print "Error: Input is invalid"
        programloop = False
        break
    except QuibbleError as e:  # catch program error
        print e.value
        programloop = False
        break


# Write transactions to file #

dailyTransactions.toFile(cmd_arguments[2])  # write output file

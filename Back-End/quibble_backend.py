# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The quibble_backend is responsible for keeping track of the current files in use.
# It imports it data from the MasterEventsFile, DailyTransactions and Transaction classes.

from lib.MasterEventsFile import *
from lib.DailyTransactions import *

import sys

cmd_arguments = sys.argv

# init
previousMasterEventsFile = cmd_arguments[1]
newMasterEventsFile = cmd_arguments[3]
newCurrentEventsFile = cmd_arguments[4]
transactionFiles = [cmd_arguments[2]]

masterEvents = MasterEventsFile()
masterEvents.fromFile(previousMasterEventsFile)

# process each file and transaction
for file in transactionFiles:
    transactionFile = DailyTransactions()
    transactionFile.fromFile(file)

    for t in transactionFile.transactions:
        masterEvents.processTransaction(t)


# write out result files
masterEvents.createCurrentEventsFile(newCurrentEventsFile)
masterEvents.toFile(newMasterEventsFile)

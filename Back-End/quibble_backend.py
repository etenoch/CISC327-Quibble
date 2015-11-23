# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The quibble_backend is responsible for keeping track of the current files in use.
# It imports it data from the MasterEventsFile, DailyTransactions and Transaction classes.

from lib.MasterEventsFile import *
from lib.DailyTransactions import *
from lib.Transaction import *

# init
previousMasterEventsFile = "test_old_master_file.txt"
newMasterEventsFile = "test_new_master_file.txt"
newCurrentEventsFile = "test_new_currentEvents_file.txt"
transactionFiles = ["transactions1.txt", "transactions2.txt"]

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

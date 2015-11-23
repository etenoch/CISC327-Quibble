# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The quibble_backend is responsible for keeping track of the current files in use.
# It imports it data from the MasterEventsFile, DailyTransactions and Transaction classes.

from lib.MasterEventsFile import *
from lib.DailyTransactions import *
from lib.Transaction import *; from testing import *; clearTestLog()

# init
logBranch(1,"quibble_backend",14); previousMasterEventsFile = "test_create_old_master_file.txt"
newMasterEventsFile = "test_create_new_master_file.txt"
newCurrentEventsFile = "test_create_currenteventsfile.txt"
transactionFiles = ["test_create_dailytransactions.txt"]

masterEvents = MasterEventsFile()
masterEvents.fromFile(previousMasterEventsFile)

# process each file and transaction
for file in transactionFiles:
    logBranch(4,"quibble_backend",24); transactionFile = DailyTransactions()
    transactionFile.fromFile(file)

    for t in transactionFile.transactions:
        logBranch(7,"quibble_backend",28); masterEvents.processTransaction(t)


# write out result files
logBranch(12,"quibble_backend",32); masterEvents.createCurrentEventsFile(newCurrentEventsFile)
masterEvents.toFile(newMasterEventsFile)

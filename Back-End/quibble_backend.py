# CISC327 Quibble - Back End
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

from lib.MasterEventsFile import *
from lib.DailyTransactions import *
from lib.Transaction import *

# init
previousMasterEventsFile = "test_old_master_file.txt"
newMasterEventsFile = "test_new_master_file.txt"
newCurrentEventsFile = "test_new_currentEvents_file.txt"
transactionFiles = ["transaction1.txt", "transaction2.txt"]

masterEvents = MasterEventsFile().fromFile(previousMasterEventsFile)

# process each file and transaction
for file in transactionFiles:
    transactionFile = DailyTransactions().fromFile(file)

    for t in transactionFile.transactions:
        masterEvents.processTransaction(t)


# write out result files
masterEvents.createCurrentEventsFile(newCurrentEventsFile)
masterEvents.toFile(newMasterEventsFile)

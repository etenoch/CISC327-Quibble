# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The daily testing script assumes Day 1 as a default entry.
# The script reads in reads the current Event File (txt) and the current Master Event File (txt).
# A temporary file is then made which holds the the processed transcations as the program cycles through the Event Files.
# Once complete the content of the temporary file is ran, which will result into a newly generated Master File for the current day.

import sys
import os
import os.path

# python scripts used for the front and backend
front_end_code = "code_front_final/quibble.py"
back_end_code = "code_back_final/quibble_backend.py"

# assume day_1 as already exsisting (default)
base_path = "day_1/"

# locations of files are retrived according to the base path
old_master_events_file = base_path+"inputs/master_events_file.txt"
old_current_events_file = base_path+"inputs/current_events_file.txt"

temp_transactions_file = base_path+"temp_transactions_file.txt"
merged_transactions_file = base_path+"merged_transactions_file.txt"

new_master_events_file = base_path+"outputs/master_events_file.txt"
new_current_events_file = base_path+"outputs/current_events_file.txt"

transactions = ["transaction_1.txt","transaction_2.txt","transaction_3.txt","transaction_4.txt"]

if len(sys.argv)>1: # called from weekly script
	cmd_arguments = sys.argv
	day = cmd_arguments[1]
	inputs = cmd_arguments[2]
	outputs = cmd_arguments[3]
	transactions = cmd_arguments[4:]

	base_path = day+"/"
	old_master_events_file = inputs+"/master_events_file.txt"
	old_current_events_file = inputs+"/current_events_file.txt"

	temp_transactions_file = base_path+"temp_transactions_file.txt"
	merged_transactions_file = base_path+"merged_transactions_file.txt"

	new_master_events_file = outputs+"/master_events_file.txt"
	new_current_events_file = outputs+"/current_events_file.txt"

# allow for file to be written to
open(merged_transactions_file,"w").close()

# run frontend cases
for case in transactions:

	# run frontend code
	os.system("python "+front_end_code+" "+old_current_events_file+" "+temp_transactions_file +" < "+base_path+case)

	lines = open(temp_transactions_file).readlines()
	if lines[-1][:2]=="00": # remove last line if 00
		lines = lines[:-1]	

	mergedFile = open(merged_transactions_file,"a")
	for item in lines:
			mergedFile.write("%s" % item)
	mergedFile.close()

# run backend
os.system("python "+back_end_code+" "+old_master_events_file+" "+merged_transactions_file+" "+new_master_events_file+" "+new_current_events_file)


# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)


import sys
import os

front_end_code = "code_front_final/quibble.py"
back_end_code = "code_backend_final/quibble_backend.py"

# defualt
base_path = "day_1/"

old_master_events_file = base_path+"inputs/master_events_file.txt"
old_current_events_file = base_path+"inputs/current_events_file.txt"

temp_transactions_file = base_path+"temp_transactions_file.txt"
merged_transactions_file = base_path+"merged_transactions_file.txt"

new_master_events_file = base_path+"outputs/master_events_file.txt"
new_current_events_file = base_path+"outputs/current_events_file.txt"

if len(sys.argv)>1: # called from weekly script
	cmd_arguments = sys.argv
	day = cmd_arguments[1]
	inputs = cmd_arguments[2]
	outputs = cmd_arguments[3]
	cases = cmd_arguments[4:]

	base_path = day+"/"
	old_master_events_file = inputs+"/master_events_file.txt"
	old_current_events_file = inputs+"/current_events_file.txt"

	temp_transactions_file = base_path+"temp_transactions_file.txt"
	merged_transactions_file = base_path+"merged_transactions_file.txt"

	new_master_events_file = outputs+"/master_events_file.txt"
	new_current_events_file = outputs+"/current_events_file.txt"

# run frontend cases
for case in ["case1","case2","case3","case4"]:

	# run frontend code
	os.system(front_end_code+" "+old_current_events_file+" "+temp_transactions_file)

	lines = open(temp_transactions_file).readlines()
	if lines[-1][:2]=="00": # remove last line if 00
		lines = lines[:-1]	

	mergedFile = open(merged_transactions_file,"a")
	for item in lines:
			mergedFile.write("%s\n" % item)


	# run backend
os.system(back_end_code+" "+old_master_events_file+" "+new_master_events_file+" "+new_current_events_file+" "+merged_transactions_file)



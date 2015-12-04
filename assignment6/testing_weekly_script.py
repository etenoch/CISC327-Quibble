# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

import os

daily_testing_script = "testing_daily_script.py"

days = [
		{
			'day':"day_1", 
			'transactions':["transaction_1.txt","transaction_2.txt","transaction_3.txt","transaction_4.txt"],
			'inputs':"day_1/inputs",
			'outputs':"day_1/outputs"
		},
		{
			'day':"day_2",	
			'transactions':["transaction_1.txt","transaction_2.txt"],
			'inputs':"day_1/outputs",
			'outputs':"day_2/outputs"
		},
		{
			'day':"day_3",	
			'transactions':["transaction_1.txt","transaction_2.txt"],
			'inputs':"day_2/outputs",
			'outputs':"day_3/outputs"
		},
		{
			'day':"day_3",	
			'transactions':["transaction_1.txt","transaction_2.txt"],
			'inputs':"day_2/outputs",
			'outputs':"day_3/outputs"
		},
		{
			'day':"day_4",	
			'transactions':["transaction_1.txt","transaction_2.txt"],
			'inputs':"day_3/outputs",
			'outputs':"day_4/outputs"
		},
		{
			'day':"day_5",	
			'transactions':["transaction_1.txt","transaction_2.txt"],
			'inputs':"day_4/outputs",
			'outputs':"day_5/outputs"
		}
	]


for d in days:
	os.system("python "+daily_testing_script+" "+d['day']+" "+d['inputs']+" "+d['outputs']+" "+" ".join(d['transactions']))

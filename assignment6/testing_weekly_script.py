# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

import os

daily_testing_script = "testing_daily_script.py"

days = [
		{
			'day':"day_1", 
			'cases':["case1","case2","case3","case4"]
			'inputs':"day_1/inputs",
			'outputs':"day_1/outputs"
		},
		{
			'day':"day_2",	
			'cases':["case1","case2"]
			'inputs':"day_1/outputs",
			'outputs':"day_2/outputs"
		},
		{
			'day':"day_3",	
			'cases':["case1","case2"]
			'inputs':"day_2/outputs",
			'outputs':"day_3/outputs"
		},
		{
			'day':"day_3",	
			'cases':["case1","case2"]
			'inputs':"day_2/outputs",
			'outputs':"day_3/outputs"
		},
		{
			'day':"day_4",	
			'cases':["case1","case2"]
			'inputs':"day_3/outputs",
			'outputs':"day_4/outputs"
		},
		{
			'day':"day_5",	
			'cases':["case1","case2"]
			'inputs':"day_4/outputs",
			'outputs':"day_5/outputs"
		}
	]


for d in days:
	os.system(daily_testing_script+" "+d['day']+" "+d['inputs']+" "+d['ouptuts']+" "+" ".join(d['cases']))

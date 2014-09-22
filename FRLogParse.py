# Import RegEx & CSV

import re
import csv

## Open the file with read only permit
f = open('FRLogging.log')

## Read the first line 
line = f.readline()


## Setup the Output & Create a Header
c = csv.writer(open("output.txt", "wb"), delimiter='|')
c.writerow(["Elapsed", "User", "Start", "Report"])

## If the file is not empty keep reading line one at a time
## till the file is empty

while line:
	my_text = line

## Only process endJobSummary lines that have a valid report name.
	if ("endJobSummary" in my_text) and ("Name:" in my_text):
	
## Breakout the line into a list of each [] formatted paramater.	
	  my_list = re.findall("\[(.*?)\]", my_text)
  
## Parse the list into the paramaters we care about.
	  for i in range (1,18):
		if "APP:" in my_list[i]:
			my_app = my_list[i].split (":")[1]
			i = i+1
		elif "userId:" in my_list[i]:
			my_user = my_list[i].split (":")[1]
			i = i+1
		elif "Elapsed:" in my_list[i]:
			my_elapsed = my_list[i].split (":")[1]
			i = i+1
## Only take the date portion of the start time
		elif "Start:" in my_list[i]:
			my_start = (my_list[i].split (" ")[0])[6:]
			i = i+1
		elif "Name:" in my_list[i]:
			my_rept = my_list[i].split (":")[1]
			i = i+1

## Output the parsed log line to the file.

	  c.writerow([my_elapsed, my_user, my_start, my_rept])

	  line = f.readline ()
	else:
	  line = f.readline()

f.close()
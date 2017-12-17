# Week 3 
# Name: Paulien Tensen
# Student number: 10811559
# Course: Data processing
#
# This program gives a JSONfile as output.

import json
import csv 

# Open KNMI csv.
csvfile = open("stations.csv", 'r')
print ("hoi")
# Set fieldnames. 
fieldnames =("date", "neerslag")

# Open json file.
jsonfile = open('filess.json', 'w')

# Make empty list.
data = [];

# Read csv as dictionary. 
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
	
	# Append rows to list.
	data.append(row)

# Dump json data in jsonfile.
json.dump(data, jsonfile, indent=4)	
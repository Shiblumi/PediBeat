#can we use stacks for FILO? (first in, last out)


#CSV file is sorted in the following:
#Time of Diagnosis,Heartbeat (bpm),Temperature (°C)


import csv


# Define the file path
records = 'sampleData.csv'


# Open the CSV file for reading
with open(records, 'r', newline='') as file:
record = csv.reader=(file)
# Iterate through each row in the CSV
for iteration in record:
# Each row is a list of values
print(iteration)




import csv

with open("students.csv") as csv_file: 
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            pass
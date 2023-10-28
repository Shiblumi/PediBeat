import csv

class data_stream:
    def __init__(self, csv_file=''):
        self.csv_file = csv_file
        
    def attach(self, csv_file):
        """
        Attach instance of data_stream to a csv file.

        Args:
            csv_file (string): Path to csv file to attach.

        Returns:
            type: Description of the return value.
        """
        with open("students.csv") as csv_file: 
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    pass
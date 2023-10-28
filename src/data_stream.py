import csv

class data_stream:
    
    def __init__(self, csv_file_path=''):
        self.buffer1 = []
        self.buffer2 = []
        self.buffer3 = []
        
        if (~csv_file_path):
            self.csv_file_obj = None
        else:
            self.csv_file_obj = self.attach(csv_file_path)
            
        
    def attach(self, csv_file_path):
        """
        Attach instance of data_stream to a csv file.

        Args:
            csv_file (string): Path to csv file to attach.

        Returns:
            None
        """
        file = open(csv_file_path)
        self.csv_file_obj = csv.DictReader(file)
    
    
    def detach(self):
        self.csv_file_obj.close()
        
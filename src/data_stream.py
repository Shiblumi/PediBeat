import csv
import buffer as bf

class data_stream:
    
    # To-Do?: Add func to add/remove more buffers after instantiation.
    def __init__(self, csv_file_path='', *args):
        """
        Example of data_stream with 3 buffers: Buffer(path, 10, 20, 30)
        """
        self.buffers = []
        for arg in args:
            self.buffers.append(bf.Buffer(max_size=arg))
            
        self.csv_file_obj = None
        self.csv_DictReader = None
        self.csv_DictWriter = None
        if (csv_file_path):
            self.attach(csv_file_path)
        
            
    def attach(self, csv_file_path):
        """
        Attach instance of data_stream to a csv file.

        Args:
            csv_file (string): Path to csv file to attach.

        Returns:
            None
        """
        if (csv_file_path != ''):
            self.detach()
        self.csv_file_obj = open(csv_file_path)
        self.csv_DictReader = csv.DictReader(self.csv_file_obj, 'r')
        self.csv_DictWriter = csv.DictWriter(self.csv_file_obj, 'w')
    
    
    def detach(self):
        """
        Detach instance of data_stream from csv file and close csv file.

        Args:
            None

        Returns:
            None
        """
        if self.csv_file_obj is not None:
            self.csv_file_obj.close()
            self.csv_file_obj = None
        else: 
            print("No csv file attached.")
             
        if self.csv_DictReader is not None:
            self.csv_DictReader.close()
            self.csv_DictReader = None
            
        if self.csv_DictWriter is not None:
            self.csv_DictWriter.close()
            self.csv_DictWriter = None  
        
        
    def feed_buffers(self, vals):
        if len(vals) != len(self.buffers):
            print("Error: Number of values does not match number of buffers.")
            exit()
            
        for buffer, val in zip(self.buffers, vals):
            if buffer.is_full():
                buffer.pop(0)
            buffer.append(val)
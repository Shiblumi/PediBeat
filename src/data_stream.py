import csv
import buffer as bf

# For use to interface and stream data from sensors.
class DataStream:
    
    # To-Do?: Add func to add/remove more buffers after instantiation.
    def __init__(self, csv_file_path = None, *args):
        """
        Example of data_stream with 3 buffers: Buffer(path, 10, 20, 30)
        """
        self.buffers = []
        for arg in args:
            self.buffers.append(bf.Buffer(max_size=arg))
            
        self.csv_file_obj = None
        self.csv_DictReader = None
        self.csv_DictWriter = None
        
        if csv_file_path:
            print("Trying to attach")
            self.attach_csv(csv_file_path)
        
            
    def attach_csv(self, csv_file_path):
        """
        Attach instance of data_stream to a csv file.

        Args:
            csv_file (string): Path to csv file to attach.

        Returns:
            None
        """
        if (csv_file_path != ''):
            self.detach_csv()
        self.csv_file_obj = open(csv_file_path)
        self.csv_DictReader = csv.DictReader(self.csv_file_obj, 'r')
        self.csv_DictWriter = csv.DictWriter(self.csv_file_obj, 'w')
    
    
    def detach_csv(self):
        """
        Detach instance of data_stream from csv file and close csv file.
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
            
        
    def append_to_csv(self):
        pass
        
        
    def feed_buffers(self, *args):
        """
        Update each buffer with corresponding value from args.

        Args:
            Tuple of values to feed into buffers.

        Returns:
            None
        """
        if len(args) != len(self.buffers):
            print("Error: Number of values does not match number of buffers.")
            exit()
            
        for buffer, arg in zip(self.buffers, args):
            if buffer.is_full():
                buffer.buffer.pop(0)
            buffer.buffer.append(arg)  


    def flush_all(self):
        """
        Empty all buffers.
        """
        for buffer in self.buffers:
            buffer.clear()
            
            
    def display(self):
        """
        Display current contents of all buffers.
        """
        for bf in self.buffers:
            print(bf.buffer)
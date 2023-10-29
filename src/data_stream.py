import csv
import buffer as bf

# For use to interface and stream data from sensors.
class DataStream:
    
    # To-Do?: Add func to add/remove more buffers after instantiation.
    def __init__(self, *buffer_maximums, csv_file_path=None):
        """
        Example of data_stream with 3 buffers: Buffer(path, 10, 20, 30)
        """
        self.buffers = []
        for max in buffer_maximums:
            self.buffers.append(bf.Buffer(max_size=max))
        
        self.csv_file_path = csv_file_path
        self.file_obj_r = None
        self.file_obj_w = None
        self.csv_reader = None
        self.csv_writer = None
        
        if csv_file_path:
            print("Trying to attach")
            self.attach_csv(csv_file_path)
            
        self.counter = 0
        
            
    def attach_csv(self, csv_file_path):
        """
        Attach instance of data_stream to a csv file.

        Args:
            csv_file (string): Path to csv file to attach.

        Returns:
            None
        """
        if self.file_obj_r != None or self.file_obj_w != None:
            self.detach_csv()
        self.file_obj_r = open(csv_file_path, 'r', newline='')
        self.file_obj_w = open(csv_file_path, 'a', newline='')
        self.csv_reader = csv.reader(self.file_obj_r)
        self.csv_writer = csv.writer(self.file_obj_w)
        
        print("Printing csv file: ")
        for row in self.csv_reader:
            print(row)

    
    def detach_csv(self):
        """
        Detach instance of data_stream from csv file and close csv file.
        """
        if self.file_obj_r is not None:
            self.file_obj_r.close()
            self.file_obj_r = None
        else: 
            print("No csv file attached.")
        if self.file_obj_w is not None:
            self.file_obj_w.close()
            self.file_obj_w = None
        else: 
            print("No csv file attached.")
             
        if self.csv_reader is not None:
            self.csv_reader.close()
            self.csv_reader = None
            
        if self.csv_writer is not None:
            self.csv_writer.close()
            self.csv_writer = None

    
    def initialize_csv(self, *col_names):
        # Make it so that multiple csv's can be made (filename conflict)
        self.csv_file_path = "./data/test_1.csv"
        self.file_obj_w = open("./data/test_1.csv", 'w', newline='')
        self.file_obj_r = open("./data/test_1.csv", 'r', newline='')
        self.csv_reader = csv.reader(self.file_obj_r)
        self.csv_writer = csv.writer(self.file_obj_w)
        self.csv_writer.writerow(col_names)
        print('csv initialized')
        
        
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
            buffer.add(arg)
            
        self.buffer_spill_to_csv()
            
            
    def buffer_spill_to_csv(self):
        """
        Store oldest data from each buffer into csv file.
        """
        row = []
        for buffer in self.buffers:
            if buffer.is_full():
                row.append(buffer.buffer[0])
            else:
                row.append(None) # Converts to empty string on csv
        self.csv_writer.writerow(row)


    def flush_buffers(self):
        """
        Empty all buffers.
        """
        for buffer in self.buffers:
            buffer.clear()
            
            
    def flush_buffers_to_csv(self):
        """
        Store all buffers onto csv and empty all buffers.
        """
        row = []
        go_next = True
        while go_next:
            go_next = False
            for buffer in self.buffers:
                if len(buffer) == 0:
                    row.append(None)
                else:
                    row.append(buffer[0])
                    go_next = True
                buffer.pop(0)
            self.csv_writer.writerow(row)
            row.clear()


    def display(self):
        """
        Display current contents of all buffers.
        """
        for bf in self.buffers:
            print(bf.buffer)
class Buffer:
    def __init__(self, max_size=10):
        self.buffer = []
        self.max_size = max_size
        
        
    def is_full(self):
        return len(self.buffer) >= self.max_size


    def add(self, data):
        if self.is_full():
            self.buffer.pop(0)
        self.buffer.append(data)
        
    
    def pop(self, key):
        if len(self.buffer) == 0:
            return None
        return self.buffer.pop(key)
    
        
    def __len__(self):
        return len(self.buffer)
    
    
    def __getitem__(self, key):
        return self.buffer[key]
        
    
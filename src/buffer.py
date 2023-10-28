class Buffer:
    def __init__(self, max_size=10):
        self.buffer = []
        self.max_size = max_size
        
    def is_full(self):
        return len(self.buffer) == self.max_size
    
    def is_overfull(self):
        return len(self.buffer) > self.max_size
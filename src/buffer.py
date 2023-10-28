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
        
    
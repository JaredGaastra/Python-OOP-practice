"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    

    def __init__(self, num):
        """create a staring num"""
        self.num = num
        self.start = num

    __repr__

    def start(self):
        """Begins the serial generator at 100 and will come back to 100 when reset"""
        
        return self.num 
    
    def generate(self):
        """generates a new serial number incrementing by 1"""
        self.num += 1
        return self.num
        
        

    def reset(self):
        """Resets the serial back to original serial num"""
        self.num = self.start - 1
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
    def __init__ (self, start=0):
        """Initialize the generator"""

        self.start = self.next = start

    def generate(self):
        """Add one to the number provided"""
        
        self.next += 1
        return self.next
    
    def reset(self):
        """Reset number to value provided"""

        self.next = self.start

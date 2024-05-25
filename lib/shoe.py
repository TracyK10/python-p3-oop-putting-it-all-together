#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = 'Used'
        
    @property
    def int_size(self):
        return self._size
    
    @int_size.setter
    def int_size(self, size):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        else:
            self._size = size
            
    def can_cobble():
        print("Your shoe is as good as new!")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
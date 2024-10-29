class Shoe:
    def __init__(self, brand, size, color="Unknown"): 
        self.brand = brand
        self.size = size  
        self.color = color
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = "New" 
        print("Your shoe is as good as new!")  
class Move:
    
    def __init__(self, value:int) -> None:
        self._value = value # We made the value non-public, only read value
        
    @property
    def value(self):
        return self._value # Used to access the only read value
        
    def is_valid(self):
        return 1 <= self._value <= 9 # Check if the value is valid
    
    
    def get_row(self):
        if self._value in (1, 2, 3):
            return 0 # Firs row on the board
        
        elif self._value in (4, 5, 6):
            return 1 # Second row on the board
        
        else:
            return 2 # Third row on the boeard
    
    def get_column(self):
        if self._value in (1, 4, 7):
            return 0 # Firs column on the board
        
        elif self._value in (2, 5, 8):
            return 1 # Second column on the board
        
        else:
            return 2 # Third column on the boeard
        

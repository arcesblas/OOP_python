import random # it is recomend import first built-in fuctions

from move import Move # We can create now Move pbjects


class Player:
    
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"
    
    def __init__(self, is_human=True) -> None:
        self._is_human = is_human # Default player is human
        
        if is_human:
            self._marker = Player.PLAYER_MARKER # We use this constant because is easy to maintain, in case we want to change the marker 
        else:
            self._marker = Player.COMPUTER_MARKER
        
    @property
    def is_human(self):
        return self._is_human
    
    @property
    def marker(self):
        return self._marker
    
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True: # Infinite loop until we put a valid value
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input) # We create a move object with the value that the user put
            if move.is_valid(): # Check if the value is valid 
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move
    
    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move
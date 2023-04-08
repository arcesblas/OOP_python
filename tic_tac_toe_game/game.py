from board import Board
from player import Player


class Game:
    
    def start(self):
        print("***********************")
        print("Welcome to Tic-Tac-Toe ")
        print("***********************")
        
        board = Board()
        player = Player()
        computer = Player(False)
        
        
        # Ask the usar if he/she would like to
        # play another round.
        
        while True: # Game
            board.print_board()
            # Get move, check tie, check game over
            while True: # Round
                
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()
                
                if board.check_is_tie():
                    print("It's a tie! 😳 Try again.")
                    break
                    
                elif board.check_is_game_over_(player, player_move):
                    print("Awesome. You won the game! 🎉")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()
                    
                    if board.check_is_game_over_(computer, computer_move):
                        print("Oops... 😱 The computer won.")
                        break
                    
            play_again = input("Would you like to play again? Enter X for Yes or O for NO: ").upper()
            
            if play_again == "O":
                print("Bye! Come back soon 👋")
                break
            
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Yor input was not valid but I will assume that you want to play again. 💡")
                self.start_new_round(board)
                
    def start_new_round(self, board):
        print("***********************")
        print("       New Round       ")
        print("***********************")
        board.reset_board()
        board.print_board() 
        
game = Game()
game.start()                 
    
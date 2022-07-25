import numpy as np

class Player:
    def __init__(self, name, shape):
        self.shape = shape
        self.name = name

    def get_row_from_input(self):
        while True:
            row = int(input("in what row do you want to put it? (1-3)"))
            if row < 1 or row > 3:
                print("the number must be in range")
            else:
                return row
                break

    def get_col_from_input(self):
        while True:
            col = int(input("in what col do you want to put it? (1-3)"))
            if col < 1 or col > 3:
                print("the number must be in range")
            else:
                return col
                break

class TurnHandler:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def update_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_current_player_shape(self):
        return self.current_player.shape

def is_valid(board,row,col,shape1,shape2):
    while True:
        if board[row,col] == shape1 or board[row,col] == shape2:
            print('sorry this place is already taken please try againe')
        else:
            break



def main():
    ##########################################################
    # ---------- Init variables ---------------------------
    ##########################################################
    board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
    player1 = Player('1', 'X')
    player2 = Player('2', 'O')
    turn_handler = TurnHandler(player1, player2)
    # -------------------------------------------------------

    ##########################################################
    # ---------- Game Loop --------------------------------
    ##########################################################
    run = True
    while run:
        current_player = turn_handler.current_player
        is_valid(board,current_player.get_row_from_input,current_player.get_col_from_input,player1.shape,player2.shape)
        board[current_player.get_col_from_input() - 1, current_player.get_row_from_input() - 1] = current_player.shape
        turn_handler.update_turn()
        print(board)


if __name__ == '__main__':
    main()
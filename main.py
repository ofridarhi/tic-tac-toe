import numpy as np
class Player:
    def __init__(self, name, shape):
        self.shape = shape
        self.name = name

    def get_row_from_input(self):
        while True:
            try:
                row = int(input("in what row do you want to put it? (1-3)"))
                if row < 1 or row > 3:
                    print("the number must be in range")
            except:
                print("input must be a number")
            else:
                return row
                break

    def get_col_from_input(self):
        while True:
            try:
                col = int(input("in what col do you want to put it? (1-3)"))
                if col < 1 or col > 3:
                    print("the number must be in range")
            except:
                print("input must be a number")
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

def get_input(board, current_player, empty_cell):
    while True:
        row = current_player.get_row_from_input() - 1
        col = current_player.get_col_from_input() - 1
        if board[row, col] == empty_cell:
            return row, col

        print('sorry this place is already taken please try againe')

def is_winning(board,current_player):
    for i in range(3):
        #horozontal line and         #horozontal line and
        if board[i,0] == board[i,1] == board[i,2] == current_player.shape or board[0,i] == board[1,i] == board[2,i] == current_player.shape:
            print(f"player{current_player.name}wins")
            return True
    if board[1,1] == board[2,2] == board[0,0] == current_player.shape:
        print(f"player{current_player.name} wins")
        return True
    if board[1,1] == board[0,2] == board[2,0] == current_player.shape:
        print(f"player{current_player.name} wins")
        return True
def main():
    ##########################################################
    # ---------- Init variables ---------------------------
    ##########################################################
    empty_cell = '-'
    board = np.array([[empty_cell, empty_cell, empty_cell], [empty_cell, empty_cell, empty_cell],
                      [empty_cell, empty_cell, empty_cell]])
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
        print(board)
        row, col = get_input(board, current_player, empty_cell)
        board[row,col] = current_player.shape
        if is_winning(board,current_player):
            break
        turn_handler.update_turn()


if __name__ == '__main__':
    main()
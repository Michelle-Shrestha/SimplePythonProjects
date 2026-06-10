from ast import main
import random

class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = row * col
        self.board = [[" _ " for _ in range(self.col)] for _ in range(self.row)]

    def print_board(self):
        for i in range(self.row):
            print("-" * (self.col * 4 + 1))
            for j in range(self.col):
                print("|" + self.board[i][j], end="")
            print("|")
        print("-" * (self.col * 4 + 1))


class Player(Board):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.current_player = " X "
        self.game_running = True
        self.winner = None

    def user_input(self):
        while True:
            try:
                row = int(input("Enter the row number {0} to {1} : ".format(1, self.row))) - 1
                col = int(input("Enter the column number {0} to {1} : ".format(1, self.col))) - 1

                if 0 <= row < self.row and 0 <= col < self.col: 
                    if self.board[row][col] == " _ ":
                        self.board[row][col] = self.current_player
                        break
                    else:
                        print("\nThe cell is already occupied, please select another cell.")
                else:
                    print("\nPlease enter a valid row and column number.")

            except:
                print("\nInvalid Input!!!")

    def switch_player(self):
        if self.current_player == " X ":
            self.current_player = " 0 "
        else:
            self.current_player = " X "

    def check_horizontal_win(self):
        for i in range(self.row):
            if self.board[i][0] == " _ ":
                continue
            win = True
            for j in range(1, self.col):
                if self.board[i][j] != self.board[i][0]:
                    win = False
                    break
            if win:
                self.winner = self.current_player
                return self.winner

    def check_vertical_win(self):
        for i in range(self.col):
            if self.board[0][i] == " _ ":
                continue
            win = True
            for j in range(1, self.row):
                if self.board[j][i] != self.board[0][i]:
                    win = False
                    break
            if win:
                self.winner = self.current_player
                return self.winner

    def check_diagonal_win(self):
        # top left to bottom right
        if self.board[0][0] != " _ ":
            win = True
            for i in range(1, self.row):
                if self.board[i][i] != self.board[0][0]:
                    win = False
                    break
            if win:
                self.winner = self.current_player
                return self.winner

        #top right to bottom left
        d2 = self.board[0][self.col - 1]
        if d2 != " _ ":
            win = True
            for i in range(1, self.row):
                if self.board[i][self.col - 1 - i] != d2:
                    win = False
                    break
            if win:
                self.winner = self.current_player
                return self.winner

    def check_win(self):
        winner = (self.check_horizontal_win() or
                  self.check_vertical_win() or
                  self.check_diagonal_win())

        if winner:
            if winner == " X ":
                print("\nPlayer X won!!!")
            elif winner == " 0 ":
                print("\nPlayer 0 won!!!")
            self.game_running = False

        elif all(self.board[i][j] != " _ "
                 for i in range(self.row)
                 for j in range(self.col)):
            print("\nIt's a draw!")
            self.game_running = False


def Main():
    g1 = Player(4,4)
    g1.print_board()

    while g1.game_running:
        g1.user_input()
        g1.print_board()
        g1.check_win()
        if g1.game_running:     
            g1.switch_player()


Main()
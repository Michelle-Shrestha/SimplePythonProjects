import numpy as np 

class TTT:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.size = self.rows* self.cols
        self.board = np.arange(0,self.size).reshape(self.rows,self.cols).astype(object)
        self.board= np.full((self.rows,self.cols), " _ ", dtype= object)
        

    def pboard(self):
        for i in range (self.rows): 
            print(" -" * (self.cols * 3+1))
            for j in range (self.cols):
                print (" | "+ self.board[i][j], end="")
            print(" | ")

        print(" -" * (self.cols * 3+1))

    

class Condition(TTT):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        
        self.win = False
        self.winner = None

    def check_h_win(self):
        for i in range (self.rows):
            if self.board[i][0] == " _ ":
                continue

            # assumes winning before checking, if condition not met then again set backs to false
            # if initialized after condition checking, it'll overwrite the condition with True 
            self.win = True
            for j in range (1,self.cols):
                if self.board[i][j] != self.board[i][0]:
                    self.win = False


            if self.win:
                self.winner = self.board[i][0]
                return self.winner
        


    def check_v_win(self):
        for i in range(self.cols):
            if self.board[0][i] == " _ ":
                continue

            self.win = True
            for j in range (1,self.rows):
                if self.board[j][i] != self.board[0][i]:
                    self.win = False
                

            if self.win:
                self.winner = self.board[0][i]
                return self.winner

            
    def l_check_diag_win(self):
        self.win = True
        for i in range(self.rows):
            if self.board[0][0] == " _ ":
                continue

            if self.board[i][i] != self.board[0][0]:
                self.win = False
            
        if self.win:
            self.winner = self.board[0][0]
            return self.winner

    def r_check_diag_win(self):

        self.win = True

        for i in range (self.rows):
            if self.board[0][self.cols-1] == " _ ":
                continue

            if self.board[i][self.cols-1-i] !=self.board[0][self.cols-1]:
                self.win= False

        if self.win:
            self.winner = self.board[0][self.cols-1]
            return self.winner
            
    
    def check_tie(self):
        for i in range(self.rows):
            for j in range (self.cols):
                if self.board[i][j] == " _ ":
                    return False
        return True


class Player(Condition):
    def __init__(self,rows, cols, player= " X "):
        super().__init__(rows,cols)
        self.curr_player = player
        self.game_running = True
    
    def user_input(self):
        while True:
            try:
                # to make indexing easier sub 1 from initial input
                r = int(input(f"Enter the row: 1-{self.rows}: "))-1
                c = int(input(f"Enter the col 1-{self.cols}: "))-1

                if 0<= r< self.rows and 0<=c<self.cols:
                    print(f"\nRow {r+1} Col {c+1} Selected.")

                    if self.board[r][c]== " _ ":
                        self.board[r][c]= self.curr_player
                        break
                    
                    else:
                        print (f"Given position is already occupied!! ")


                #if r more than 4 then error cause if max 5 and user input = 5 
                #then 5-1 = 4, it'll go from 0-4
                elif ( r<0 or r>=self.rows) and (c<0 or c>=self.cols):
                    print(f"\nRow {r+1} Col {c+1} Selected. \nRows and Columns must be more than 0 but less than {self.rows+1}\n")

                elif r<0 or r>=self.rows: # if 5 or more error, must be less than 5
                    print(f"\nRow {r+1} is wrong!!!. Please enter valid row input\n")

                elif c<0 or c>=self.cols:
                    print(f"\nCol {c+1} is wrong!!!.please enter valid col input\n")
                            
            except Exception as e:
                print(f"Error: {e}")


    def swich_player(self):
        if self.curr_player == " X ":
            self.curr_player = " O "
        else:
            self.curr_player= " X "


    def winner_print(self):
        winner = (self.check_h_win() or
                  self.check_v_win() or self.l_check_diag_win() or self.r_check_diag_win() )
        
        if winner == self.curr_player:
            print (f"Congratulations {self.curr_player} Won")
            self.game_running = False

        elif self.check_tie():
            print("It's a Tie!!!")
            self.game_running = False



def play():
    board = TTT(3,3)
    playing = Player(board.rows, board.cols)
    playing.pboard()
    #print("To quit type 404")
    while playing.game_running:
        playing.user_input()
        playing.pboard()
        playing.winner_print()
        playing.swich_player()

    
play()
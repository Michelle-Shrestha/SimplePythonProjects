
#Priniting game board
# Take player input
#check for win or tie
#switch the player
#Check for win or tie again

game_running = True
winner = None
current_player = " X "


def main_board():
    #board = []
    return [" _ " for _ in range (9)]

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print ("-------------")
        print ("|"+ board[i]+ "|" +board[i+1]+ "|" +board[i+2]+ "|")
    print ("-------------\n") 

def switch_player():
    global current_player
    if current_player == " X ":
         current_player = " O "
    else:
        current_player = " X "
    return current_player

def player_input(board):
    while True:
        try:
            choice = int(input("Enter a position (1-9): "))
            if choice < 1 or choice > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[choice-1]== " _ ":
                board[choice-1] = current_player
                #switch_player()
                return choice
            else:
                print("Position already taken. Please choose another.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board):
    global current_player, game_running
    #check rows:
    for i in range(0,9,3):
        if board[i]== board[i+1] == board[i+2] == current_player:
            game_running = False
            winner = current_player
            return winner
        
    #check columns:
    for i in range (0,3):
        if board[i] == board[i+3] == board[i+6]== current_player:
            game_running = False
            winner= current_player
            return winner
        
    #check diagonals:
    if board[0]== board[4]== board[8] == current_player:
        game_running = False
        winner = current_player
        return winner
    
    if board[2]==board[4]== board[6] == current_player:
        game_running = False
        winner = current_player
        return winner
    return None

def check_tie(board):
    global game_running
    if " _ " not in board:
        game_running = False
        return True
    return False


def Main():
    board = main_board()
    print_board(board)
    while game_running:
        player_input(board)
        print_board(board)
        tie = check_tie(board)
        result = check_win(board)
        if result == current_player:
            print(f"Congratulations, Player {current_player} wins!")
            break
        if tie:
            print("Oh My!!,, It's a tie!")
            break
        switch_player()
        
Main()

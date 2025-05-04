import math
nodes_visited=0
# Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    """prints current state of board """
    res=""
    for i in range(3):
        for j in range(3):
            res+=str(board[i][j])+"|"
        res+="\n"
        if i<2:
            res+="-------\n"
    return res




def is_winner(board, player):
    """checks the given player has won or not ., return true , false """
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]==player:
            return True
        
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]==player:
            return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    if board[0][2]==board[1][1]==board[2][0]==player:
        return True


def is_full(board):
    """returns True if the board is full else false"""
    for row in board:
        for pos in row:
            if pos==' ':
                return False
    return True
def open_lines(board, depth):
    score = 0
    l = []
    for row in board:
        l.append(row)
    for col in range(3):
        l.append([board[row][col] for row in range(3)])
    l.append([board[i][i] for i in range(3)])
    l.append([board[i][2 - i] for i in range(3)])
    for line in l:
        X_count = 0
        O_count = 0
        for cell in line:
            if cell == 'X':
                X_count += 1
            elif cell == 'O':
                O_count += 1

        if O_count == 0 and X_count > 0:
            score += 1  
        elif X_count == 0 and O_count > 0:
            score -= 1 

    if is_winner(board, 'X'):
        return 100 + depth
    if is_winner(board, 'O'):
        return -100 - depth

    return score

def minimax(board, depth, is_maximizing, alpha, beta):
    """ Minimax algorithm to evaluate board positions two option ,set depth level heuristic
      ,or continue till game end ,return best score  """
    global nodes_visited
    nodes_visited+=1
    if is_winner(board,"X"):
        return +10
    if is_winner(board,"O"):
        return -10
    if is_full(board):
        return 0
    if depth==0:
        open_lines(board,10)
    if is_maximizing:
        best_score=float("-inf")
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==' ':
                    board[i][j]="X"
                    eval_score= minimax(board, depth-1, False, alpha, beta)
                    board[i][j]=" "
                    best_score=max(best_score, eval_score)
                    alpha=max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score=float("inf")
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==' ':
                    board[i][j]="O"
                    eval_score= minimax(board, depth-1, True, alpha, beta)
                    board[i][j]=" "
                    best_score=min(eval_score,best_score)
                    beta=min(beta, best_score)
                if alpha>=beta:
                    break
        return best_score


    # add conditon beta less than equal to alpha both for minimizer (USER) and maximizer (ai)  and where condition meets break the loop 

def best_move():
    """finds and returns the best move for the AI using the minimax function ,
      while calling minimax ,set alpha to minus infinty and beta to positive infinity."""
    best_score=float("-inf")
    move =None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==' ':
                board[i][j]="X"
                eval=minimax(board,3,False,float("-inf"),float("inf"))
                board[i][j]=" "
                if eval > best_score:
                    best_score = eval
                    move = (i, j)
    #print(f"Nodes visited:{nodes_visited}")
    return move
        

      
def main():
    """Main game loop."""
    
    print("0|1|2")
    print("---------")
    print("3|4|5")
    print("---------")
    print("6|7|8")
    print("Choose the position from this board")

    while True:
        print(print_board(board))

        # User move
        user_pos = int(input("Enter the position where you want to insert 'O': "))
        if user_pos < 0 or user_pos > 8:
            print("Invalid position. Please enter a number between 0 and 8.")
            continue
        row = user_pos // 3
        col = user_pos % 3

        if board[row][col] == ' ':
            board[row][col] = "O"
        else:
            print("Position already occupied. Please choose another position.")
            continue

        # Display the board after the user's move
        print(print_board(board))

        # Check if the user has won
        if is_winner(board, "O"):
            print("You win!")
            break

        # Check if the board is full 
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("Maximizer's turn, 'X':")
        ai_move = best_move()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "X"

        #Check if the AI has won
        if is_winner(board, "X"):
            print(print_board(board))
            print("AI wins!")
            break

        # Check if the board is full after AI's move
        if is_full(board):
            print("It's a tie!")
            break
    print(f"Nodes visited:{nodes_visited}")

main() 
    
    

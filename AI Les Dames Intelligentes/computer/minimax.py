#Minimax algorithm for the computer to play the game against the human
#This algorithm simulates all the possible valid moves that can take place at a given action until the next action is reached
#It does this by creating a tree traversal approach to this as it is aims to maximise the ‘score’ of the AI winning and minimize the ‘score’ of losing. 
# This is a backtracking/recursive process as it constantly decides if I take this action, what this value will entail. 
# Is this value higher than the previous one or lower… 
# Eventually, the maximising player (AI) generates values for each action and looks at all the possible next actions that it will entail, ultimately finding the best move to play.


from copy import deepcopy #Copy the board a numerous amount of times with the referrence and object
import pygame

BLACK = (86, 83, 82)#Man WHITE
WHITE = (248, 248, 248)#Man BLACK,RED

#recursive call
def minimax(location, depth, maximum, interface):
    if depth == 0 or location.champion() != None:
        return location.analyse(), location
    
    #Let BLACK be the AI
    if maximum:
        max_analyse = float('-inf')#-infinity is the best score we have seen so far
        optimum_path = None
        for move in obtain_every_man(location, BLACK, interface):#for every move we make in the game we will get a new board and we analyse the board 
            evaluation = minimax(move, depth-1, False, interface)[0]#for each of the nodes
            max_analyse = max(max_analyse, evaluation)
            if max_analyse == evaluation:
                optimum_path = move
        
        return max_analyse, optimum_path
    else:
        min_analyse = float('inf')#infinity is the best score we have seen so far
        optimum_path = None
        for move in obtain_every_man(location, WHITE, interface):#for every move we make in the game we will get a new board and we analyse the board  
            evaluation = minimax(move, depth-1, True, interface)[0]#for each of the nodes
            min_analyse = min(min_analyse, evaluation)
            if min_analyse == evaluation:
                optimum_path = move
        
        return min_analyse, optimum_path


def move_simulation(man, move, board, interface, jump):
    board.move(man, move[0], move[1])
    if jump:
        board.clear(jump)

    return board


def obtain_every_man(board, color, interface):
    moves = []#blank list which will store board, piece, forshadowing what the board will look like after moving a piece
    for man in board.obtain_every_man(color):
        correct_movement = board.get_correct_movement(man)
        for move, jump in correct_movement.items():
            temp_board = deepcopy(board)
            temp_man = temp_board.obtain_man(man.row, man.col)
            new_board = move_simulation(temp_man, move, temp_board, interface, jump)
            moves.append(new_board)
    
    return moves





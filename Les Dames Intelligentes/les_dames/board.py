import pygame
from .constants import GREEN, ROWS, CREAM, SQUARE_SIZE, COLS, BLACK, WHITE
from .man import Man#from .piece import Piece
from pygame import mixer

class Board:
    def __init__(self):#Internal represenation of the board
        self.board = []#2D array with a piece object and a location value corresponding to that
        self.white_left = self.black_left = 20#how many pieces/man are left
        self.white_kings = self.black_kings = 0
        self.generate_board()
    
    def generate_squares(self, win):#Method to generate the squares
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):#Creates a draught board tile pattern from the top left (0,0)
                pygame.draw.rect(win, CREAM, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def generate_board(self):#Setting up the board
        for row in range(ROWS):
            self.board.append([])#Interior list for each row
            for col in range(COLS):
                if col%2 == ((row+1)%2):
                    if row<4:#3
                        self.board[row].append(Man(row, col, BLACK))
                    elif row>5:#4
                        self.board[row].append(Man(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def create(self, win):#draw method to create squares on the board/grid
        self.generate_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                man = self.board[row][col]
                if man != 0:
                    man.create(win)

    def clear(self, pieces):
        for man in pieces:
            self.board[man.row][man.col]=0
            if man != 0:
                if man.color == CREAM:
                    self.white_left -= 1
                else:
                    self.black_left -= 1

    
    def champion(self):
        if self.white_left <=0:
            return GREEN
        elif self.black_left <= 0:
            return 
            
        return None

    
    

    def movement(self, man, row, col):
        self.board[man.row][man.col], self.board[row][col] = self.board[row][col], self.board[man.row][man.col]#piece Swap values in order to move without using any temp variables/values
        man.movement(row, col)#piece
        if row == ROWS - 1 or row == 0:
            man.generate_king()#make_king
            if man.color == BLACK:
                self.black_kings +=1
            else:
                self.white_kings +=1
    
    def obtain_man(self, row, col):#get_piece
        return self.board[row][col]

    #Movement
    #check to see the colour of the man/piece
    #look at each diagonal side for any correct/valid movement
    #check one at a time for each square to see if it's empty
    #if it has a man/piece on the diagonal, check the next square to see what's there
    #repeat for right side
    #what happens when double-jumping?
    #well if already jumped over man then check to see if you can do it again/repeat

    def get_correct_movement(self, man):#given a man/piece find the corresponsing valid moves
        movement = {}#moves
        left = man.col - 1#move left 1
        right = man.col + 1#move right 1
        row = man.row
        if man.color == WHITE or man.king:
            movement.update(self._look_left(row-1, max(row-3, -1), -1, man.color, left))
            movement.update(self._look_right(row-1, max(row-3, -1), -1, man.color, right))
        
        if man.color == BLACK or man.king:
            movement.update(self._look_left(row+1, min(row+3, ROWS), 1, man.color, left))
            movement.update(self._look_right(row+1, min(row+3, ROWS), 1, man.color, left))
        return movement#return all the correct movement for that man/piece

    #Handles where we can move to
    def _look_left(self, begin, end, step, color, left, jumped=[]):
        movement = {}
        last = []
        for r in range(begin, end, step):
            if left < 0:
                break
            current = self.board[r][left]#get_piece
            if current == 0:
                if jumped and not last:#skipped
                    break
                elif jumped:#skip_only
                    movement[(r, left)] = last + jumped#skipped
                else:
                    movement[(r, left)] = last#moves
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)
                    movement.update(self._look_left(r+step, row, step, color, left-1, jumped=last))
                    movement.update(self._look_right(r+step, row, step, color, left+1, jumped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return movement


    def _look_right(self, begin, end, step, color, right, jumped=[]):#_traverse_right, self, start, stop, step, color, left skipped
        movement = {}
        last = []
        for r in range(begin, end, step):
            if right >= COLS:
                break
            current = self.board[r][right]#get_piece
            if current == 0:
                if jumped and not last:#skipped
                    break
                elif jumped:#skip_only
                    movement[(r, right)] = last + jumped#skipped
                else:
                    movement[(r, right)] = last#moves
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)
                    movement.update(self._look_left(r+step, row, step, color, right-1, jumped=last))
                    movement.update(self._look_right(r+step, row, step, color, right+1, jumped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        return movement










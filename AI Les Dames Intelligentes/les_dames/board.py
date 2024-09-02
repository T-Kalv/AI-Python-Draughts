import pygame
from .constants import GREEN, ROWS, CREAM, SQUARE_SIZE, COLS, BLACK, WHITE
from .man import Man

class Board:
    def __init__(self):#Internal represenation of the board
        self.board = []#2D array with a piece object and a location value corresponding to that
        self.white_left = self.black_left = 12#how many pieces/man are left
        self.white_kings = self.black_kings = 0
        self.generate_board()
    
    def generate_squares(self, win):#Method to generate the squares
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):#Creates a draught board tile pattern from the top left (0,0)
                pygame.draw.rect(win, CREAM, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    #Analysis method given the state of this board what is the corresponding score to this for the minimax algorithm
    def analyse(self):#Takes into account how many kings and man/pieces there are left
        return self.black_left - self.white_left + (self.black_kings * 0.5 - self.white_kings * 0.5)#The better this function is is the better the analyis of the board is

    def obtain_every_man(self, color):#loop through all the man/pieces and return that colour
        pieces = []
        for row in self.board:
            for man in row:
                if man != 0 and man.color == color:
                    pieces.append(man)
        return pieces

    def move(self, man, row, col):#piece movement method which will move the pieces/man to a correspondng row/column
        self.board[man.row][man.col], self.board[row][col] = self.board[row][col], self.board[man.row][man.col]#piece Swap values in order to move without using any temp variables/values
        man.move(row, col)

        if row == ROWS - 1 or row == 0:
            man.generate_king()
            if man.color == BLACK:
                self.black_kings += 1
            else:
                self.white_kings += 1 

    def obtain_man(self, row, col):#given a row and column it will give you the piece/man at that row/column
        return self.board[row][col]

    def generate_board(self):#Setting up the board
        for row in range(ROWS):
            self.board.append([])#Interior list for each row
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Man(row, col, BLACK))
                    elif row > 4:
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
            self.board[man.row][man.col] = 0
            if man != 0:
                if man.color == CREAM:
                    self.white_left -= 1
                else:
                    self.black_left -= 1
    
    def champion(self):
        if self.white_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return WHITE
        
        return None 

    #Movement
    #check to see the colour of the man/piece
    #look at each diagonal side for any correct/valid movement
    #check one at a time for each square to see if it's empty
    #if it has a man/piece on the diagonal, check the next square to see what's there
    #repeat for right side
    #what happens when double-jumping?
    #well if already jumped over man then check to see if you can do it again/repeat

    def get_correct_movement(self, man):#given a man/piece find the corresponsing valid moves
        moves = {}
        left = man.col - 1#move left 1
        right = man.col + 1#move right 1
        row = man.row

        if man.color == WHITE or man.king:
            moves.update(self._look_left(row -1, max(row-3, -1), -1, man.color, left))
            moves.update(self._look_right(row -1, max(row-3, -1), -1, man.color, right))
        if man.color == BLACK or man.king:
            moves.update(self._look_left(row +1, min(row+3, ROWS), 1, man.color, left))
            moves.update(self._look_right(row +1, min(row+3, ROWS), 1, man.color, right))
    
        return moves#return all the correct movement for that man/piece

    #Handles where we can move to
    def _look_left(self, start, stop, step, color, left, jumped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if jumped and not last:
                    break
                elif jumped:
                    moves[(r, left)] = last + jumped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._look_left(r+step, row, step, color, left-1,jumped=last))
                    moves.update(self._look_right(r+step, row, step, color, left+1,jumped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _look_right(self, start, stop, step, color, right, jumped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if jumped and not last:
                    break
                elif jumped:
                    moves[(r,right)] = last + jumped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._look_left(r+step, row, step, color, right-1,jumped=last))
                    moves.update(self._look_right(r+step, row, step, color, right+1,jumped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
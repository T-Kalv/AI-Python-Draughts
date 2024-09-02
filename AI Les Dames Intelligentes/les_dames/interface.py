import pygame
from .constants import SQUARE_SIZE, WHITE, BLACK, GREENO, SQUARE_SIZE
from les_dames.board import Board
from pygame import mixer

mixer.init()

class Interface:
    def __init__(self, win):
        self._init()#Creates the board
        self.win = win
    
    def update(self):#update method
        self.board.create(self.win)
        self.create_correct_movement(self.correct_movement)
        pygame.display.update()

    def _init(self):#Create the board using the _init method
        self.selected = None
        self.board = Board()#Handles the state of board
        self.turn = WHITE
        self.correct_movement = {}

    def champion(self):
        return self.board.champion()

    def reset(self):
        self._init()

    def choose(self, row, col):#allows us to move choose a piece and move it
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.choose(row, col)
        #technically recursive
        man = self.board.obtain_man(row, col)
        if man != 0 and man.color == self.turn:
            self.selected = man
            self.correct_movement = self.board.get_correct_movement(man)
            return True
            
        return False

    def _move(self, row, col):
        man = self.board.obtain_man(row, col)
        if self.selected and man == 0 and (row, col) in self.correct_movement:
            self.board.move(self.selected, row, col)
            jumped = self.correct_movement[(row, col)]
            if jumped:
                self.board.clear(jumped)
            self.change_turn()
        else:
            return False

        return True

    def create_correct_movement(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREENO, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):#Switches turn after player has done their turn
        move_Sound = mixer.Sound('move.wav')#Plays Les_Dames piece/man sound move
        move_Sound.play()
        self.correct_movement = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def obtain_board(self):#We have a board object stored and we want to return the board
        return self.board

    def computer_move(self, board):#return the new board after AI has made a move (updates it)
        self.board = board
        self.change_turn()
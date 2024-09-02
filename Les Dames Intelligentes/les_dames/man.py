import pygame
from .constants import WHITE, BLACK, SQUARE_SIZE, GREY, KING, KNIGHT
from pygame import mixer
import time
from time import sleep
mixer.init()

#Represents one singular man/piece
class Man:
    PADDING = 16
    OUTLINE = 4
    def __init__(self, row, col, color):
        self.row = row  
        self.col = col
        self.color = color
        self.king = False#King false by default
        
        self.x=0
        self.y=0
        self.analyse_position()
    
    def analyse_position(self):#calc_pos
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2#Centres the pieces/man
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2#Centres the pieces/man

    def generate_king(self):
        self.king = True
        sound = 'king_sound.mp3'#Plays the copyright-free sound by Sound Effect from https://pixabay.com/sound-effects/success-fanfare-trumpets-6185/
        mixer.music.load(sound)
        mixer.music.play()
        sleep(1)
        music = 'background_music.mp3'#Plays the copyright-free background music by https://pixabay.com/users/the_mountain-3616498/?amp=
        mixer.music.load(music)
        mixer.music.play(-1)
        

    def create(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius+self.OUTLINE)#Creates the bigger circle (outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)#Creates the smaller circle (inside)
        win.blit(KNIGHT,(self.x - KNIGHT.get_width()//2, self.y - KNIGHT.get_height()//2))#Places Knight directly centre using (x,y) position on screen and does //2 to avoid rounding error
        if self.king:
            win.blit(KING,(self.x - KING.get_width()//2, self.y - KING.get_height()//2))#Places King directly centre using (x,y) position on screen and does //2 to avoid rounding error

    def movement(self, row, col):
        self.row = row 
        self.col = col 
        self.analyse_position()



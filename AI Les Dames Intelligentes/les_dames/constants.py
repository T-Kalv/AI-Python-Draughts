import pygame

#Dimensions of the board
WIDTH, HEIGHT = 800, 800#1000, 1000
ROWS, COLS = 8, 8#10, 10
SQUARE_SIZE = WIDTH//COLS

#RGB 
GREEN = (118, 150, 86)
CREAM= (238, 238, 210)
BLACK = (86, 83, 82)
WHITE = (248, 248, 248)
GREY = (84, 82, 70)#Outline 
GREENO = (246, 248, 105)#Indicator 

#KING
KING = pygame.transform.scale(pygame.image.load('king.png'),(50,50))
#Using icon from https://icons8.com/icon/XNqagknpLLqu/palace

#KNIGHT
KNIGHT = pygame.transform.scale(pygame.image.load('knight.png'),(50,50))
#Using icon from https://icons8.com/icon/1011/knight
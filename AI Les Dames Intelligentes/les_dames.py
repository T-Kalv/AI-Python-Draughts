#Les Dames Intelligentes with Artificial Intelligence using the Minimax Algorithm (Human Vs AI)
#Using this as a reference/guide: https://github.com/jemappellesami/Python-Checkers-AI
import pygame, sys, threading
from les_dames.constants import SQUARE_SIZE, WIDTH, HEIGHT, WHITE, BLACK
from les_dames.interface import Interface
from computer.minimax import minimax
from pygame import mixer
import time
from time import sleep

# Initialize the game engine
pygame.init()

FPS = 60#Program runs at 60FPS to maintain stability on all devices
 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AI Les Dames Intelligentes')#Name of the program
icon = pygame.image.load('les dames icon.png')#App icon
pygame.display.set_icon(icon)
running = True


#Needs to be before main duh
def access_mouse_position(pos):
    x,y=pos#tuple
    col=x//SQUARE_SIZE
    row=y//SQUARE_SIZE
    return row, col

def main():
    run = True
    move_Sound = mixer.Sound('New_Game.wav')#Plays Les_Dames piece/man sound move
    move_Sound.play()
    clock = pygame.time.Clock()
    #board = Board()
    interface = Interface(WIN)
    #board.movement()
    time.sleep(1)
    #In order to play background music, I had to use the pygame mixer module using stackoverflow as a reference: https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
    music = 'background_music.mp3'#Plays the copyright-free background music by https://pixabay.com/users/the_mountain-3616498/?amp=
    mixer.init()
    mixer.music.load(music)
    mixer.music.play(-1)
    while run:
        clock.tick(FPS)#FPS=60

        if interface.turn == BLACK:
            value, new_board = minimax(interface.obtain_board(), 4, BLACK, interface)#The higher the depth in the minimax algorithm (in this case 4) the more accurate the AI will be
            #So in the future I could add different difficulties or maybe alpha-beta pruning
            interface.computer_move(new_board)

        if interface.champion() != None:
            print(interface.champion())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#When user hits red button
                run = False#Quits the program
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = access_mouse_position(pos)#get_row_col_from_mouse(pos):
                interface.choose(row, col)
            if event.type == pygame.KEYDOWN:#When user hits the x key on their keyboard the game quits
                if event.key == pygame.K_x:
                    music = 'exit_sound.mp3'#Plays the copyright-free background sound by https://pixabay.com/sound-effects/error-3-125761/
                    mixer.music.load(music)
                    mixer.music.play()
                    sleep(1)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:#When user hits the r key on their keyboard the game restarts
                if event.key == pygame.K_r:
                    main()
                

        interface.update()#class that represents the state of the interface

    pygame.quit()

main()

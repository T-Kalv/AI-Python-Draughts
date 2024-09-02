#Les Dames Intelligentes (Human Vs Human)
#Using this as a reference/guide: https://github.com/jemappellesami/Python-Checkers-AI
import pygame, sys, threading
from les_dames.constants import SQUARE_SIZE, WIDTH, HEIGHT, WHITE, BLACK
from les_dames.interface import Interface
from pygame import mixer
import time
from time import sleep

# Initialize the game engine
pygame.init()

mixer.init()

FPS = 60#Program runs at 60FPS to maintain stability on all devices
 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Les Dames Intelligentes')#Name of the program
icon = pygame.image.load('les dames icon.png')
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
    #In order to play background music, I had to use the pygame mixer module using stackoverflow as a reference: https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
    music = 'background_music.mp3'#Plays the copyright-free background music by https://pixabay.com/users/the_mountain-3616498/?amp=
    mixer.music.load(music)
    mixer.music.play(-1)
    
    while run:
        clock.tick(FPS)

        if interface.champion() != None:
            print(interface.champion())

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
                if event.key == pygame.K_r or pygame.K_F5:
                    main()

        interface.update_display()

    pygame.quit()

main()









"""
This file is the main file of My-PyChess application.
Run this file to launch the program.

In this file, we handle the main menu which gets displayed at runtime.
"""
import pygame

import chess
import menus
from tools.loader import MAIN

# This is a non-important bit of code. Flush stdout - useful incase external
# programs are calling this application.
# sys.stdout.flush()

# Some initialisation
pygame.init()
clock = pygame.time.Clock()

# Initialise display, set the caption and icon. Use SCALED if on pygame 2.
if pygame.version.vernum[0] >= 2:
    win = pygame.display.set_mode((500, 500), pygame.SCALED)
else:
    win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My-Chess")
pygame.display.set_icon(MAIN.ICON)

# Coordinates of buttons in rectangle notation.
sngl = (140, 200, 220, 40)


# This is the function that displays the main screen.
# "prefs" value is passed, prefs is a list of all the user settings
def showMain():
    # cnt and image are two global variables, cnt is an integer that is
    # incremented in every frame, when cnt reaches 210, it is setback to zero.
    # img variable denotes the image that is displayed on the screen
    # it can have a value from 0 to 3 (both inclusive)
    # global cnt, img

    # First, blit background image (based on the img variable)
    win.blit(MAIN.BG, (0, 0))


    # Now blit all the texts onto the screen one by one
    win.blit(MAIN.HEADING, (80, 20))
    pygame.draw.line(win, (255, 255, 255), (80, 100), (130, 100), 4)
    pygame.draw.line(win, (255, 255, 255), (165, 100), (340, 100), 4)
    # win.blit(MAIN.VERSION, (345, 95))

    win.blit(MAIN.SINGLE, sngl[:2])
    # win.blit(MAIN.MULTI, mult[:2])
    # win.blit(MAIN.ONLINE, onln[:2])
    # win.blit(MAIN.LOAD, load[:2])
    # win.blit(MAIN.PREF, pref[:2])
    # win.blit(MAIN.HOWTO, hwto[:2])
    # win.blit(MAIN.ABOUT, abt[:2])
    # win.blit(MAIN.STOCK, stok[:2])

# Initialize a few more variables
# cnt = 0
# img = 0
run = True

# Load the settings of the player
# prefs = menus.pref.load()

# music = sound.Music()
# music.play(prefs)
while run:
    # Start the game loop at 30fps, show the screen every time at first
    clock.tick(30)
    showMain()

    # We need to get the position of the mouse so that we can blit an image
    # on the text over which the mouse hovers
    x, y = pygame.mouse.get_pos()

    if sngl[0] < x < sum(sngl[::2]) and sngl[1] < y < sum(sngl[1::2]):
        win.blit(MAIN.SINGLE_H, sngl[:2])

    # Begin pygame event loop to catch all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User has clicked somewhere, determine which button and
            # call a function to handle the game into a different window.
            x, y = event.pos

            if sngl[0] < x < sum(sngl[::2]) and sngl[1] < y < sum(sngl[1::2]):
                # sound.play_click(prefs)
                ret = menus.splayermenu(win)
                if ret == 0:
                    run = False
                elif ret != 1:
                    if ret[0]:
                        run = chess.mysingleplayer(win, ret[1])
                    

    # Update the screen every frame
    pygame.display.flip()

# Stop music, quit pygame after the loop is done
pygame.quit()

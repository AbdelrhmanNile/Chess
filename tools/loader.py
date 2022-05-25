"""
This file is a part of My-PyChess application.
This file loads all the images and texts that are used.

Most of the scripts in this application import specific classes from this
module. Each class is a collection of resources for a particular script.
All font-related stuff is done in this file, the functions to put a number
on the screen and display date and time are also defined here
"""

import os.path
import pygame

# Initialize pygame.font module and load the font file.
pygame.font.init()
FONT = os.path.join("res", "Asimov.otf")

# Load different sizes of the font.
head = pygame.font.Font(FONT, 80)
large = pygame.font.Font(FONT, 50)
medium = pygame.font.Font(FONT, 38)
small = pygame.font.Font(FONT, 27)
vsmall = pygame.font.Font(FONT, 17)

# Define RGB color constants for use.
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 20, 20)

# Define a few constants that contain loaded texts of numbers and chararters.
NUM = [vsmall.render(str(i), True, WHITE) for i in range(10)]
SLASH = vsmall.render("/", True, WHITE)
COLON = vsmall.render(":", True, WHITE)



def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM[int(i)], (pos[0] + (cnt * 9), pos[1]))



def splitstr(string, index=57):
    data = []
    while len(string) >= index:
        data.append(string[:index])
        string = string[index:]
    data.append(string)
    return data


# Defined important globals for loading background image sprites.
BGSPRITE = pygame.image.load(os.path.join("res", "img", "bgsprites.jpg"))
PSPRITE = pygame.image.load(os.path.join("res", "img", "piecesprite.png"))

# Load global image for back
BACK = pygame.image.load(os.path.join("res", "img", "back.png"))


class CHESS:
    PIECES = ({}, {})
    for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
        for side in range(2):
            PIECES[side][ptype] = PSPRITE.subsurface(
                (i * 50, side * 50, 50, 50))

    CHECK = small.render("CHECK!", True, BLACK)
    STALEMATE = small.render("STALEMATE!", True, BLACK)
    CHECKMATE = small.render("CHECKMATE!", True, BLACK)
    LOST = small.render("LOST", True, BLACK)
    CHOOSE = small.render("CHOOSE:", True, BLACK)
    UNDO = small.render("Undo", True, BLACK)

    MESSAGE = (
        small.render("Do you want to quit", True, WHITE),
        small.render("this game?", True, WHITE),
    )

    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)
    TURN = (
        small.render("Others turn", True, BLACK),
        small.render("Your turn", True, BLACK),
    )

    DRAW = small.render("Draw", True, BLACK)

    OK = small.render("Ok", True, WHITE)
    COL = small.render(":", True, BLACK)


class MAIN:
    HEADING = head.render("MyChess", True, WHITE)
    ICON = pygame.image.load(os.path.join("res", "img", "icon.gif"))
    BG = BGSPRITE.subsurface((0, 0, 500, 500))

    SINGLE = medium.render("Play", True, WHITE)

    SINGLE_H = medium.render("Play", True, GREY)


class SINGLE:
    HEAD = large.render("Singleplayer", True, WHITE)
    SELECT = pygame.image.load(os.path.join("res", "img", "select.jpg"))
    CHOOSE = small.render("Choose:", True, WHITE)
    START = small.render("Start Game", True, WHITE)

    with open(os.path.join("res", "texts", "single1.txt")) as f:
        PARA1 = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    BACK = vsmall.render("Go Back", True, WHITE)
    OK = vsmall.render("Ok", True, WHITE)
    NOTNOW = vsmall.render("Not Now", True, WHITE)


pygame.font.quit()

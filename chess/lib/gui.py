"""
This file is a part of My-PyChess application.
In this file, we define some basic gui-related functions

For a better understanding of the variables used here, checkout docs.txt
"""
import pygame
from tools.loader import CHESS, BACK
from tools import sound

# Apply 'convert_alpha()' on all pieces to optimise images for speed.


def convertPieces(win):
    for i in range(2):
        for key, val in CHESS.PIECES[i].items():
            CHESS.PIECES[i][key] = val.convert_alpha(win)

# This function displays the choice menu when called, taking user input.
# Returns the piece chosen by the user


def getChoice(win, side):
    win.blit(CHESS.CHOOSE, (130, 10))
    win.blit(CHESS.PIECES[side]["q"], (250, 0))
    win.blit(CHESS.PIECES[side]["b"], (300, 0))
    win.blit(CHESS.PIECES[side]["r"], (350, 0))
    win.blit(CHESS.PIECES[side]["n"], (400, 0))
    pygame.display.update((0, 0, 500, 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < event.pos[1] < 50:
                    if 250 < event.pos[0] < 300:
                        return "q"
                    elif 300 < event.pos[0] < 350:
                        return "b"
                    elif 350 < event.pos[0] < 400:
                        return "r"
                    elif 400 < event.pos[0] < 450:
                        return "n"

# This function draws the board


def drawBoard(win):
    win.fill((100, 200, 200))
    pygame.draw.rect(win, (180, 100, 30), (50, 50, 400, 400))
    for y in range(1, 9):
        for x in range(1, 9):
            if (x + y) % 2 == 0:
                pygame.draw.rect(win, (220, 240, 240),
                                 (50 * x, 50 * y, 50, 50))

# This funtion draws all pieces onto the board


def drawPieces(win, board):
    for side in range(2):
        for x, y, ptype in board[side]:
            # if flip:
            #     x, y = 9 - x, 9 - y
            win.blit(CHESS.PIECES[side][ptype], (x * 50, y * 50))

# This function displays the prompt screen when a user tries to quit
# User must choose Yes or No, this function returns True or False respectively


def prompt(win, msg=None):
    pygame.draw.rect(win, (0, 0, 0), (110, 160, 280, 130))
    pygame.draw.rect(win, (255, 255, 255), (110, 160, 280, 130), 4)

    pygame.draw.rect(win, (255, 255, 255), (120, 160, 260, 60), 2)

    win.blit(CHESS.YES, (145, 240))
    win.blit(CHESS.NO, (305, 240))
    pygame.draw.rect(win, (255, 255, 255), (140, 240, 60, 28), 2)
    pygame.draw.rect(win, (255, 255, 255), (300, 240, 50, 28), 2)

    if msg is None:
        win.blit(CHESS.MESSAGE[0], (130, 160))
        win.blit(CHESS.MESSAGE[1], (190, 190))

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 < event.pos[1] < 270:
                    if 140 < event.pos[0] < 200:
                        return True
                    elif 300 < event.pos[0] < 350:
                        return False

# This function shows a small animation when the game starts, while also
# optimising images for display - call only once per game


def start(win):
    convertPieces(win)
    clk = pygame.time.Clock()
    for i in range(101):
        clk.tick_busy_loop(140)
        drawBoard(win)

        for j in range(8):
            win.blit(CHESS.PIECES[0]["p"], (0.5 * i * (j + 1), 225 + 1.25 * i))
            win.blit(CHESS.PIECES[1]["p"], (0.5 * i * (j + 1), 225 - 1.25 * i))

        for j, pc in enumerate(["r", "n", "b", "q", "k", "b", "n", "r"]):
            win.blit(CHESS.PIECES[0][pc], (0.5 * i * (j + 1), 225 + 1.75 * i))
            win.blit(CHESS.PIECES[1][pc], (0.5 * i * (j + 1), 225 - 1.75 * i))

        pygame.display.update()

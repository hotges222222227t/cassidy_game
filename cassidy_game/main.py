import pygame
import sys

from cassidy_game.config import SCREEN_WIDTH, SCREEN_HEIGHT
from cassidy_game.scenes.menu import main_menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cassidy: Noir Hacker")
    main_menu(screen)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

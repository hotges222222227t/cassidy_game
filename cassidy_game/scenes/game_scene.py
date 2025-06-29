import pygame
import sys
import os
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_PATH

def draw_text(surface, text, size, x, y, color=(255, 0, 0)):
    font = pygame.font.Font(FONT_PATH, size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.topleft = (x, y)
    surface.blit(text_surface, rect)

def main_menu(screen):
    clock = pygame.time.Clock()

    # Абсолютный путь к изображению фона
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bg_path = os.path.join(base_dir, "assets", "images", "menu_bg.png")

    try:
        background = pygame.image.load(bg_path).convert()
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except pygame.error as e:
        print("Ошибка загрузки фона:", e)
        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background.fill((0, 0, 0))

    running = True
    while running:
        screen.blit(background, (0, 0))
        draw_text(screen, "НОВАЯ ИГРА", 40, 100, 400)
        draw_text(screen, "НАСТРОЙКИ", 40, 100, 470)
        draw_text(screen, "ВЫХОД", 40, 100, 540)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

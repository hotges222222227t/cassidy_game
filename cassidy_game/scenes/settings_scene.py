# scenes/settings_scene.py
import pygame
import json
import os
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_PATH

class SettingsScene:
    def __init__(self, game):
        self.game = game
        self.options = ["Музыка: Вкл", "Звук: Вкл", "Назад"]
        self.selected = 0
        self.font = pygame.font.Font(FONT_PATH, 36)
        self.settings_path = os.path.join("data", "settings.json")
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_path):
            with open(self.settings_path, "r") as f:
                self.settings = json.load(f)
        else:
            self.settings = {"music": True, "sound": True}

    def save_settings(self):
        with open(self.settings_path, "w") as f:
            json.dump(self.settings, f)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected == 0:
                    self.settings["music"] = not self.settings["music"]
                    self.options[0] = f"Музыка: {'Вкл' if self.settings['music'] else 'Выкл'}"
                elif self.selected == 1:
                    self.settings["sound"] = not self.settings["sound"]
                    self.options[1] = f"Звук: {'Вкл' if self.settings['sound'] else 'Выкл'}"
                elif self.selected == 2:
                    self.save_settings()
                    self.game.change_scene("menu")

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.selected else (255, 255, 255)
            text = self.font.render(option, True, color)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150 + i * 60))

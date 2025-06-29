# player_scene.py — Сцена плеера с возможностью воспроизведения музыки из папки и Telegram
import pygame
import sys
import os
from utils.audio_player import AudioPlayer
from utils.telegram_music_loader import TelegramMusicLoader
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

class PlayerScene:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.music_loader = TelegramMusicLoader()
        self.audio_player = AudioPlayer()
        self.tracks = self.load_tracks()
        self.current_track_index = 0

    def load_tracks(self):
        local_tracks = [f for f in os.listdir("assets/music") if f.endswith(".mp3") or f.endswith(".ogg")]
        telegram_tracks = self.music_loader.fetch_tracks()
        return local_tracks + telegram_tracks

    def draw_ui(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font("assets/fonts/noir_pixel.ttf", 32)
        y_offset = 100
        for idx, track in enumerate(self.tracks):
            color = WHITE if idx != self.current_track_index else (255, 0, 0)
            text_surface = font.render(track, True, color)
            self.screen.blit(text_surface, (100, y_offset))
            y_offset += 40

        control_text = font.render("Enter - Play | Up/Down - Navigate | Esc - Back", True, WHITE)
        self.screen.blit(control_text, (100, SCREEN_HEIGHT - 50))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_DOWN:
                        self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
                    elif event.key == pygame.K_UP:
                        self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
                    elif event.key == pygame.K_RETURN:
                        self.audio_player.play("assets/music/" + self.tracks[self.current_track_index])

            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(60)

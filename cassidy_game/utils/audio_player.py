# audio_player.py — модуль управления воспроизведением музыки

import pygame
import os

class AudioPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = []
        self.current_track = 0
        self.load_playlist()

    def load_playlist(self):
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3") or file.endswith(".ogg"):
                self.playlist.append(os.path.join(self.music_folder, file))
        self.playlist.sort()

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play()

    def previous_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play()

    def get_current_track_name(self):
        if self.playlist:
            return os.path.basename(self.playlist[self.current_track])
        return "No Track"

    def is_playing(self):
        return pygame.mixer.music.get_busy()
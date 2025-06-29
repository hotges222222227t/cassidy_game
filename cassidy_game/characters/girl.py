# characters/girl.py
import pygame
import random

class Girl(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {
            "idle": self.load_animation("idle", 3),
            "walk": self.load_animation("walk", 4)
        }
        self.state = "idle"
        self.image = self.animations[self.state][0]
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index = 0
        self.frame_timer = 0
        self.animation_speed = 0.15
        self.direction = random.choice(["left", "right"])
        self.walk_range = [pos[0] - 100, pos[0] + 100]
        self.velocity = 1
        self.pause_timer = 0

    def load_animation(self, name, count):
        return [
            pygame.image.load(f"assets/images/girl_{name}_{i}.png").convert_alpha()
            for i in range(count)
        ]

    def update(self, dt):
        self.frame_timer += dt

        if self.pause_timer > 0:
            self.pause_timer -= dt
            self.state = "idle"
        else:
            self.state = "walk"
            if self.direction == "right":
                self.rect.x += self.velocity
                if self.rect.x >= self.walk_range[1]:
                    self.direction = "left"
                    self.pause_timer = random.randint(30, 100)
            else:
                self.rect.x -= self.velocity
                if self.rect.x <= self.walk_range[0]:
                    self.direction = "right"
                    self.pause_timer = random.randint(30, 100)

        # Анимация
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.state])
            self.image = self.animations[self.state][self.frame_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

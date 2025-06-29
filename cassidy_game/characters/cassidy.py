# characters/cassidy.py
import pygame

class Cassidy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.animations = {
            "idle": self.load_animation("idle", 4),
            "walk": self.load_animation("walk", 6),
            "interact": self.load_animation("interact", 4)
        }
        self.current_animation = "idle"
        self.frame = 0
        self.image = self.animations[self.current_animation][self.frame]
        self.rect = self.image.get_rect(topleft=position)
        self.animation_speed = 0.15
        self.frame_timer = 0

    def load_animation(self, name, frame_count):
        frames = []
        for i in range(frame_count):
            path = f"assets/images/cassidy_{name}_{i}.png"
            img = pygame.image.load(path).convert_alpha()
            frames.append(img)
        return frames

    def update(self, dt, keys):
        # Управление
        dx, dy = 0, 0
        speed = 3

        if keys[pygame.K_w]:
            dy -= speed
            self.current_animation = "walk"
        elif keys[pygame.K_s]:
            dy += speed
            self.current_animation = "walk"
        elif keys[pygame.K_a]:
            dx -= speed
            self.current_animation = "walk"
        elif keys[pygame.K_d]:
            dx += speed
            self.current_animation = "walk"
        else:
            self.current_animation = "idle"

        self.rect.x += dx
        self.rect.y += dy

        # Анимация
        self.frame_timer += dt
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.frame = (self.frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.frame]

    def interact(self):
        self.current_animation = "interact"
        self.frame = 0

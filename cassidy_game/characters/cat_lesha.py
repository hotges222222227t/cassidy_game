# characters/cat_lesha.py
import pygame
import random

class CatLesha(pygame.sprite.Sprite):
    def __init__(self, spawn_points):
        super().__init__()
        self.images = self.load_animation("idle", 3)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=random.choice(spawn_points))
        self.spawn_points = spawn_points
        self.frame = 0
        self.frame_timer = 0
        self.animation_speed = 0.2
        self.visible = True
        self.timer = 0
        self.max_time = random.randint(300, 600)

    def load_animation(self, name, count):
        return [
            pygame.image.load(f"assets/images/cat_{name}_{i}.png").convert_alpha()
            for i in range(count)
        ]

    def update(self, dt):
        self.timer += 1
        self.frame_timer += dt

        if self.timer >= self.max_time:
            self.visible = not self.visible
            self.timer = 0
            self.max_time = random.randint(300, 600)
            if self.visible:
                self.rect.topleft = random.choice(self.spawn_points)

        if self.visible:
            if self.frame_timer >= self.animation_speed:
                self.frame_timer = 0
                self.frame = (self.frame + 1) % len(self.images)
                self.image = self.images[self.frame]
        else:
            self.image = pygame.Surface((0, 0))  # Прячем кошку

    def interact(self):
        print("Мяу! (Кошка даёт предмет)")
        # Здесь можно добавить механику подарка или реплики

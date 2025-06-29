import os

# Размеры экрана
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Папка с ассетами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
FONT_PATH = os.path.join(ASSETS_DIR, "fonts", "PressStart2P-Regular.ttf")  # Убедись, что шрифт на месте

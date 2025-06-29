# utils/telegram_music_loader.py
# Модуль для загрузки музыки с Telegram-бота или канала

import os
import requests
from dotenv import load_dotenv

# Загрузка конфигурации из .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DOWNLOAD_DIR = "assets/music"

HEADERS = {
    "User-Agent": "CassidyGameBot/1.0"
}


def get_telegram_file(file_id):
    """
    Получает ссылку на файл по его file_id из Telegram API.
    """
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getFile?file_id={file_id}"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        file_path = response.json()["result"]["file_path"]
        return f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}"
    except Exception as e:
        print(f"[Ошибка] Не удалось получить ссылку на файл: {e}")
        return None


def download_telegram_music(file_id, filename):
    """
    Загружает музыкальный файл из Telegram и сохраняет его в DOWNLOAD_DIR.
    """
    file_url = get_telegram_file(file_id)
    if not file_url:
        return None

    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()

        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        filepath = os.path.join(DOWNLOAD_DIR, filename)

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"[Успешно] Файл сохранён: {filepath}")
        return filepath
    except Exception as e:
        print(f"[Ошибка] Не удалось скачать файл: {e}")
        return None


# Пример запуска для теста
if __name__ == "__main__":
    test_file_id = "your_audio_file_id_here"
    filename = "telegram_track_1.ogg"
    download_telegram_music(test_file_id, filename)

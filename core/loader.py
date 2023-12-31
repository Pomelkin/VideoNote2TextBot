from aiogram import Bot, Dispatcher
from core.config import TELEGRAM_TOKEN
from faster_whisper import WhisperModel

model_size = "large-v3"

model = WhisperModel(model_size, device="cpu", compute_type="int8")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
from aiogram import Bot, Dispatcher
from core.config import TELEGRAM_TOKEN
import whisper

model = whisper.load_model("small")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
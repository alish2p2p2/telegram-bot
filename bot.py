from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import random

TOKEN = "7522644797:AAEWwbdhIeJYbNdPQq4A-k6uRRPYOz97QAo"

WORDS = [
    {"word": "Resilient", "translation": "устойчивый, стойкий", "example": "She is very resilient after all the hardships."},
    {"word": "Eager", "translation": "жаждущий, стремящийся", "example": "He is eager to learn new skills."},
    {"word": "Diligent", "translation": "прилежный, старательный", "example": "She is a very diligent student."}
]

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Напиши /word, чтобы получить слово!")

async def send_word(update: Update, context: CallbackContext) -> None:
    word_data = random.choice(WORDS)
    message = f"Word of the Day: {word_data['word']}\nTranslation: {word_data['translation']}\nExample: {word_data['example']}"
    await update.message.reply_text(message)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", send_word))
    app.run_polling()

if __name__ == "__main__":
    main()
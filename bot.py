import os
import signal
import sys
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Список карт Таро
CARDS = [
    "Шут", "Маг", "Верховная Жрица", "Императрица", "Император",
    "Иерофант", "Влюбленные", "Колесница", "Сила", "Отшельник",
    "Колесо Фортуны", "Справедливость", "Повешенный", "Смерть",
    "Умеренность", "Дьявол", "Башня", "Звезда", "Луна", "Солнце",
    "Суд", "Мир"
]

# URL вашего веб-приложения
WEBAPP_URL = "https://ove1an.github.io/taro/index.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        "Открыть расклад Таро",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Добро пожаловать в бот Таро!\nНажмите кнопку ниже, чтобы открыть расклад:',
        reply_markup=reply_markup
    )

def signal_handler(signum, frame):
    print("\nПолучен сигнал завершения. Останавливаем бота...")
    sys.exit(0)

def main():
    # Регистрируем обработчик сигналов
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Создаем и запускаем приложение
    application = Application.builder().token('7751942086:AAEc7V1UHwNR4wtoFNNyECzKr6AHRGHAc40').build()
    application.add_handler(CommandHandler("start", start))
    
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

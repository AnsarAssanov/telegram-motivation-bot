from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, Bot
from apscheduler.schedulers.background import BackgroundScheduler
import random

# Твой токен
TOKEN = '7883262290:AAE0tmmkfAON44ta7qZ7MPf-2Dw98GghWRs'

# Список для хранения ID всех пользователей
user_ids = set()

# 50+ мотивационных цитат
quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "You are capable of amazing things.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Don’t wait for opportunity. Create it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Little things make big days.",
    "Do something today that your future self will thank you for.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Keep pushing forward, no matter what.",
    "Stay positive. Work hard. Make it happen.",
    "Push harder than yesterday if you want a different tomorrow.",
    "Believe you can and you’re halfway there.",
    "Your only limit is your mind.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do what you can with all you have, wherever you are.",
    "Be so good they can’t ignore you.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Doubt kills more dreams than failure ever will.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Make each day your masterpiece.",
    "Work until your idols become your rivals.",
    "Success is what comes after you stop making excuses.",
    "Discipline is the bridge between goals and accomplishment.",
    "You don’t get what you wish for. You get what you work for.",
    "A little progress each day adds up to big results.",
    "If you get tired, learn to rest, not to quit.",
    "Hustle in silence and let your success make the noise.",
    "Act as if what you do makes a difference. It does.",
    "Opportunities don't happen. You create them.",
    "Nothing will work unless you do.",
    "The secret of getting ahead is getting started.",
    "Don't limit your challenges. Challenge your limits.",
    "Start where you are. Use what you have. Do what you can.",
    "The future depends on what you do today."
]

# Инициализация бота и планировщика
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
scheduler = BackgroundScheduler(timezone="UTC")

# Обработка команды /start
def start(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    user_ids.add(user_id)
    context.bot.send_message(chat_id=user_id, text="👋 Привет! Ты будешь получать мотивационные сообщения каждый час!")

# Функция отправки мотивации
def send_motivation():
    message = random.choice(quotes)
    for uid in user_ids:
        try:
            bot.send_message(chat_id=uid, text=message)
        except Exception as e:
            print(f"❌ Не удалось отправить пользователю {uid}: {e}")

# Добавляем задачи и команды
scheduler.add_job(send_motivation, 'interval', hours=1)
scheduler.start()

dispatcher.add_handler(CommandHandler('start', start))

# Запуск бота
print("Бот запущен. Нажмите Ctrl+C для остановки.")
updater.start_polling()
updater.idle()

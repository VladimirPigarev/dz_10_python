from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def loger(update: Update, context: ContextTypes):
   file = open('db.csv', 'a+', encoding="utf-8")
   file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
   file.close()
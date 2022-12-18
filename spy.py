from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def log_command(update: Update, context: ContextTypes):
   file = open('db.csv', 'a+')
   file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}')
   file.close()
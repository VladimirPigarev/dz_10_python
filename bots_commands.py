from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hi_command(update: Update, context: ContextTypes):
    log_command(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes):
    log_command(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def time_command(update: Update, context: ContextTypes):
    log_command(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    msg = update.messege.text
    print(msg)
    items = msg.split() # sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

# async def help_command(update: Update, context: ContextTypes):
#     await update.message.reply_text(f'')

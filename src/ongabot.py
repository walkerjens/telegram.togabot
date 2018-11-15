#!/usr/bin/env python3

import logging
import os

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.environ['API_TOKEN']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
  await bot.send_message(message.chat.id, 'All hail ON/GA')

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
  await bot.send_message(message.chat.id, 'TBD')

@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
  await bot.send_message(message.chat.id, 'No settings currently available')

@dp.message_handler(commands=['onga'])
async def onga(message: types.Message):
  with open('onga.jpg', 'rb') as photo:
    await bot.send_photo(message.chat.id, photo, caption='ON/GA is here 😺')

@dp.message_handler(commands=['newevent'])
async def new(message: types.Message):
  await bot.send_message(message.chat.id, 'Arguments:' + message.text[10:])

@dp.message_handler(commands=['status'])
async def status(message: types.Message):
  await bot.send_message(message.chat.id, 'Running... beep boop!\nActive events: 0')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)

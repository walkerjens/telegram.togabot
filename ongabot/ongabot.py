#!/usr/bin/env python3

import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler

from command.startcommand import StartCommandHandler
from command.helpcommand import HelpCommandHandler
from command.neweventcommand import NewEventCommandHandler
from command.ongacommand import OngaCommandHandler

API_TOKEN = os.environ['API_TOKEN']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, error)

def button(bot, update):
    query = update.callback_query
    editedMessageText = query.message.text + "\nSelected option: {}".format(query.data)

    keyboard = [[InlineKeyboardButton("17.30 - 0", callback_data='1')],
                [InlineKeyboardButton("18.30 - 0", callback_data='2')],
                [InlineKeyboardButton("19.30 - 0", callback_data='3')],
                [InlineKeyboardButton("20.30 - 0", callback_data='4')],
                [InlineKeyboardButton("noop - 0", callback_data='5')],
                [InlineKeyboardButton("maybe baby - 0", callback_data='6')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=editedMessageText,
                            reply_markup=reply_markup)

def main():
  """Setup and run ONGAbot"""
  updater = Updater(API_TOKEN)

  # Get the dispatcher to register handlers
  dp = updater.dispatcher
  dp.add_handler(StartCommandHandler())
  dp.add_handler(HelpCommandHandler())
  dp.add_handler(OngaCommandHandler())
  dp.add_handler(NewEventCommandHandler())
  dp.add_handler(CallbackQueryHandler(button))
  dp.add_error_handler(error)

  # Start the Bot
  updater.start_polling()

  # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
  # SIGABRT. This should be used most of the time, since start_polling() is
  # non-blocking and will stop the bot gracefully.
  updater.idle()


if __name__ == '__main__':
  main()

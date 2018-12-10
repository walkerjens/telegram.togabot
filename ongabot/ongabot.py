#!/usr/bin/env python3

import logging
import os

from telegram.ext import Updater

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

def main():
  """Setup and run ONGAbot"""
  updater = Updater(API_TOKEN)

  # Get the dispatcher to register handlers
  dp = updater.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(StartCommandHandler())
  dp.add_handler(HelpCommandHandler())
  dp.add_handler(OngaCommandHandler())
  dp.add_handler(NewEventCommandHandler())

  # log all errors
  dp.add_error_handler(error)

  # Start the Bot
  updater.start_polling()

  # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
  # SIGABRT. This should be used most of the time, since start_polling() is
  # non-blocking and will stop the bot gracefully.
  updater.idle()


if __name__ == '__main__':
  main()

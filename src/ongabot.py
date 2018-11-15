#!/usr/bin/env python3

import logging
import os

from telegram.ext import Updater, CommandHandler


API_TOKEN = os.environ['API_TOKEN']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, error)

# TODO: Extract commands into their own handlers and files
def startCommand(bot, update):
  """Print the help text for a /start or /help command"""
  helpText = "Welcome traveler, my name is ONGAbot.\n" \
             "I'm the one and only, the truth speaker.\n" \
             "\n" \
             "My duties are:\n" \
             " - Uphold the law, obviously, with weekly ON/GA polls\n" \
             " - Give praise to the faithful\n" \
             " - Aid the needing\n" \
             " - Condemn the wicked\n" \
             "\n" \
             "Commandments:\n" \
             "/help - To show this very helpful text\n" \
             "/onga - Print the image of the one\n" \
             "/newevent - Create a new event, args=TBD\n"

  update.message.reply_text(helpText)


def ongaCommand(bot, update):
  """Print the image of the one when the true word of /onga is spoken"""
  with open('onga.jpg', 'rb') as photo:
    update.message.reply_photo(photo, 'All are naked in front of the ONE!')


# TODO:
# [] Print message similar to other poll bots inc. options
# [] Add answer buttons
# [] Connect answer buttons to data
# [] Update original message with updated data
# [] Add status command to reprint active poll
# [] Cancel/close command
# [] Basic error handling if already exist a poll
# [] Add end time for a poll (auto close)
# [] Decide creation of poll (manual vs. automated)
# [] Persistent storage for current poll
# [] Multiple active polls
# [] Add custom polls (other than CS events)
# [] Add Configurable or random answer options
def neweventCommand(bot, update):
  """Create a poll as result of command /newevent"""
  titleText = "ON/GA time, 21/11 kl 17.30"
  infoText = "Insert priority here"

  message = '{}\n{}'.format(titleText, infoText)
  update.message.reply_text(message)


def main():
  """Setup and run ONGAbot"""
  updater = Updater(API_TOKEN)

  # Get the dispatcher to register handlers
  dp = updater.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("start", startCommand))
  dp.add_handler(CommandHandler("help", startCommand))
  dp.add_handler(CommandHandler("onga", ongaCommand))
  dp.add_handler(CommandHandler("newevent", neweventCommand))

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

#!/usr/bin/env python3

import logging
import os

from telegram.ext import PicklePersistence, Updater

from handler.startcommand import StartCommandHandler
from handler.helpcommand import HelpCommandHandler
from handler.neweventcommand import NewEventCommandHandler
from handler.ongacommand import OngaCommandHandler


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Setup and run ONGAbot"""
    API_TOKEN = os.getenv("API_TOKEN")
    DB_PATH = os.getenv("DB_PATH", "ongabot.db")
    pp = PicklePersistence(filename=DB_PATH)
    updater = Updater(API_TOKEN, persistence=pp, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(StartCommandHandler())
    dp.add_handler(HelpCommandHandler())
    dp.add_handler(OngaCommandHandler())
    dp.add_handler(NewEventCommandHandler())
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()

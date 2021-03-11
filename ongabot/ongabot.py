#!/usr/bin/env python3

import logging
import os

from telegram.ext import PicklePersistence, Updater

from handler.startcommand import StartCommandHandler
from handler.helpcommand import HelpCommandHandler
from handler.neweventcommand import NewEventCommandHandler
from handler.ongacommand import OngaCommandHandler
from handler.eventpollhandler import EventPollHandler
from handler.eventpollanswerhandler import EventPollAnswerHandler


logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Setup and run ONGAbot"""
    persistence = PicklePersistence(filename=os.getenv("DB_PATH", "ongabot.db"))

    updater = Updater(os.getenv("API_TOKEN"), persistence=persistence, use_context=True)

    # Register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(StartCommandHandler())
    dispatcher.add_handler(HelpCommandHandler())
    dispatcher.add_handler(OngaCommandHandler())
    dispatcher.add_handler(NewEventCommandHandler())
    dispatcher.add_handler(EventPollHandler())
    dispatcher.add_handler(EventPollAnswerHandler())
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()

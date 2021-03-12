"""This module contains the StartCommandHandler class."""
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

import utils.helper as helper


class StartCommandHandler(CommandHandler):
    """Handler for /start command"""

    def __init__(self):
        CommandHandler.__init__(self, "start", callback)


def callback(update: Update, _: CallbackContext):
    """Print the help text for a /start or /help command"""
    update.message.reply_text(helper.create_help_text())

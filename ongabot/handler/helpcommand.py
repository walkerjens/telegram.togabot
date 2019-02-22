from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

import handler.helper as helper


class HelpCommandHandler(CommandHandler):
    def __init__(self):
        CommandHandler.__init__(self, "help", self.helpCommand)

    def helpCommand(self, update: Update, context: CallbackContext):
        """Print the help text for a /start or /help command"""
        update.message.reply_text(helper.helpText())

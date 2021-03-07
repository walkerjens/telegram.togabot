from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

import handler.helper as helper


class NewEventCommandHandler(CommandHandler):
    def __init__(self):
        CommandHandler.__init__(self, "newevent", self.neweventCommand)

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
    def neweventCommand(self, update: Update, context: CallbackContext):
        """Create a poll as result of command /newevent"""
        message = update.message
        text = helper.assembleEventHeader("None")
        options = helper.assembleEventButtons()
        message.reply_poll(text, options=options, quote=False, is_anonymous=False, allows_multiple_answers=True)

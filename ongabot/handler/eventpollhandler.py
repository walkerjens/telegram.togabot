import logging

from telegram import Update
from telegram.ext import PollHandler, CallbackContext


class EventPollHandler(PollHandler):
    def __init__(self):
        PollHandler.__init__(self, callback=self.callback)

    def callback(self, update: Update, context: CallbackContext):
        """Handle an poll update"""
        logger = logging.getLogger()
        logger.debug("ENTER: EventPollHandler::callback")
        logger.debug("update:")
        logger.debug("{}".format(update))

        # Update stored poll_data
        poll_data = context.bot_data[update.poll.id]
        poll_data["poll"] = update.poll
        context.bot_data.update(poll_data)

        logger.debug("context.bot_data")
        logger.debug("{}".format(context.bot_data))
        logger.debug("EXIT: EventPollHandler::callback")

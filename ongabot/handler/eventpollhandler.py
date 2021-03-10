import logging

from telegram import Update
from telegram.ext import PollHandler, CallbackContext


class EventPollHandler(PollHandler):
    def __init__(self):
        PollHandler.__init__(self, callback=self.callback)

    def callback(self, update: Update, context: CallbackContext):
        """Handle an poll update"""
        logger = logging.getLogger()
        logger.info("ENTER: PollHandler callback")
        logger.info("update content:")
        logger.info("{}".format(update))
        logger.info("context.bot_data")
        logger.info("{}".format(context.bot_data))
        logger.info("{}".format(context.bot_data[update.poll.id]["poll"]))
        context.bot_data[update.poll.id]["poll"] = update.poll
        logger.info("{}".format(context.bot_data))
        logger.info("{}".format(context.bot_data[update.poll.id]["poll"]))

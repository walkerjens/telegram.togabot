import logging

from telegram import Update
from telegram.ext import PollAnswerHandler, CallbackContext


class EventPollAnswerHandler(PollAnswerHandler):
    def __init__(self):
        PollAnswerHandler.__init__(self, callback=self.callback)

    def callback(self, update: Update, context: CallbackContext):
        """Handle an poll update"""
        logger = logging.getLogger()
        logger.info("ENTER: PollAnswerHandler callback")
        logger.info("update content:")
        logger.info("{}".format(update))
        logger.info("context.chat_data:")
        logger.info("{}".format(context.bot_data))
        logger.info("{}".format(context.user_data))

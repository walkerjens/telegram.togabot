import logging

from telegram import Update
from telegram.ext import PollAnswerHandler, CallbackContext


class EventPollAnswerHandler(PollAnswerHandler):
    def __init__(self):
        PollAnswerHandler.__init__(self, callback=self.callback)

    def callback(self, update: Update, context: CallbackContext):
        """Handle an poll update"""
        logger = logging.getLogger()
        logger.debug("ENTER: EventPollAnswerHandler::callback")
        logger.debug("update:")
        logger.debug("{}".format(update))

        # Store poll answer in user_data
        user_data = {
            "user": update.poll_answer.user,
            "poll_answers": {
                update.poll_answer.poll_id: {
                    "poll_answer": update.poll_answer.option_ids,
                },
            },
        }
        context.user_data.update(user_data)

        context.bot.send_message(
            context.bot_data[update.poll_answer.poll_id]["chat_id"],
            "Wow {}, what a great job answering that poll!".format(
                user_data["user"].name
            ),
        )

        logger.debug("context.user_data")
        logger.debug("{}".format(context.user_data))
        logger.debug("EXIT: EventPollAnswerHandler::callback")

import logging

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


class NewEventCommandHandler(CommandHandler):
    def __init__(self):
        CommandHandler.__init__(self, "newevent", self.neweventCommand)

    def neweventCommand(self, update: Update, context: CallbackContext):
        """Create a poll as result of command /newevent"""
        text = generateText()
        options = generateOptions()
        message = context.bot.send_poll(
            update.effective_chat.id,
            text,
            options=options,
            is_anonymous=False,
            allows_multiple_answers=True,
        )

        # Store the new poll in bot_data
        poll_data = {
            message.poll.id: {
                "chat_id": update.effective_chat.id,
                "poll": message.poll,
            }
        }
        context.bot_data.update(poll_data)
        logger = logging.getLogger()
        logger.info("message content:")
        logger.info("{}".format(message))
        logger.info("{}".format(context.bot_data))


def generateText():
    titleText = "Event: ONGA"
    whenText = "When: <insert date>"
    statusText = (
        "<insert text about current size of squad or number of missing players>"
    )
    message = "{}\n{}\n{}".format(titleText, whenText, statusText)
    return message


def generateOptions():
    options = [
        "17.30",
        "18.30",
        "19.30",
        "20.30",
        "No-op",
        "Maybe Baby <3",
    ]

    return options

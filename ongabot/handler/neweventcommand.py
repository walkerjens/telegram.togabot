import logging
from datetime import date, timedelta

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


class NewEventCommandHandler(CommandHandler):
    def __init__(self):
        CommandHandler.__init__(self, "newevent", self.callback)

    def callback(self, update: Update, context: CallbackContext):
        """Create a poll as result of command /newevent"""
        logger = logging.getLogger()
        logger.debug("ENTER: NewEventCommandHandler::callback")
        logger.debug("update:")
        logger.debug("{}".format(update))

        text = generateText()
        options = generateOptions()
        message = context.bot.send_poll(
            update.effective_chat.id,
            text,
            options=options,
            is_anonymous=False,
            allows_multiple_answers=True,
        )

        logger.debug("message:")
        logger.debug("{}".format(message))

        # Store the new poll in bot_data
        poll_data = {
            message.poll.id: {
                "chat_id": update.effective_chat.id,
                "poll": message.poll,
            }
        }
        context.bot_data.update(poll_data)

        logger.debug("context.bot_data")
        logger.debug("{}".format(context.bot_data))
        logger.debug("EXIT: NewEventCommandHandler::callback")


def generateText():
    titleText = "Event: ONGA"
    whenText = f"When: {getUpcomingWednesdayDate(date.today())}"
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


def getUpcomingWednesdayDate(today):
    wednesday_day_of_week_index = 2  # 0-6, 0 is monday and 6 is sunday
    next_wednesday_date = today + timedelta((wednesday_day_of_week_index - today.weekday()) % 7)
    return next_wednesday_date
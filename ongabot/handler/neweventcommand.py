from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


class NewEventCommandHandler(CommandHandler):
    def __init__(self):
        CommandHandler.__init__(self, "newevent", self.neweventCommand)

    def neweventCommand(self, update: Update, context: CallbackContext):
        """Create a poll as result of command /newevent"""
        message = update.message
        text = generateText()
        options = generateOptions()
        message.reply_poll(text, options=options, quote=False, is_anonymous=False, allows_multiple_answers=True)


def generateText():
    titleText = "Event: ONGA"
    whenText = "When: <insert date>"
    statusText = "<insert text about current size of squad or number of missing players>"
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

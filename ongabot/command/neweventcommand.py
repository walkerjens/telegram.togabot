from telegram.ext import CommandHandler

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
    def neweventCommand(self, bot, update):
        """Create a poll as result of command /newevent"""
        titleText = "ON/GA time, 21/11 kl 17.30"
        infoText = "Insert priority here"

        message = '{}\n{}'.format(titleText, infoText)
        update.message.reply_text(message)
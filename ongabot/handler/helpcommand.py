import handler.helper as helper

from telegram.ext import CommandHandler

class HelpCommandHandler(CommandHandler):
  def __init__(self):
    CommandHandler.__init__(self, "help", self.helpCommand)

  # TODO: Extract commands into their own handlers and files
  def helpCommand(self, bot, update):
    """Print the help text for a /start or /help command"""
    update.message.reply_text(helper.helpText())

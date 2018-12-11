from telegram.ext import CommandHandler

class OngaCommandHandler(CommandHandler):
  def __init__(self):
    CommandHandler.__init__(self, "onga", self.ongaCommand)

  def ongaCommand(self, bot, update):
    """Print the image of the one when the true word of /onga is spoken"""
    with open('onga.jpg', 'rb') as photo:
      update.message.reply_photo(photo, 'All are naked in front of the ONE!')
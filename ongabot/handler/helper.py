from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def assembleEventHeader(selected):
  titleText = "ON/GA time, 21/11 kl 17.30"
  infoText = "Insert priority here"
  selectionText = "Selected: {}".format(selected)
  message = '{}\n{}\n{}'.format(titleText, infoText, selectionText)
  return message

def assembleEventButtons():
  keyboard = [[InlineKeyboardButton("17.30 - 0", callback_data='1')],
              [InlineKeyboardButton("18.30 - 0", callback_data='2')],
              [InlineKeyboardButton("19.30 - 0", callback_data='3')],
              [InlineKeyboardButton("20.30 - 0", callback_data='4')],
              [InlineKeyboardButton("noop - 0", callback_data='5')],
              [InlineKeyboardButton("maybe baby - 0", callback_data='6')]]

  reply_markup = InlineKeyboardMarkup(keyboard)
  return reply_markup

def helpText():
    """Print the help text for a /start or /help command"""
    helpText = "Welcome traveler, my name is ONGAbot.\n" \
                "I'm the one and only, the truth speaker.\n" \
                "\n" \
                "My duties are:\n" \
                " - Uphold the law, obviously, with weekly ON/GA polls\n" \
                " - Give praise to the faithful\n" \
                " - Aid the needing\n" \
                " - Condemn the wicked\n" \
                "\n" \
                "Commandments:\n" \
                "/help - To show this very helpful text\n" \
                "/onga - Print the image of the one\n" \
                "/newevent - Create a new event, args=TBD\n"

    return helpText


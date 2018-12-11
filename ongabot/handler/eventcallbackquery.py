import handler.helper as helper

from telegram.ext import CallbackQueryHandler


class EventCallbackQueryHandler(CallbackQueryHandler):
  def __init__(self):
    CallbackQueryHandler.__init__(self, self.eventCallback)

  def eventCallback(self, bot, update):
    query = update.callback_query
    message = helper.assembleEventHeader(query.data)
    reply_markup = helper.assembleEventButtons()
    query.edit_message_text(text=message,
                            reply_markup=reply_markup)

        
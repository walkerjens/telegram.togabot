import handler.helper as helper

from telegram.ext import CallbackQueryHandler


class EventCallbackQueryHandler(CallbackQueryHandler):
  def __init__(self):
    CallbackQueryHandler.__init__(self, self.eventCallback)

  def eventCallback(self, bot, update):
    query = update.callback_query
    if query.data == '6':
      bot.delete_message(query.message.chat_id, 
                         query.message.message_id)

    else:
      text = helper.assembleEventHeader(query.data)
      reply_markup = helper.assembleEventButtons()
      query.edit_message_text(text=text,
                              reply_markup=reply_markup)

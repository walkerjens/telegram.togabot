import logging

from telegram import Update
from telegram.ext import CallbackQueryHandler, CallbackContext

import handler.helper as helper


class EventCallbackQueryHandler(CallbackQueryHandler):
    def __init__(self):
        CallbackQueryHandler.__init__(self, self.eventCallback)

    def eventCallback(self, update: Update, context: CallbackContext):
        logger = logging.getLogger()
        logger.info("{}".format(context.user_data))
        logger.info("{}".format(context.chat_data))
        query = update.callback_query
        logger.info("{}".format(query))
        if query.data == "6":
            context.bot.delete_message(query.message.chat_id, query.message.message_id)

        else:
            text = helper.assembleEventHeader(query.data)
            reply_markup = helper.assembleEventButtons()
            query.edit_message_text(text=text, reply_markup=reply_markup)

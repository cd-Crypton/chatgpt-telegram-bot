# This script were written using python-telegram-bot (v20.1)

# Setting up system environment
import openai
import os
import logging

from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union
from telegram import Update
from telegram._utils.defaultvalue import DEFAULT_TRUE
from telegram._utils.types import DVType
from telegram.ext import filters as filters_module
from telegram.ext._handler import BaseHandler
from telegram.ext._utils.types import CCT, HandlerCallback
from telegram.ext import ApplicationBuilder, ContextTypes

# Fetch OpenAI API key and Telegram Bot token from environment variables
openai_api_key = os.environ.get('OPENAI_KEY')
openai.api_key = openai_api_key
telegram_bot_token = os.environ.get('TELEGRAM_TOKEN')

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if TYPE_CHECKING:
    from telegram.ext import Application

RT = TypeVar("RT")

class MessageHandler(BaseHandler[Update, CCT]):

    __slots__ = ("filters",)
 
    def __init__(
        self,
        filters: filters_module.BaseFilter,
        callback: HandlerCallback[Update, CCT, RT],
        block: DVType[bool] = DEFAULT_TRUE,
    ):
        super().__init__(callback, block=block)
        self.filters: filters_module.BaseFilter = (
            filters if filters is not None else filters_module.ALL
        )

    def check_update(self, update: object) -> Optional[Union[bool, Dict[str, List[Any]]]]:
        if isinstance(update, Update):
            return self.filters.check_update(update) or False
        return None


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    
    # Make "typing..." status visible under bots name
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    
    # Use OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{user_input}\n",
        max_tokens=2048
    )
    # Send the response back to the user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response["choices"][0]["text"])
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Any more questions?")

if __name__ == "__main__":
    # Create the Telegram bot instance
    application = ApplicationBuilder().token(telegram_bot_token).build()
    
    # Register the message handler
    handler = MessageHandler(filters=None, callback=handle_message)
    application.add_handler(handler)
    # Start the bot
    application.run_polling()

#!/bin/bash

export OPENAI_API="<your-openai-api-key-here>"
export TELEGRAM_TOKEN="<your-telegram-bot-token-here>"

echo "Done setting up environment variables."

echo "Will now run the bot..."

python3 ./chatgpt_bot.py

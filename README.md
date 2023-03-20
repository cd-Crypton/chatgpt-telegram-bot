Template for ChatGPT Telegram Bot | Written via Python-Telegram-Bot

### Run it Yourself
Setup Bot and OpenAI:
* Create Bot using [@BotFather](https://t.me/BotFather). Name it any name you want.
* Once you've created the bot, it will give you an API token. Keep this token safe, as you'll need it later.
* Create an account in https://platform.openai.com/, and got to your Profile and click View API Keys. Generate new key, and save it.
* Clone this repository to get `chatgpt_bot.py` and `secrets.sh`.

Setup Local Environment:
* Do `sudo apt-get install python3` (or depends on your OS how, just make sure it has python installed), skip this if part if you already have.
* Then run this `pip install python-telegram-bot --upgrade`.
* Go to root directory of the cloned repository, and open `secrets.sh` via Text Editor.
* Replace `<your-openai-api-key-gere>` and `<your-telegram-bot-token>` with your own.
* Now, open your Terminal in the root directory, where `chatgpt_bot.py` and `run.sh` were saved.
* In terminal, run `source ./run.sh`.
* If you didn't recieve any error, and you see something like this: `XXXX-XX-XX - telegram.ext._application - INFO - Application started`.
* The bot is now live, so ask a question.
* Ctrl+C to stop it from running.

Since this is a local setup, once you close the terminal, the bot will not be able to answer your question anymore. You can publish it via server, or via other means. At this point, it's now up to you.

This script was also published in Replit: [ChatGPT Telegram Bot - Replit](https://replit.com/@CarloDee/ChatGPT-Telegram-Bot)

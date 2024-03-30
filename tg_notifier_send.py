import sys, os
from telegram_notifier_bot import Notifier

__author__ = 'p4irin'
__email__ = 'p4irin.github.io@gmail.com'

github_output = os.getenv('GITHUB_OUTPUT')
telegram_bot_token = sys.argv[1]
telegram_chat_id = sys.argv[2]
message = sys.argv[3]

notifier = Notifier(telegram_bot_token)
response = notifier.send(notification=message, to_chat_id=telegram_chat_id)

if github_output:
    with open(github_output, 'a') as gh_env_file:
        gh_env_file.write(f'tg_response={response.content}')
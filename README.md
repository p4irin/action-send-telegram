[![Test action-send-telegram](https://github.com/p4irin/action-send-telegram/actions/workflows/test_action.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/p4irin/action-send-telegram/actions/workflows/test_action.yml)

# Send Telegram action

Send a message to a Telegram user or group from within a GitHub Actions workflow

## Prerequisite

Get a Telegram bot token and the chat-id of the user/group you want to send a message to: [Create a new Telegram bot](https://core.telegram.org/bots/features#creating-a-new-bot)

## Inputs

### `telegram-bot-token`

**Required** Your Telegram bot token.

### `telegram-chat-id`

**Required** The chat-id of a Telegram user or group

### `message`

**Required** Your text message

## Outputs

### `telegram_response`

The response from Telegram

## Example usage

```
uses: p4irin/action-send-telegram@v1
with:
  telegram-bot-token: ${{ secrets.TELEGRAM_BOT_TOKEN }}
  telegram-chat-id: ${{ secrets.TELEGRAM_CHAT_ID}}
  message: 'Your message here'
```
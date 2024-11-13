from telethon import TelegramClient, events

# Replace with your actual API ID, API Hash, and Bot Token
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Initialize both clients
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
user = TelegramClient('user', api_id, api_hash)

# Send startup messages
async def send_startup_messages():
    await user.send_message('me', 'User client started and active!')

# Bot welcome message with greeting
@bot.on(events.NewMessage(pattern='/start'))
async def bot_welcome(event):
    await event.respond("Welcome Telethonians! How are you? Here’s our GitHub link: https://github.com/Telethonian/Telethonian")
    print("Bot received /start command")

# Echo functionality for specific words
@bot.on(events.NewMessage(pattern='/echo (.+)'))
async def bot_echo(event):
    text = event.pattern_match.group(1)
    if text.lower() in ['hi', 'hello']:
        await event.respond(f'You said: {text}')
    else:
        await event.respond(f'Echo: {text}')

# Ping response for user client
@user.on(events.NewMessage(pattern='/ping'))
async def user_ping(event):
    await event.reply("Pong!")

# User client welcome response with additional greetings
@user.on(events.NewMessage(outgoing=True, pattern=r"(Hi|Hey|Hello|Ciao)"))
async def user_greeting(event):
    await event.reply("Welcome Telethonians! How are you? Here’s our GitHub link: https://github.com/Telethonian/Telethonian")

# Main function to start clients and send startup messages
async def main():
    await user.start()
    await send_startup_messages()
    print("User and Bot clients are now online.")

bot.loop.run_until_complete(main())

# Run both clients until disconnected
bot.run_until_disconnected()
user.run_until_disconnected()

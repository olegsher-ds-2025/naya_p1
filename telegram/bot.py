from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Your bot token from BotFather
TOKEN = '7265686775:AAHvlpXuwR53HX7u2TAqxxecAUV2CJxqgRI'

# Function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! I am your simple Telegram bot.')

# Function to handle text messages
def handle_message(update, context):
    user_message = update.message.text
    update.message.reply_text(f'You said: {user_message}')

# Function to handle unknown commands
def unknown(update, context):
    update.message.reply_text('Sorry, I didn’t understand that command.')

def main():
    # Create an Updater object and Dispatcher
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handler for /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Add message handler for regular text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Add handler for unknown commands
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the bot
    updater.start_polling()
    updater.idle()  # Keep the bot running until stopped

if __name__ == '__main__':
    main()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, filters
from api import work_with_series


# Your bot token from BotFather
TOKEN: str = '7265686775:AAHvlpXuwR53HX7u2TAqxxecAUV2CJxqgRI'
DEV_BOT_TOKEN: str = '7529871846:AAG16iO9f1vn5-0Vq1CYfV30HMKkn5w44yM'
rate = work_with_series()[2]
date_of_course = work_with_series()[1]
l_currencies = [key for key in rate.keys()]


# Function to handle the /start command
def start(update, context) -> None:
    update.message.reply_text('Hello! I am your simple Telegram Currency rate bot.')
    update.message.reply_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6mHwMCHABuF4qIQkUphrfhdJQTvYJKLGxhvCBdoypb63HQpRgTOTdZEzwZk6g7R2nEG8&usqp=CAU')

# Function to handle text messages
def handle_message(update, context) -> None:
    user_message = update.message.text
    if user_message in l_currencies:
        update.message.reply_text(f'1 EUR is equal {rate[user_message]} {user_message} for {date_of_course}')
    else:
        update.message.reply_text(f'You said: {user_message}')


# Function to handle unknown commands
def unknown(update, context) -> None:
    update.message.reply_text('Sorry, I didn’t understand that command.')

def main() -> None:
    # print(z.get(' USD'))
    # Create an Updater object and Dispatcher
    updater = Updater(DEV_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()
    updater.idle()  # Keep the bot running until stopped




if __name__ == '__main__':
    main()
    
    

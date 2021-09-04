from telegram import *
from telegram.ext import *
from datetime import datetime

bot =Bot("1899329169:AAEQGWcJBFmP_nPFc46JtO1p6MoNmPvjwHc")
updater=Updater("1899329169:AAEQGWcJBFmP_nPFc46JtO1p6MoNmPvjwHc",use_context=True)
dispatcher=updater.dispatcher
print("Bot started...")

def responses(intput_text):
	user_message=str(intput_text).lower()

	if user_message in ("hello", "hi", "sup",):
		return "Hi Coder,Welcome!"  
	if user_message in ("who are you", "who are you?"):
		return "Hi,I am the coder bot! How can I help you ??"

	if user_message in ("time"," time ?"):
		now=datetime.now();
		date_time=now.strftime("%d/%m/%y , %H:%M:%S")
		return str(date_time)

	return "Sorry ,I couldn't understand🐒 My bad "	



def start_command(update,context):
	update.message.reply_text('Type Something To Get Start!')

def help_command(update,context):
	update.message.reply_text('Sorry, I have no answer for this,I am still learning')


def handle_message(update,context):
	text=str(update.message.text).lower()
	response=responses(text)
	update.message.reply_text(response)

def error(update,context):
	print(f"Update {update} caused error{context.error}")



def merge_function(update:Update,context:CallbackContext):
	bot.send_message(

		chat_id=update.effective_chat.id,
		text="Vedio Link:- https://youtu.be/JSceec-wEyw",
		)


start_value=CommandHandler('merge_sort',merge_function)
 
def function(update:Update,context:CallbackContext):
	bot.send_message(

		chat_id=update.effective_chat.id,
		text="Hello,What's going On ?",
		)


start_value1=CommandHandler('hello',function)
 


def main():
	
    

    dispatcher.add_handler(start_value)
    dispatcher.add_handler(start_value1)

    dispatcher.add_handler(CommandHandler("start",start_command))
    dispatcher.add_handler(CommandHandler("help",help_command))
    dispatcher.add_handler(MessageHandler(Filters.text,handle_message))

    updater.start_polling()
    updater.idle()


main()







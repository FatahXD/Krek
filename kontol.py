import os,sys
try:
	from telegram import Update
	from telegram.ext import Application, CommandHandler, ContextTypes
except:
	os.system("pip install telegram python-telegram-bot")
# Ganti 'YOUR_BOT_TOKEN' dengan token API bot Anda
TOKEN = '7219906671:AAFMDWP4ezAGrYkckMDCeW4xMGSRlwA65J8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Termux bot.')

async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = ' '.join(context.args)
    if command:
        import os
        result = os.popen(command).read()
        await update.message.reply_text(f'Output:\n{result}')
    else:
        await update.message.reply_text('No command provided.')

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('exec', execute))

    application.run_polling()

if __name__ == '__main__':
    main()

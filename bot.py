import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Bot configuration
BOT_TOKEN = "8093224011:AAHP9OlpEkyg44nfCUf2rjyINutqMHw1IBM"
CHANNEL = "your_channel"  # Replace with your channel username
GROUP = "your_group"      # Replace with your group username
TWITTER = "your_twitter"  # Replace with your Twitter username

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL}")],
        [InlineKeyboardButton("👥 Join Group", url=f"https://t.me/{GROUP}")],
        [InlineKeyboardButton("🐦 Follow Twitter", url=f"https://twitter.com/{TWITTER}")],
        [InlineKeyboardButton("💰 SUBMIT SOL WALLET", callback_data="submit_wallet")]
    ]
    await update.message.reply_text(
        "🎉 SOL Airdrop Bot 🎉\n\n"
        "To qualify for 10 SOL airdrop:\n"
        "1. Join our channel\n"
        "2. Join our group\n"
        "3. Follow our Twitter\n"
        "4. Submit your SOL wallet address\n\n"
        "Click the button below when ready:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_submission(update: Update, context: CallbackContext) -> None:
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("⬇️ Enter your Solana wallet address:")

async def process_wallet(update: Update, context: CallbackContext) -> None:
    wallet = update.message.text
    await update.message.reply_text(
        f"🚀 Congratulations! 10 SOL is on its way to:\n\n`{wallet}`\n\n"
        "💡 Note: This is a test transaction. No actual SOL will be sent.",
        parse_mode="Markdown"
    )

def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_submission, pattern="^submit_wallet$"))
    app.add_handler(MessageHandler(None, process_wallet))
    
    # Run with webhook for Render
    port = int(os.environ.get("PORT", 5000))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=BOT_TOKEN,
        webhook_url=f"https://your-render-app.onrender.com/{BOT_TOKEN}"
    )

if __name__ == "__main__":
    main()

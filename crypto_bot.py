
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

TOKEN = "8060903040:AAFy5FEEikLpeSNuTheH75zhhFIPmR7EM5Q"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📉 قیمت رمزارز", callback_data="price")],
        [InlineKeyboardButton("📰 اخبار مهم روز", callback_data="news")],
        [InlineKeyboardButton("🐋 تحلیل نهنگ‌ها", callback_data="whales")],
        [InlineKeyboardButton("📊 اخبار اقتصادی", callback_data="economy")],
        [InlineKeyboardButton("🪙 جستجوی توکن", callback_data="token")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("یه دکمه انتخاب کن:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "price":
        await query.edit_message_text("مثلاً قیمت لحظه‌ای بیت‌کوین: BTC $...")
    elif query.data == "news":
        await query.edit_message_text("تازه‌ترین اخبار بازار کریپتو...")
    elif query.data == "whales":
        await query.edit_message_text("تحلیل نهنگ‌های بازار...")
    elif query.data == "economy":
        await query.edit_message_text("اخبار مهم اقتصاد جهانی...")
    elif query.data == "token":
        await query.edit_message_text("اسم توکن رو بفرست تا اخبارش بیاد. مثال: ETH")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("ربات راه‌اندازی شد")
    app.run_polling()

if __name__ == "__main__":
    main()

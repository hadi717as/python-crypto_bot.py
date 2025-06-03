import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

    TOKEN = "8060903040:AAFy5FEEikLpeSNuTheH75zhhFIPmR7EM5Q"

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("📈 قیمت و چارت", callback_data='price')],
            [InlineKeyboardButton("📰 اخبار مهم بازار", callback_data='news')],
            [InlineKeyboardButton("🐋 اخبار نهنگی", callback_data='whales')],
            [InlineKeyboardButton("💵 اخبار اقتصادی", callback_data='economy')],
            [InlineKeyboardButton("🔍 جستجوی خبر توکن", callback_data='token')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("به ربات کریپتوی شخصی خوش اومدی! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=reply_markup)

    async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "price":
            await query.edit_message_text("لطفاً نماد ارز دیجیتال رو ارسال کن. مثال: BTC")
        elif query.data == "news":
            await query.edit_message_text("📢 آخرین اخبار مهم بازار:
(در این نسخه اولیه فقط نمونه‌ها نمایش داده می‌شود)")
        elif query.data == "whales":
            await query.edit_message_text("🔍 آخرین فعالیت‌های نهنگ‌ها:
(در این نسخه اولیه فقط نمونه‌ها نمایش داده می‌شود)")
        elif query.data == "economy":
            await query.edit_message_text("💼 آخرین اخبار اقتصادی جهانی:
(در این نسخه اولیه فقط نمونه‌ها نمایش داده می‌شود)")
        elif query.data == "token":
            await query.edit_message_text("🔍 لطفاً نماد ارزی که می‌خوای خبرش رو ببینی وارد کن. مثال: ETH")

    def main():
        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button))

        print("ربات آماده اجراست.")
        app.run_polling()

    if __name__ == '__main__':
        main()

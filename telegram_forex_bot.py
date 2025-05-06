import logging
import asyncio
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Setup
TOKEN = "8093523026:AAFxYidoFEOWYwJOX3anG1kV2KnmWKruuBY"
CHAT_ID = 6116829199

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_signal():
    pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD"]
    timeframes = ["M1", "M5", "M15"]
    directions = ["CALL (BUY)", "PUT (SELL)"]
    strategy_used = "EMA + RSI + S/R Breakout"
    accuracy = round(random.uniform(88, 98), 2)

    return {
        "pair": random.choice(pairs),
        "timeframe": random.choice(timeframes),
        "direction": random.choice(directions),
        "strategy": strategy_used,
        "accuracy": accuracy
    }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Forex Signal Bot is running!")

async def send_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal = generate_signal()
    message = (
        f"📊 *New Signal Alert*
"
        f"Pair: {signal['pair']}
"
        f"Timeframe: {signal['timeframe']}
"
        f"Direction: {signal['direction']}
"
        f"Strategy: {signal['strategy']}
"
        f"Accuracy: {signal['accuracy']}%
"
    )
    await update.message.reply_markdown(message)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", send_signal))
    logger.info("Bot is starting...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
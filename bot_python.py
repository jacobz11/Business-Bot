import os
import telebot
from telebot import types

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
@bot.message_handler(commands=["start"])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=1)  # Single-column for longer buttons
    diary = types.InlineKeyboardButton('לחץ כאן לספר "המדריך היומי לניהול תקציב משפחתי"', url="https://hagitbenporat.ravpage.co.il/BOOK")#3
    tiktok = types.InlineKeyboardButton("לTikTok של חגית בן פורת", url="https://www.tiktok.com/@hagitvqa6qi?_t=8s4S8dEPQlS&_r=1")
    youtube = types.InlineKeyboardButton("לYouTube של חגית בן פורת", url="https://youtube.com/channel/UC2J4mn-KQKIkscdckbbn1WQ?si=CDFZe-Z8S4XEpNqx")
    webinar = types.InlineKeyboardButton("לחץ כאן להצטרפות לכנס וובינר הקרוב", url="https://hagitbenporat.ravpage.co.il/kenes6")
    whatsapp_group = types.InlineKeyboardButton("קבוצת ווצאפ - טיפים ותוכן לניהול הכסף", url="https://chat.whatsapp.com/G38UDoWuFkj4a4CAshhsS2")
    recommend = types.InlineKeyboardButton("לחץ כאן לצפייה בהמלצות מלקוחות ועדויות", url="https://hagitbenporat.ravpage.co.il/edut")
    private_whatsapp = types.InlineKeyboardButton("לחץ כאן לשיחת ווצאפ עם חגית", url="https://wa.me/972544923802")
    markup.add(diary, tiktok, youtube, webinar, whatsapp_group, recommend, private_whatsapp)

    bot.send_message(message.chat.id, "שלום, אני הבוט של חגית בן פורת. איך אוכל לסייע?🙂", reply_markup=markup)#1

bot.polling()
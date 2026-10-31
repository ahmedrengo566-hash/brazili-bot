import logging
import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8887904786:AAEidXt-3_zHhoRepYrnkbYfcXRw7g-3gmc"

logging.basicConfig(level=logging.INFO)

jokes = [
    "مرة واحد نام متأخر فاته الحلم 😂",
    "مرة كمبيوتر اتجوز خلف داتا 😂",
    "الجدع جدع حتى لو لابس شبشب 🐍",
    "مرة واحد محشش دخل مدرسة سألوه عن تاريخ اليوم قالهم مكسور شوية 😂"
]

# 1. أوامر البداية والمساعدة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ أهلاً بيك في بوت البرازيلي المتطور 🐍\n"
        "كبير الروم وصل.. اكتب /help لعرض كل الأوامر الإدارية والترفيهية والالعاب 😂"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐍 قائمة أوامر البرازيلي الشاملة:\n\n"
        "🎮 **أوامر ترفيهية وألعاب:**\n"
        "/joke - نكتة عشوائية تضحكك\n"
        "/quiz - فزورة سريعة لتشغيل دماغك\n"
        "/rules - قوانين الروم المهمة\n"
        "/play <اسم الأغنية> - تشغيل أو البحث عن أغنية\n"
        "/roll - رمي زهر عشوائي (من 1 لـ 6)\n\n"
        "🛡️ **أوامر الإدارة (تستخدم بالرد على الرسالة):**\n"
        "/ban - حظر العضو من الروم\n"
        "/kick - طرد العضو\n"
        "/mute - كتم العضو في الجروب\n"
        "/unmute - إلغاء كتم العضو\n"
        "/delete - حذف الرسالة المردود عليها"
    )

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(jokes))

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.chat_data["answer"] = "القاهرة"
    await update.message.reply_text("🧠 مسابقة ذكاء سريعة:\nما عاصمة مصر؟ (اكتب الإجابة في الشات)")

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 قوانين روم البرازيلي:\n"
        "1- الاحترام المتبادل بين الأعضاء\n"
        "2- ممنوع الإزعاج أو السب والشتم\n"
        "3- ممنوع نشر الروابط بدون إذن الإدارة\n"
        "4- اسمع كلام الإدارة دائماً 😂"
    )

async def roll_dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 6)
    await update.message.reply_text(f"🎲 النرد رمى وطلع لك رقم: **{number}** يا أسطورة!")

# 2. أمر تشغيل الأغاني
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🎵 يا حب، اكتب اسم الأغنية بعد الأمر، مثل:\n`/play عمرو دياب`")
        return
    song_name = " ".join(context.args)
    await update.message.reply_text(f"🎧 جاري البحث عن وتشغيل: **{song_name}** يا أسطورة... 🎶🔥")

# 3. الأوامر الإدارية (حظر، طرد، كتم، حذف)
async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("⚠️ رد على رسالة الشخص اللي عايز

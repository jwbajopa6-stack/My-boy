import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- كود البقاء حياً (Keep Alive) لـ Koyeb ---
app = Flask('')
@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تشغيل البوت باسم: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('أهلاً بك يا مصطفى! أنا شغال الآن على Koyeb')

# --- تشغيل البوت ---
keep_alive()
bot.run('MTQ5ODcyNTAzODA0NjcwNzg2NA.GjyAps.0V6wvtpam6-pMCniJ30Ir53Jx7DQCzwMFXaBaE') # امسح هذا السطر وضع توكن ديسكورد الخاص بك
